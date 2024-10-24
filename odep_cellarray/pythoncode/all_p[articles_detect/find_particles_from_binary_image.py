import cv2
import numpy as np
import os

def find_circles_and_save(image_path, output_txt_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return

    # 使用 HoughCircles 找圆
    circles = cv2.HoughCircles(image, 
                               cv2.HOUGH_GRADIENT, 
                               dp=1, 
                               minDist=10, 
                               param1=50, 
                               param2=15, 
                               minRadius=4, 
                               maxRadius=7)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print(f"Found {len(circles)} circles.")
        
        # 打开文本文件并写入圆心坐标
        with open(output_txt_path, "w") as f:
            for (x, y, r) in circles:
                f.write(f"Center: ({x}, {y}), Radius: {r}\n")
                
        print(f"Circles saved to {output_txt_path}")
        
        # 显示检测结果
        output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for (x, y, r) in circles:
            cv2.circle(output_image, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output_image, (x, y), 2, (0, 0, 255), 3)
        
        cv2.imshow('Detected Circles', output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No circles found.")

# 图像路径
image_path = "/mnt/data/2024.09.19_001.png"

# 输出文本路径
output_txt_path = "detected_circles.txt"

# 检测圆并保存圆心到TXT文件
find_circles_and_save(image_path, output_txt_path)
