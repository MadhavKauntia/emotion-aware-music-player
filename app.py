import cv2
import imutils
import train
import argparse
import sys
import music

emotions = ["angry", "happy", "sad", "neutral"]

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', help="Train the model again", type=bool, default=True, required=False, nargs='?')
args = parser.parse_args()

video_capture = cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier("XML/haarcascade_frontalface_default.xml")
fishface = cv2.face.FisherFaceRecognizer_create()

def crop_face(gray, face):
    for (x, y, w, h) in face:
        faceslice = gray[y:y+h, x:x+w]
        faceslice = imutils.resize(faceslice, width=200, height=200)
    return faceslice

if args.update == True and len(sys.argv) > 1:
    print('Update')
    train.run_recognizer()
else:
    face_list = []
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        clahe_image = clahe.apply(gray)
        face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
        if len(face) == 1:
            faceslice = crop_face(gray, face)
            face_list.append(faceslice)
            if len(face_list) == 10:
                break

    fishface.read('Model/model.cv2')
    emotion_list = []
    max = 0
    correct_emotion = 0
    for face in face_list:
        emotion, confidence = fishface.predict(face)
        if confidence > max:
            correct_emotion = emotion
            max = confidence

    music.play_music(emotions[correct_emotion])