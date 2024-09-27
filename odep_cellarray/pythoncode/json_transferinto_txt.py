import json
import os
import glob
from tkinter import Tk
from tkinter.filedialog import askdirectory

# 隱藏主視窗
Tk().withdraw()

# 選擇輸入資料夾
input_dir = askdirectory(title="選擇Labelme JSON檔案所在資料夾")
if not input_dir:
    print("未選擇輸入資料夾，程序結束。")
    exit()

# 選擇輸出資料夾
output_dir = askdirectory(title="選擇YOLO標註檔案輸出資料夾")
if not output_dir:
    print("未選擇輸出資料夾，程序結束。")
    exit()

# 定義類別對應字典
class_labels = {
    'target': 0,  # 根據您的類別名稱修改
    # 可以添加更多類別
}

def convert(size, points):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    result = []
    for point in points:
        x = point[0] * dw
        y = point[1] * dh
        result.append(x)
        result.append(y)
    return result

def decode_json(json_folder_path, json_name):
    json_path = os.path.join(json_folder_path, json_name)
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    img_w = data['imageWidth']
    img_h = data['imageHeight']
    txt_file_name = os.path.splitext(json_name)[0] + '.txt'
    txt_file_path = os.path.join(output_dir, txt_file_name)

    with open(txt_file_path, 'w') as txt_file:
        for shape in data['shapes']:
            label_name = shape['label']
            if label_name in class_labels:
                points = shape['points']
                xys = convert((img_w, img_h), points)
                txt_file.write(f"{class_labels[label_name]} " + " ".join(map(str, xys)) + '\n')

if __name__ == '__main__':
    os.makedirs(output_dir, exist_ok=True)  # 確保輸出資料夾存在
    json_files = glob.glob(os.path.join(input_dir, '*.json'))  # 獲取所有JSON檔案
    for json_file in json_files:
        decode_json(input_dir, os.path.basename(json_file))
    
    print("轉換完成！")