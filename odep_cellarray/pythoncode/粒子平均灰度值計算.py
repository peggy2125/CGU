'''import json
import cv2
import numpy as np
import math
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


# Function to calculate grayscale values along the circumference of a circle
def process_image_for_circles(json_path, img_path):
    # Read the image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Failed to load image.")
        return

    # Load the JSON data
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Loop through each shape (assuming all are circles)
    for shape in data['shapes']:
        if shape['shape_type'] == 'circle':
            # Get points
            x1, y1 = shape['points'][0]  # Center of the circle
            x2, y2 = shape['points'][1]  # A point on the circumference

            # Calculate the radius
            radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Store the grayscale values of the circumference pixels
            circumference_pixels = []

            # Traverse the circumference of the circle
            for angle in np.arange(0, 2 * np.pi, 0.01):  # Sweep angles from 0 to 2*pi
                x = int(x1 + radius * np.cos(angle))
                y = int(y1 + radius * np.sin(angle))

                # Make sure coordinates are within the image bounds
                if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
                    # Append the grayscale value at this point
                    circumference_pixels.append(img[y, x])

            # Calculate statistics
            if circumference_pixels:
                max_value = np.max(circumference_pixels)
                min_value = np.min(circumference_pixels)
                mean_value = np.mean(circumference_pixels)

                print(f"Circular shape at center ({x1:.2f}, {y1:.2f}), radius: {radius:.2f}")
                print(f"Max grayscale value: {max_value}")
                print(f"Min grayscale value: {min_value}")
                print(f"Average grayscale value: {mean_value}")
            else:
                print(f"No valid circumference pixels found for circle at center ({x1:.2f}, {y1:.2f}).")

# Main function to drive the program
def main():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    
    # 打開文件對話框以選擇資料夾
    json_path = askdirectory(title="選擇含有json標記檔的資料夾")
    image_path = askdirectory(title="選擇含有json標記檔的資料夾")
    file_number=0
    
    for json_name in os.listdir(json_path):
        file_number+=1
        if json_name.endswith('.json'):
            file_path = os.path.join(json_path,json_name)
            
            process_image_for_circles(json_path=, image_file)

if __name__ == "__main__":
    main()'''
    
import json
import cv2
import numpy as np
import math
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pandas as pd  # 用于生成 Excel 文件

# Function to calculate grayscale values along the circumference of a circle
def process_image_for_circles(json_path, img_path):
    # Read the image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Failed to load image: {img_path}")
        return None

    # Load the JSON data
    with open(json_path, 'r') as f:
        data = json.load(f)

    results = []

    # Loop through each shape (assuming all are circles)
    circle_num = 1
    for shape in data['shapes']:
        if shape['shape_type'] == 'circle':
            # Get points
            x1, y1 = shape['points'][0]  # Center of the circle
            x2, y2 = shape['points'][1]  # A point on the circumference

            # Calculate the radius
            radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Traverse the circumference of the circle
            for angle in np.arange(0, 2 * np.pi, 0.01):  # Sweep angles from 0 to 2*pi
                x = int(x1 + radius * np.cos(angle))
                y = int(y1 + radius * np.sin(angle))

                # Make sure coordinates are within the image bounds
                if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
                    # Append the grayscale value and the (x, y) coordinates
                    results.append([f"Circle {circle_num}", f"({x}, {y})", img[y, x]])

            circle_num += 1
    return results


# Main function to drive the program
def main():
    # 隐藏主 tkinter 窗口
    Tk().withdraw()
    
    # 打开文件对话框以选择包含 JSON 和图像的文件夹
    folder_path = askdirectory(title="选择包含JSON与图像的文件夹")
    if not folder_path:
        print("未选择文件夹。")
        return

    all_results = []  # 用于存储所有文件的结果

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            json_path = os.path.join(folder_path, file_name)
            img_name = file_name.replace('.json', '.png')  # 假设图像文件扩展名为 .png
            img_path = os.path.join(folder_path, img_name)
            
            # 如果图像文件存在，则处理
            if os.path.exists(img_path):
                print(f"Processing: {file_name}")
                results = process_image_for_circles(json_path, img_path)
                if results:
                    # Add file name as a header
                    all_results.append([file_name])  # 在每个文件前插入文件名
                    all_results.extend(results)  # 添加该文件的结果
                    all_results.append([])  # Add an empty row for separation
            else:
                print(f"Image file not found for {file_name}")

    # 将结果输出到 Excel
    if all_results:
        output_path = "D:\\CGU\\odep_cellarray\\circle_grayscale_values.xlsx"
        # 使用 pandas 将数据保存为 Excel 文件
        df = pd.DataFrame(all_results)
        df.to_excel(output_path, index=False, header=False)
        print(f"Results saved to {output_path}")
    else:
        print("No valid results to save.")

if __name__ == "__main__":
    main()
