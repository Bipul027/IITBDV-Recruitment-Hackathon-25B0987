from ultralytics import YOLO
import cv2
model = YOLO("./YOLOv11s-Carmaker.pt")
img = cv2.imread("./image.png")
results = model(img)
results[0].save("./output.jpg")
cone_height = 0.3
focal_length = 1000
detections = []
for i in range(len(results[0].boxes)):
    box = results[0].boxes[i]
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    bbox_height = y2 - y1
    distance = (cone_height * focal_length) / bbox_height

    detections.append(distance)
    label = f"d: {distance:.2f}"
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.putText(img, label, (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (255,255,255), 2)
    
cv2.imwrite("output.jpg", img)

# Print the list of detected cones
for i in range(len(detections)):
    print(f"Cone {i+1}: d = {detections[i]:.2f}\n")