import json
import os
import numpy as np
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askdirectory

def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data


def load_txt(txt_path):
    centers = []
    with open(txt_path, 'r') as f:
        for line in f:
            # 通过字符串拆分提取圆心
            if "Center" in line:
                parts = line.split("Center: (")[1].split("), Radius:")[0]
                x, y = map(int, parts.split(", "))  # 提取x和y并转换为整数
                centers.append((x, y))
    return centers


def is_point_in_circle(px, py, cx, cy, radius):
    return (px - cx) ** 2 + (py - cy) ** 2 <= radius ** 2

def compare_circles(json_path, txt_path):
    # Load JSON and TXT data
    json_data = load_json(json_path)
    txt_circles = load_txt(txt_path)

    json_circles = []
    for shape in json_data['shapes']:
        if shape['shape_type'] == 'circle':
            # Extract circle center and radius from JSON
            x1, y1 = shape['points'][0]
            x2, y2 = shape['points'][1]
            radius = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            json_circles.append((x1, y1, radius))

    # Compare circles
    txt_in_json_count = 0
    txt_not_in_json_count = 0
    json_missed_count = 0
    checked_json = [False] * len(json_circles)

    for txt_x, txt_y in txt_circles:
        found_in_json = False
        for i, (json_x, json_y, radius) in enumerate(json_circles):
            if is_point_in_circle(txt_x, txt_y, json_x, json_y, radius):
                found_in_json = True
                checked_json[i] = True
                break
        if found_in_json:
            txt_in_json_count += 1
        else:
            txt_not_in_json_count += 1
    filename = os.path.splitext(os.path.basename(json_path))[0]
    json_missed_count = len(json_circles) - sum(checked_json)

    return {
        'filename': filename,
        'JSON circles': len(json_circles),
        'TXT circles': len(txt_circles),
        'Correctly matched circles': txt_in_json_count,
        'TXT circles not in JSON': txt_not_in_json_count,
        'JSON circles missed in TXT': json_missed_count
    }
    

    


# main
Tk().withdraw() 
# 打開文件對話框以選擇資料夾
#json_folder = askdirectory(title="選擇樣比對的json檔資料夾")
txt_folder = askdirectory(title="選擇樣比對的txt檔資料夾")
json_folder = "D:/CGU/odep_cellarray/detecting_testing_data/binaryimage_and_json/json"
#txt_folder = "D:/CGU/odep_cellarray/detecting_testing_data/binaryimage_and_json/binary_threshold(75)/FIND_CPARTICLES_TXT"
output_excel_path= askdirectory(title="選擇輸出excel資料夾")
files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

results = []
for file in files:
    json_path = os.path.join(json_folder, file)
    base_filename = os.path.splitext(os.path.basename(json_path))[0]
    print(base_filename)
    txt_path = os.path.join(txt_folder, base_filename)
    output_excel = (f"{output_excel_path}_compareresult.xlsx")
    result=compare_circles(json_path, txt_path)
    results.append(result)
        # 将结果导出为 Excel 文件
    df = pd.DataFrame(results)
    df.to_excel(output_excel, index=False)
    print(f"Results saved to {output_excel}")
