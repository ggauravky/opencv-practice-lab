import os
import sys
import cv2

# Paths to Haar cascade files
BASE_DIR = r"C:\Users\Lenovo\VS Code Files\Python\OpenCV\008 Face & Object Detection"
CASCADE_FACE = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")
CASCADE_EYE = os.path.join(BASE_DIR, "haarcascade_eye.xml")
CASCADE_SMILE = os.path.join(BASE_DIR, "haarcascade_smile.xml")

# Load cascade classifiers
print("Loading cascade files...")
face_cascade = cv2.CascadeClassifier(CASCADE_FACE)
eye_cascade = cv2.CascadeClassifier(CASCADE_EYE)
smile_cascade = cv2.CascadeClassifier(CASCADE_SMILE)

# Verify all cascades loaded successfully
if face_cascade.empty():
    print(f"Error: failed to load face cascade from: {CASCADE_FACE}")
    sys.exit(1)
if eye_cascade.empty():
    print(f"Error: failed to load eye cascade from: {CASCADE_EYE}")
    sys.exit(1)
if smile_cascade.empty():
    print(f"Error: failed to load smile cascade from: {CASCADE_SMILE}")
    sys.exit(1)

print("All cascade files loaded successfully!")
print("Attempting to open camera...")

# Try multiple camera backends
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DirectShow for Windows
if not cap.isOpened():
    print("Failed with CAP_DSHOW, trying default backend...")
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: cannot open camera with index 0")
    print("Trying camera index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: cannot open any camera")
    print("\nTroubleshooting tips:")
    print("1. Check if camera is connected and not used by another app")
    print("2. Grant camera permissions to Python in Windows settings")
    print("3. Try running: python -c 'import cv2; print(cv2.__version__)'")
    sys.exit(1)

print(f"Camera opened successfully!")
print("\nControls:")
print("  Press 'q' to quit")
print("  Press 's' to toggle smile detection")
print("  Press 'e' to toggle eye detection\n")

# Feature toggles
detect_eyes = True
detect_smile = True

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Warning: failed to read frame from camera. Exiting loop.")
            break

        # Convert to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for x, y, w, h in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "Face",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

            # Region of interest for face
            roi_gray = gray[y : y + h, x : x + w]
            roi_color = frame[y : y + h, x : x + w]

            # Detect eyes within face region
            if detect_eyes:
                eyes = eye_cascade.detectMultiScale(
                    roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15)
                )
                for ex, ey, ew, eh in eyes:
                    cv2.rectangle(
                        roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2
                    )
                    cv2.putText(
                        roi_color,
                        "Eye",
                        (ex, ey - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.4,
                        (255, 0, 0),
                        1,
                    )

            # Detect smile within face region
            if detect_smile:
                # Focus on lower half of face for smile detection
                smile_roi_gray = roi_gray[int(h / 2) :, :]
                smile_roi_color = roi_color[int(h / 2) :, :]

                smiles = smile_cascade.detectMultiScale(
                    smile_roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25)
                )

                if len(smiles) > 0:
                    cv2.putText(
                        frame,
                        "Smiling :)",
                        (x, y + h + 25),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2,
                    )
                    for sx, sy, sw, sh in smiles:
                        cv2.rectangle(
                            smile_roi_color,
                            (sx, sy),
                            (sx + sw, sy + sh),
                            (0, 255, 255),
                            2,
                        )

        # Display status
        status_y = 30
        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (10, status_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Eyes: {'ON' if detect_eyes else 'OFF'}",
            (10, status_y + 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Smile: {'ON' if detect_smile else 'OFF'}",
            (10, status_y + 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )

        cv2.imshow("Face Detection - Multi-Feature", frame)

        # Keyboard controls
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("e"):
            detect_eyes = not detect_eyes
            print(f"Eye detection: {'ON' if detect_eyes else 'OFF'}")
        elif key == ord("s"):
            detect_smile = not detect_smile
            print(f"Smile detection: {'ON' if detect_smile else 'OFF'}")
finally:
    cap.release()
    cv2.destroyAllWindows()
