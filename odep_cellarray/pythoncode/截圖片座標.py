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
    
    height, width, channels = image.shape
    print("原始圖像大小 (寬 x 高):", width, "x", height)
    
    # 轉換為灰階圖
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 對圖像進行二值化處理
    _, thresh = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
    
    # 找到輪廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 假設最大的輪廓是我們關心的物體
    largest_contour = max(contours, key=cv2.contourArea)
    
    # 獲取邊界矩形
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # 計算四個角的座標
    top_left = (x, y)
    top_right = (x + w, y)
    bottom_left = (x, y + h)
    bottom_right = (x + w, y + h)
    
    corners = [top_left, top_right, bottom_left, bottom_right]
    
    # 檢查四個角是否形成正方形
    side1 = np.linalg.norm(np.array(top_left) - np.array(top_right))
    side2 = np.linalg.norm(np.array(top_left) - np.array(bottom_left))
    
    is_square = np.isclose(side1, side2)
    
    print("四角座標 (x, y):", corners)
    print("是否為正方形:", is_square)

if __name__ == "__main__":
    main()
