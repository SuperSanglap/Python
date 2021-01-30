import cv2
import matplotlib.pyplot as plt

try:
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.title('Image Camera-1')
    plt.imshow(img1)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    cap.release()
except Exception as e:
    print('Something Went Wrong!')