import cv2
import glob
import random
import imutils
import numpy as np

emotions = ["angry", "happy", "sad", "neutral"]
fishface = cv2.face.FisherFaceRecognizer_create()
data = {}

def get_files(emotion):
    files = glob.glob("dataset\\%s\\*" %emotion)
    random.shuffle(files)
    training = files[:int(len(files))]
    return training

def make_sets():
    training_data = []
    training_labels = []
    for emotion in emotions:
        training = get_files(emotion)
        for item in training:
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = imutils.resize(gray, width=200, height=200)
            training_data.append(gray)
            training_labels.append(emotions.index(emotion))

    return training_data, training_labels

def run_recognizer():
    training_data, training_labels = make_sets()
    print("Training Fisher Face Classifier..")
    print("Size of training set is:", len(training_labels), "images")
    fishface.train(training_data, np.asarray(training_labels))
    fishface.save('Model/model.cv2')