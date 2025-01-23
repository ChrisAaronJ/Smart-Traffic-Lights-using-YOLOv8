import cv2
from ultralytics import YOLO
import serial
import time

# Initialize YOLO model
model = YOLO('yolov8n.pt')

# Initialize serial communication with Arduino
arduino = serial.Serial('COM5', 9600)  # Replace 'COM5' with your Arduino COM port
time.sleep(2)  # Wait for Arduino to initialize

cap = cv2.VideoCapture(0)  # Access the webcam

if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        results = model(frame)  # Run YOLO detection
        car_detected = False
        
        for r in results[0].boxes.data.tolist():
            # Extract bounding box and class information
            x1, y1, x2, y2, conf, cls = r
            cls = int(cls)  # Class index
            
            # Check if the detected object is a car
            if model.names[cls] == "car":
                car_detected = True
                
                # Draw bounding box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                # Add label
                label = f"Car: {conf:.2f}"
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Send data to Arduino
        if car_detected:
            arduino.write(b'G')  # Send 'G' to Arduino for green signal
            print("Signal is green")
        else:
            arduino.write(b'R')  # Send 'R' to Arduino for red signal
            print("Signal is red")
        
        # Display the frame with annotations
        cv2.imshow("Car Detection", frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()



