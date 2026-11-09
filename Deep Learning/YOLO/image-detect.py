from ultralytics import YOLO
import cv2

model=YOLO(r"C:\Users\Karan\Downloads\yolov8s.pt")
image_path=r"C:\Users\Karan\Downloads\WhatsApp Image 2026-11-06 at 12.53.20 PM.jpeg"
img=cv2.imread(image_path)

if img is None:
    print('Error: No image found')

results = model(img)
print(results)