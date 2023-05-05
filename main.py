import cv2
import mediapipe as mp

# inicializar opencv e mediapipe
webcam = cv2.VideoCapture(0)
face_detection = mp.solutions.face_detection
face_recognition = face_detection.FaceDetection()
drawing = mp.solutions.drawing_utils

while True:
    # capturar frame da webcam
    checker, frame = webcam.read()

    if not checker:
        break

    # armazenar todos os rostos capturados no frame
    face_list = face_recognition.process(frame)

    if face_list.detections:
        for face in face_list.detections:
            drawing.draw_detection(frame, face)

    cv2.imshow("Rotos detectados na webcam", frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
