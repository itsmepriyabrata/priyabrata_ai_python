import cv2

class FaceRecognition:
    def __init__(self, image_path, name):
        self.image_path = image_path
        self.name = name
    
    def recognize_face(self):
        # Load the pre-trained face detection model
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Load your image for recognition
        image = cv2.imread("C:\\Users\\priyabrata\\Desktop\\scrapping\\myvenv\\priyabrata.jpeg")
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Loop through each detected face
        for (x, y, w, h) in faces:
            # Recognize the face using your face recognition model
            # Here, you would typically compare the detected face with a database of known faces
            # For simplicity, let's assume the detected face matches your face
            recognized_name = self.name
            
            # If the recognized name is your name, say your name
            if recognized_name == self.name:
                print("Hello, " + self.name)
            else:
                print("Sorry, you are not recognized.")
                
            # Draw a rectangle around the face
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the image with detected faces
        cv2.imshow('Face Recognition', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    recognizer = FaceRecognition("priyabrata.jpeg ", "Priyabrata")
    recognizer.recognize_face()
