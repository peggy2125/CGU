import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog

# 設定參數
size = 150  # 自訂array單格大小
width, height = 2 * size, 2 * size
bar_height = 2 * size

# 創建Tkinter窗口以獲取用戶輸入
root = tk.Tk()
root.withdraw()
bar_width = simpledialog.askinteger("Input", "Enter the width of light bar (integer):")
bar_width = int(bar_width)
radius_of_circle = 5
moved_circles_images = []
bad_circle = []
number = 0

# 讀取初始圖片
image_path = "D:\\CGU\\odep_cellarray\\Cell_Manipulation_Simulation\\virtual_test_image\\array_image\\arrayimage_0.png"  # 請替換為你的圖片路徑
img = cv2.imread(image_path)

# 確保圖片成功讀取
if img is None:
    raise ValueError("無法讀取圖片，請檢查路徑。")

# 獲取紅色圓形的位置（假設紅色圓形是純紅色）
circles = []
for y in range(1080):
    for x in range(1442):
        if (img[y, x, 2] == 255) and (img[y, x, 1] == 0) and (img[y, x, 0] == 0):
            circles.append((x, y))

# 設定長條的初始位置和速度
bar_x_position = width + 10  # 初始位置在右側
speed = 3  # 每幀移動的像素數

# 模擬運動並顯示圖像
while True:
    # 使用原始圖像作為背景，這樣可以避免重疊問題
    display_img = img.copy()
    number += 1

    # 繪製白色長條
    cv2.rectangle(display_img, (bar_x_position, 0), (bar_x_position + bar_width, bar_height), (255, 255, 255), thickness=cv2.FILLED)

    # 清空 bad_circle 並重新檢查符合條件的圓形
    bad_circle.clear()
    
    for circle in circles:
        circle_x, circle_y = circle
        
        if circle_x <= 2 * size and circle_y <= 2 * size:
            bad_circle.append(circle)

    # 檢查 bad_circle 中的所有圓形是否碰到長條邊緣
    for circle in bad_circle:
        circle_x, circle_y = circle
        
        if bar_x_position <= circle_x <= bar_x_position + bar_width:  # 檢查圓形是否碰到長條的邊緣
            
            # 計算斥力效果，將圓形推開
            new_circle_x = circle_x - speed
            
            # 更新圓形位置並保存圖像
            update_circle_coordinate = (new_circle_x, circle_y)
            circles.remove(circle)  # 從原始列表中移除舊位置的圓形
            circles.append(update_circle_coordinate)  # 將更新後的位置添加回列表中

    # 繪製紅色圓形，確認半徑為5
    for circle in circles:
        cv2.circle(display_img, circle, radius_of_circle, (0, 0, 255), -1)

    # 更新長條位置向左移動
    bar_x_position -= speed
    
    # 創建可調整大小的窗口並設置為正常模式
    cv2.namedWindow('Animation', cv2.WINDOW_NORMAL)
    
    # 根據圖像大小設置窗口尺寸，確保不會被放大或縮小
    cv2.resizeWindow('Animation', display_img.shape[1], display_img.shape[0])  
    
    print(f"Image shape: {display_img.shape}, Circle Radius: {radius_of_circle}")
    
    # 顯示當前幀
    cv2.imshow('Animation', display_img)

    # 每幀延遲33毫秒（約30幀每秒）
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
    
    output_path = f'D:\\CGU\\odep_cellarray\\Cell_Manipulation_Simulation\\virtual_test_image\\cleanparticle_at_array_image\\{number}.png'
    cv2.imwrite(output_path, display_img)
    print(f"結果已輸出至: {output_path}")

# 清理資源
cv2.destroyAllWindows()