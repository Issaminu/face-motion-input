import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key

# Initialize the keyboard controller
keyboard = Controller()

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define thresholds for face detection confidence and head positions
face_detection_threshold = 0.5  # Adjust this threshold as needed
lean_threshold = 40
head_lower_threshold = 80  # Adjust this threshold for detecting the head moving lower

# Initialize state variables
is_face_leaning_left = False
is_face_leaning_right = False
is_head_lowered = False

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Face Detection
    results = face_detection.process(rgb_frame)

    # Extract face detection data
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

            # Calculate the center of the detected face
            center_x = x + w / 2
            frame_center = iw / 2

            # Calculate the height of the face
            face_height = y + h

            # Update state variables based on head movements
            if center_x < frame_center - lean_threshold:
                is_face_leaning_left = True
                is_face_leaning_right = False
            elif center_x > frame_center + lean_threshold:
                is_face_leaning_left = False
                is_face_leaning_right = True
            else:
                is_face_leaning_left = False
                is_face_leaning_right = False

            if face_height > ih - head_lower_threshold:
                is_head_lowered = True
            else:
                is_head_lowered = False

    else:
        # No face detected, reset all state variables
        is_face_leaning_left = False
        is_face_leaning_right = False
        is_head_lowered = False

    # Simulate keypresses based on the state variables
    if is_face_leaning_left:
        keyboard.press('d')
        print("Left")
    else:
        keyboard.release('d')

    if is_face_leaning_right:
        keyboard.press('a')
        print("Right")
    else:
        keyboard.release('a')

    if is_head_lowered:
        keyboard.press(Key.space)
        print("Space")
    else:
        keyboard.release(Key.space)

    # Display the frame
    cv2.imshow('Face Detection and Tracking', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
