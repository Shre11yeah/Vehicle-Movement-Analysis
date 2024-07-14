import cv2
import numpy as np
import os
import datetime
import matplotlib.pyplot as plt
import easyocr
import imutils

# Function to correct license plate text if needed
def correct_license_plate(text):
    # Implement your logic here for text correction if required
    # Example: Convert to uppercase and remove non-alphanumeric characters
    corrected_text = text.upper().replace(' ', '').replace('-', '')
    return corrected_text

def main():
    # Load Haar cascade for license plate detection
    haar_cascade_path = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\haarcascade_russian_plate_number.xml'
    plate_cascade = cv2.CascadeClassifier(haar_cascade_path)

    # Load YOLOv4 model
    yolo_config_path = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\yolov4.cfg'
    yolo_weights_path = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\yolov4.weights'
    model_classes = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\cfg\\coco.names'
    net = cv2.dnn.readNetFromDarknet(yolo_config_path, yolo_weights_path)
    
    if net.empty():
        print("Error: Could not load YOLOv4 network.")
        return
    
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # Open video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    img_display = ax.imshow(np.zeros((480, 640, 3), dtype=np.uint8))

    # Ensure the results directory exists
    results_dir = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result'
    os.makedirs(results_dir, exist_ok=True)

    detected_plates = []  # List to track detected license plates

    # Approved database
    approved_db = {
        "MH27BE6630": "Authorized", "MH27BV8448": "Authorized", "MH27BV6826": "Authorized",
        "MH27DE7731": "Authorized", "MH27BE2954": "Authorized", "MH27DE8408": "Authorized",
        "MH27BE7477": "Authorized", "MH01CP1574": "Authorized", "MH29R4300": "Authorized",
        "MH27DL7212": "Authorized", "MH27BE9889": "Authorized", "MH27DL4474": "Authorized",
        "MH27BZ4676": "Authorized", "MH27DE9744": "Authorized", "MH27BE4704": "Authorized",
        "MH14JU4530": "Authorized", "MH27AC3897": "Authorized"
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from video capture.")
            break

        print("Frame captured successfully.")

        # Use YOLOv4 to detect vehicles
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

        detections = net.forward(output_layers)

        vehicles = []
        for detection in detections:
            for obj in detection:
                scores = obj[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    if class_id == 2:  # Assuming class_id 2 is for vehicles in your YOLOv4 config
                        box = obj[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                        (center_x, center_y, width, height) = box.astype("int")
                        x = int(center_x - (width / 2))
                        y = int(center_y - (height / 2))
                        vehicles.append((x, y, int(width), int(height)))

        print(f"Detected {len(vehicles)} vehicles.")

        for (x, y, w, h) in vehicles:
            vehicle_roi = frame[y:y+h, x:x+w]

            # Check if vehicle_roi is empty or None
            if vehicle_roi is None or vehicle_roi.size == 0:
                continue

            # License plate detection and OCR processing on vehicle_roi
            plates = plate_cascade.detectMultiScale(cv2.cvtColor(vehicle_roi, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (px, py, pw, ph) in plates:
                plate = vehicle_roi[py:py+ph, px:px+pw]

                # Preprocessing plate region
                gray_plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray_plate, 150, 255, cv2.THRESH_BINARY_INV)
                plate = cv2.bitwise_and(plate, plate, mask=thresh)

                # OCR Processing
                reader = easyocr.Reader(['en'])
                result = reader.readtext(plate)

                if result:
                    text = result[0][-2]
                    corrected_text = correct_license_plate(text)

                    if corrected_text not in detected_plates:
                        detected_plates.append(corrected_text)

                        # Check authorization using approved_db
                        if corrected_text in approved_db:
                            authorization_status = approved_db[corrected_text]
                        else:
                            authorization_status = 'Unauthorized'  # Default to unauthorized if not found

                        font = cv2.FONT_HERSHEY_SIMPLEX
                        frame = cv2.putText(frame, text=corrected_text, org=(px, py - 10), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                        frame = cv2.rectangle(frame, (px, py), (px + pw, py + ph), (0, 255, 0), 3)

                        # Save detected license plate image
                        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                        img_path = os.path.join(results_dir, f'detected_license_plate_{timestamp}.jpg')
                        cv2.imwrite(img_path, frame)
                        print(f"Detected license plate image saved: {img_path}")

                        # Save metadata
                        metadata = {
                            'vehicle_image_path': img_path,
                            'vehicle_timestamp': timestamp,
                            'license_plate': corrected_text,
                            'authorization_status': authorization_status
                        }

                        metadata_file = os.path.join(results_dir, f'detected_license_plate_metadata_{timestamp}.txt')
                        with open(metadata_file, 'w') as f:
                            for key, value in metadata.items():
                                f.write(f"{key}: {value}\n")
                        print(f"Metadata saved: {metadata_file}")

        # Display the frame with detections
        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        fig.canvas.draw()
        plt.pause(0.001)

        # Check if 'q' was pressed to break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
