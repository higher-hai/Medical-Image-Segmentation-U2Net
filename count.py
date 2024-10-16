import cv2
import numpy as np

image = cv2.imread('test.jpg')  # 替换为自己的图像路径

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义绿色（阳性）和蓝色（阴性）的 HSV 范围
lower_green = np.array([40, 40, 40])  # 下限 (Hue, Saturation, Value)
upper_green = np.array([80, 255, 255])  # 上限

lower_blue = np.array([100, 40, 40])
upper_blue = np.array([140, 255, 255])

# 根据 HSV 阈值创建掩码
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

green_area = np.sum(green_mask > 0)
blue_area = np.sum(blue_mask > 0)

total_area = green_area + blue_area

# 计算阳性部分占比
if total_area > 0:
    green_ratio = green_area / total_area
    print(f"阳性占比: {green_ratio:.2%}")
else:
    print("没有检测到细胞")

cv2.imshow("Green Mask", green_mask)
cv2.imshow("Blue Mask", blue_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
