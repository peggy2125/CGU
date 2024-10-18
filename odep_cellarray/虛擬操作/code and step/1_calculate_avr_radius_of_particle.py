import os
import json
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory

def calculate_average_radius(folder_path):
    totalsum_radius = 0
    particle_count = 0
    file_number=0
    # 遍歷資料夾中的所有 JSON 檔案
    for filename in os.listdir(folder_path):
        file_number+=1
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)

            # 讀取 shapes 中的每個標記
            for shape in data.get('shapes', []):
                if shape['shape_type'] == 'circle' and len(shape['points']) == 2:
                    center = np.array(shape['points'][0])  # 圓心
                    perimeter_point = np.array(shape['points'][1])  # 圓上的一點

                    # 計算半徑
                    radius = np.linalg.norm(center - perimeter_point)
                    totalsum_radius += radius
                    particle_count += 1

    # 計算平均半徑
    average_radius = totalsum_radius / particle_count if particle_count > 0 else 0
    return average_radius, particle_count, file_number

# 使用範例
# 隱藏主 tkinter 視窗
Tk().withdraw()
    
# 打開文件對話框以選擇資料夾
folder_path = askdirectory(title="選擇含有json標記檔的資料夾")

average_radius, particle_count, file_number = calculate_average_radius(folder_path)
print(f'json檔案數量:{file_number}')
print(f'標記的粒子數為:{particle_count}')
print(f'所有標記的平均半徑為: {average_radius:.2f}')