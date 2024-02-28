import cv2
your_image = cv2.imread("WhatsApp-Image-2024-02-27-at-6.58.08-PM.jpg", cv2.IMREAD_GRAYSCALE)
your_image_width, your_image_height = your_image.shape[:2]

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def compare_faces(face1, face2):
    return abs(face1[2] - your_image_width) < 30 and abs(face1[3] - your_image_height) < 30

def recognize_face():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        faces = detect_face(frame)

        if len(faces) == 1 and compare_faces(faces[0], your_image):
            recognized_name = "PRIYABRATA"
        else:
            recognized_name = None

        for (x, y, w, h) in faces:
            if recognized_name:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f"Hello, {recognized_name}!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, "Sorry, you are not recognized", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Call the function to start face recognition
recognize_face()
