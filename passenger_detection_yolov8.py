import os
import cv2
from ultralytics import YOLO

# =========================
# Config (easy to change)
# =========================
VIDEO_PATH = "sample_video.mp4"   # Change this to your video path
MODEL_PATH = "yolov8n.pt"         # Pretrained YOLOv8 nano model


def main():
    # Basic path validation
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: Video file not found at '{VIDEO_PATH}'")
        return

    # Load YOLO model
    try:
        model = YOLO(MODEL_PATH)
    except Exception as e:
        print(f"Error: Failed to load model '{MODEL_PATH}': {e}")
        return

    # Open video file
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"Error: Could not open video '{VIDEO_PATH}'")
        return

    # Process video frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:
            # End of video or frame read failure
            break

        # Run YOLO detection on current frame
        results = model(frame, verbose=False)

        people_count = 0

        # Filter detections to class 'person' only, then draw boxes
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id]

                if class_name == "person":
                    people_count += 1

                    # Bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Draw person bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Optional label
                    cv2.putText(
                        frame,
                        "person",
                        (x1, max(y1 - 8, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2
                    )

        # Display people count at top-left
        cv2.putText(
            frame,
            f"People count: {people_count}",
            (10, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 255),
            2
        )

        # Show output frame
        cv2.imshow("Passenger Detection - YOLOv8", frame)

        # Press 'q' to quit cleanly
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources properly
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
