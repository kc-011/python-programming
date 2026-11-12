from ultralytics import YOLO
import cv2

#model=YOLO("yolov8s.pt")
model=YOLO(r"C:\Users\Karan\Downloads\yolov8s.pt\yolov8s")
image_path=r"C:\Users\Karan\Downloads\IMG_4094.jpeg"
img=cv2.imread(image_path)

if img is None:
    print('Error: No image found')
    exit()
    
results = model(img)
annotated = results[0].plot()
print('\nDetected Objects:')
for box in results[0].boxes:
    cls = int(box.cls[0])
    conf = float(box.conf[0])
    x1,y1,x2,y2 = box.xyxy[0]
    print(f"{model.names[cls].title()} | Confidence : {conf:.2f} | box: {x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f}")

cv2.imshow("YOLO Detection",annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result.jpg",annotated)
print("Over")
