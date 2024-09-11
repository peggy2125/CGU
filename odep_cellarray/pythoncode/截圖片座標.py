import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    
    # 打開文件對話框以選擇圖片
    filename = askopenfilename(title="選擇圖片", filetypes=[("圖片檔案", "*.jpg;*.jpeg;*.png")])
    
    # 加載圖片
    image = cv2.imread(filename)
    
    cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
    cv2.imshow('Image Window', image)

    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉所有窗口
    
    # 獲取原始圖像大小
    height, width, channels = image.shape
    print("原始圖像大小 (寬 x 高):", width, "x", height)
    
    
    # 轉換為灰階圖
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉所有窗口
    # 對圖像進行二值化處理
    _, binary = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)
    
    # 顯示二值化後的圖像
    cv2.imshow('Binary Image', binary)
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉所有窗口

    # 找到輪廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 假設最大的輪廓是我們關心的物體
    largest_contour = max(contours, key=cv2.contourArea)
    
    # 獲取邊界矩形
    x, y, w, h = cv2.boundingRect(largest_contour)

    # 創建新圖像 cropped
    cropped = image[y:y+h, x:x+w].copy()
    
    # 顯示裁剪後的圖像
    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉所有窗口
    
    # 計算四個角的座標
    top_left = (x, y)
    top_right = (x + w, y)
    bottom_left = (x, y + h)
    bottom_right = (x + w, y + h)
    
    corners = [top_left, top_right, bottom_left, bottom_right]
    
    
    # 輸出結果
    print("四角座標 (x, y):", corners)
    print("切割圖像大小:",(w,h))

if __name__ == "__main__":
    main()
