import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog,simpledialog
import os

def select_png_file():
    # 隱藏主視窗
    root = tk.Tk()
    root.withdraw()

    # 使用 askopenfilename 選擇 PNG 檔案
    file_path = filedialog.askopenfilename(
        title='選擇 PNG 檔案',
        filetypes=[('PNG Files', '*.png')]
    )

    # 打印選擇的檔案路徑
    if file_path:
        print(f'選擇的檔案: {file_path}')
        return file_path
    else:
        print('未選擇任何檔案')

def generate_array(image,size):
    # 繪製四個正方形
    for i in range(2):
        for j in range(2):
            top_left = (i * size, j * size)  # 左上角座標
            bottom_right = (top_left[0] + size, top_left[1] + size)  # 右下角座標
            
            # 繪製虛線正方形
            cv2.rectangle(image, top_left, bottom_right, (255, 191, 0), 2)

    area_image=image.copy()
    #area_of_chip
    cv2.line(area_image, (2*size, 2*size), (2*size, 1080), (238, 238, 174), 2)
    cv2.line(area_image, (2*size, 2*size), (1442, 2*size), (238, 238, 174), 2)
    x=int(size+1442/2.5) 
    y=int(2*size-30)
    cv2.putText(area_image, 'A' , (x,y), cv2.FONT_HERSHEY_TRIPLEX, 10, (238, 238, 174), 2)
    cv2.putText(area_image, 'B' , (x,y+500), cv2.FONT_HERSHEY_TRIPLEX, 10, (238, 238, 174), 2)
    cv2.putText(area_image, 'C' , (x-650,y+500), cv2.FONT_HERSHEY_TRIPLEX, 10, (238, 238, 174), 2)
    return image , area_image

   

if __name__ == '__main__':
    file_path=select_png_file()
    image=cv2.imread(file_path)
    file_name = os.path.basename(file_path)
    name, extension = os.path.splitext(file_name)
    #set size of each square arraysize
    root = tk.Tk()
    root.withdraw()
    size = simpledialog.askinteger("Input", "Enter the size of each square in the array (integer):")
    size=int(size)
    arrayimage, arrayimage_with_area=generate_array(image,size)
    
    # showimage_with_array
    cv2.imshow('Array of Squares', arrayimage )
    cv2.imshow('3 area of chip', arrayimage_with_area)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_directory=os.path.dirname(file_path)
    array_image_path = os.path.join(save_directory, f'arrayimage_{file_name}.png')
    area_image_path = os.path.join(save_directory, f'3_area_of_chip_{file_name}.png')
    cv2.imwrite(array_image_path, arrayimage)
    cv2.imwrite(area_image_path , arrayimage_with_area)