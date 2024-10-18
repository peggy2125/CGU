import numpy as np
import cv2
import os
import tkinter as tk
from tkinter import filedialog,simpledialog
import math

def select_png_file():
    # 隱藏主視窗
    root = tk.Tk()
    root.withdraw()

    # 使用 askopenfilename 選擇 PNG 檔案
    file_path = filedialog.askopenfilename(
        title='選擇 txt 檔案',
        filetypes=[('txt Files', '*.txt')]
    )

    # 打印選擇的檔案路徑
    if file_path:
        print(f'選擇的檔案: {file_path}')
        return file_path
    else:
        print('未選擇任何檔案')


def read_and_form_sort_4list(txt_path):
    all_coordinates = []  # 初始化空列表以存儲座標

    # 打開文本檔案並讀取座標
    with open(txt_path, 'r') as f:
        for line in f:
            # 去除行末的換行符號，然後將字符串轉換為元組
            point = eval(line.strip())  # 使用 eval() 將字符串轉換為元組
            all_coordinates.append(point)  # 將座標添加到列表中
    
    all_sorted_coordinates = sorted(all_coordinates, key=lambda point: math.sqrt(point[0]**2 + point[1]**2))
    return all_sorted_coordinates

def calculate_distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def picking_target(all_coordinate,R):
    target_coordinate=[]
    variable_obstacle_coordinate=[]
    
    while len(all_coordinate) >= 4:
        # 取前四个坐标
        current_points = all_coordinate[:4]
        keep_indices = [0, 1, 2, 3]  # 跟踪要保留的索引

        # 比较每对点之间的距离
        for i in range(3):
            for j in range(i + 1, 4):
                if calculate_distance(current_points[i], current_points[j]) < R:
                    # 如果距离小于 R，保留索引较小的点
                    if i < j:
                        keep_indices[j] = None  # 标记为移除
                    else:
                        keep_indices[i] = None  # 标记为移除

        # 筛选出有效的点并更新目标坐标
        kept_points = [current_points[i] for i in keep_indices if i is not None]
        for i in kept_points
        target_coordinate.extend(kept_points)
 
        # 移动被移除的点到可变障碍坐标列表中
        for i in keep_indices:
            if i is None:
                continue  # 已经被保留
            variable_obstacle_coordinate.append(current_points[i])

        # 从 all_coordinate 中移除已处理的点
        all_coordinate = all_coordinate[4:]

    return target_coordinate, variable_obstacle_coordinate

# 示例用法
all_coordinates = [(0, 0), (1, 1), (2, 2), (3, 3), (5, 5), (8, 8)]
R = 2.5
targets, obstacles = picking_target(all_coordinates, R)
print("目标坐标:", targets)
print("可变障碍坐标:", obstacles)
    












if __name__ == '__main__':
    #generate 4 list
    all_coordinate=[]
    target_coordinate=[]
    variable_obstacle_coordinate=[]
    stable_obstacle_coordinate=[]
    
    #get txt file
    txt_filepath=select_png_file()
    #generating all_cooridinate
    all_coordinate=read_and_form_sort_4list(txt_filepath)
    #picking 4 target and get variable_obstacle_coordinate
    picking_target(all_coordinate)
    