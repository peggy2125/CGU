import cv2
import numpy as np
import os

'''def find_circles_and_save(image_path, output_txt_path):
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
image_path = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\binary_threshold(75)\\IMAGE\\2024.09.18_001.png"

# 输出文本路径
output_txt_path = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\binary_threshold(75)\\FIND_CPARTICLES_TXT\\detected_circles.txt"

# 检测圆并保存圆心到TXT文件
find_circles_and_save(image_path, output_txt_path)
'''
import cv2
import numpy as np

def find_circles_from_binary(image_path, output_txt_path):
    # 读取二值图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 确保图像正确加载
    if image is None:
        print(f"Error: Failed to load image from {image_path}")
        return
    
    # 调整图像类型：确保是8-bit单通道
    if image.dtype != np.uint8:
        image = (image * 255).astype(np.uint8)
    
    # 检查图像属性
    print(f"Image loaded: {image.shape}, dtype: {image.dtype}")
    
    # 使用高斯模糊减少噪声
   # blurred_image = cv2.GaussianBlur(image, (9, 9), 2)
    
    # 使用 HoughCircles 找圆
    circles = cv2.HoughCircles(image, 
                               cv2.HOUGH_GRADIENT, 
                               dp=1, 
                               minDist=10, 
                               param1=50, 
                               param2=4.5,  # 调整 param2 以适应检测精度
                               minRadius=4, 
                               maxRadius=6)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print(f"Found {len(circles)} circles.")
        
        # 打开文本文件并写入圆心坐标
        with open(output_txt_path, "w") as f:
            for (x, y, r) in circles:
                f.write(f"Center: ({x}, {y}), Radius: {r}\n")
                
        print(f"Circles saved to {output_txt_path}")
        
        # 在图像上绘制检测到的圆
        output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for (x, y, r) in circles:
            cv2.circle(output_image, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output_image, (x, y), 2, (0, 0, 255), 3)
        
        scale_percent = 50  # 缩放比例
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(output_image, dim, interpolation=cv2.INTER_AREA)

        # 显示检测结果
        cv2.imshow('Detected Circles', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No circles found.")


# Set the directory containing your files
directory = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\binary_threshold(75)\\IMAGE"
# # Get a list of all tiff files
num=0
files = [f for f in os.listdir(directory) if f.endswith('.png')]
for image in files:
    num+=1
    image_path = os.path.join(directory, image)
    print(num)
    base_filename = os.path.splitext(os.path.basename(image_path))[0]  # 去掉扩展名
    output_folder = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\binary_threshold(75)\\FIND_CPARTICLES_TXT"
    output_txt_path = os.path.join(output_folder, base_filename)  # 指定输出路径
    find_circles_from_binary(image_path, output_txt_path)


