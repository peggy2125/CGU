import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pyautogui
import keyboard

def screenshot_by_keyboardspace():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    

    # 打開文件對話框以選擇資料夾
    save_folderdirc = askdirectory(title="選擇存放截圖的資料夾")

    if not save_folderdirc:
        print("未選擇資料夾，程式結束。")
        return
        
    
    # 設置截圖的座標範圍
    x1, y1 = 239, 0
    
    number=0
    print("每當按下空白鍵時截圖，按下end鍵後終止程式")
    
    # 等待空白鍵被按下
    keyboard.wait('space')  # 等待空白鍵按下


      # 設置一個標誌來控制截圖循環

    while True:
        
        if keyboard.is_pressed('space'):
            # 截取螢幕
            screenshot_pil = pyautogui.screenshot(region=( x1, y1, 1442, 1080))
        
            #PIL(BRG)轉換為RGB(opencv默認)
            screenshot_numpy = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)
        
            number+=1
        
            # 保存截圖
            save_path = os.path.join(save_folderdirc, f"{number}.png")
            cv2.imwrite(save_path, screenshot_numpy)
             
            # 檢查是否按下空白鍵以停止截圖
        if keyboard.is_pressed('end'):
            print("截圖程序結束")
            print("截圖數量:",number)
            break


screenshot_by_keyboardspace()
