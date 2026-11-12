from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\Karan\Downloads\yolov8n.pt\yolov8n")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Cannot access webcam')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to read webcam")
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Live Object Detection", annotated_frame)
    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()