import numpy as np
import cv2
import os
import tkinter as tk
from tkinter import filedialog,simpledialog
import math

def select_file(a):
    # 隱藏主視窗
    root = tk.Tk()
    root.withdraw()
    
    if a==0:
        # 使用 askopenfilename 選擇 PNG 檔案
        file_path = filedialog.askopenfilename(
        title='選擇 txt 檔案',
        filetypes=[('txt Files', '*.txt')]
        )
    else:
        # 使用 askopenfilename 選擇 PNG 檔案
        file_path = filedialog.askopenfilename(
        title='選擇 png 檔案',
        filetypes=[('png Files', '*.png')]
        )

    # 打印選擇的檔案路徑
    if file_path:
        print(f'選擇的檔案: {file_path}')
        return file_path
    else:
        print('未選擇任何檔案')


def read_and_form_sort_4list(txt_path,size):
    all_coordinates = []  # 初始化空列表以存儲座標

    # 打開文本檔案並讀取座標
    with open(txt_path, 'r') as f:
        for line in f:
            # 去除行末的換行符號，然後將字符串轉換為元組
            point = eval(line.strip())  # 使用 eval() 將字符串轉換為元組
            if point[0] > 2 * size or point[1] > 2 * size:
                all_coordinates.append(point)  # 将坐标添加到列表中
              # 將座標添加到列表中
    
    all_sorted_coordinates = sorted(all_coordinates, key=lambda point: math.sqrt(point[0]**2 + point[1]**2))
    return all_sorted_coordinates

def calculate_distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def picking_target(all_coordinate,R):
    target_coordinate=[]
    variable_obstacle_coordinate=[]
    skip_point_count=1#紀錄被捨棄的點
    iretaion_time=0
    if len(all_coordinate) >= 4:
    # 取前四个坐标
        current_points = all_coordinate[:4]
        keep_indices = [0, 1, 2, 3]  # 跟踪要保留的索引
        all_coordinate = all_coordinate[4:] #只有第一次確定擷4個
        while skip_point_count!=0:
            # 重置移至垃圾區的counts
            skip_point_count=0
            # 比较每对点之间的距离
            for i in range(3):
                for j in range(i + 1, 4):
                    if calculate_distance(current_points[i], current_points[j]) < R:
                        # 如果距离小于 R，保留索引较小的点
                        if i < j:
                            keep_indices[j] = None  # 标记为移除
                        else:
                            keep_indices[i] = None  # 标记为移除
            x=len(keep_indices)
            for i in range (x):
                if keep_indices[i] is None:
                    variable_obstacle_coordinate.append(current_points[i])
                    current_points.pop(i)
                    skip_point_count+=1
            #current poin與indice重置
            if skip_point_count>0:
                current_points.extend(all_coordinate[:skip_point_count])
                keep_indices = keep_indices = list(range(len(current_points)))       
            # 从 all_coordinate 中移除已处理的点
            if iretaion_time>0:
                all_coordinate = all_coordinate[skip_point_count:]
            iretaion_time+=1
            
        for i in keep_indices:
            if i is not None:
                target_coordinate.append(current_points[i])
            else:
                print("error")
        #非target全部移入obstacle
        x=len(all_coordinate)
        for i in range(x):
            if len(all_coordinate) >= 0:
                variable_obstacle_coordinate.append(all_coordinate[i])
            else:
                break
        #確認用
        print(f'length of target_coordinate={len(target_coordinate)}')
        print(f'length of variable obstacle coordinate={len(variable_obstacle_coordinate)}')
        return target_coordinate, variable_obstacle_coordinate
    else:
        print("all_coordinate list length error")

def draw_light_image(image,target_coordinate,variable_obstacle_coordinate,R):
    raw_image=image.copy()
    good=len(target_coordinate)
    bad=len(variable_obstacle_coordinate)
    for i in range(good):
        cv2.circle(image,target_coordinate[i],R,(250,250,255),10)  # 繪製圓形
    for i in range(bad):
        cv2.circle(image,variable_obstacle_coordinate[i],10,(238,238,174),1)  # 繪製圓形
    return raw_image,image    
        
        
        
        

if __name__ == '__main__':
    #generate 4 list
    all_coordinate=[]
    target_coordinate=[]
    variable_obstacle_coordinate=[]
    stable_obstacle_coordinate=[]
    
    #get txt file
    txt_filepath=select_file(0)
    #generating all_cooridinate
    all_coordinate=read_and_form_sort_4list(txt_filepath,size=150)
    print(f'length of all_coordinate list={len(all_coordinate)}')
    #picking 4 target and get variable_obstacle_coordinate
    target_coordinate, variable_obstacle_coordinate=picking_target(all_coordinate,R=20)
    
    #驗證用
    image_filepath= select_file(1)
    image=cv2.imread(image_filepath)
    raw_image,processed_image=draw_light_image(image,target_coordinate, variable_obstacle_coordinate,R=20)
    cv2.imshow('processed image', processed_image )
    cv2.imshow('raw image', raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    