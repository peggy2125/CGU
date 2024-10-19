import numpy as np
import cv2

def moving_circle(radius, height, frames):
    # 初始圓心位置
    center_x = 721  # 畫布寬度的一半
    center_y = 1080 - radius  # 初始位置在底部

    for i in range(frames):
        # 創建黑色畫布
        canvas = np.zeros((1080, 1442, 3), dtype=np.uint8)

        # 計算新的圓心位置
        center_y -= height  # 每幀向上移動指定的高度

        # 繪製紅色圓形
        cv2.circle(canvas, (center_x, int(center_y)), radius, (0, 0, 255), -1)

        # 顯示當前幀
        cv2.imshow('Moving Circle', canvas)

        # 等待 100 毫秒，並檢查是否按下 'q' 鍵以退出
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

# 使用範例
radius = 10      # 圓的半徑
frames = 100     # 總幀數
height = 10      # 每幀向上移動的高度

moving_circle(radius, height, frames)