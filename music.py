import os, random, time, sys

def play_music(emotion):
    mp3s = []
    mediapath = "Music\\" + emotion + '\\'

    for path, directory, element in os.walk(mediapath, False):
        print("Loading music from" + path + "...")
        tmparray = element

        for i in range(0, len(tmparray) - 1):
            if (tmparray[i][-3:] == "mp3" and tmparray[i][:1] != "."):
                mp3s.append(tmparray[i])
            else:
                print("Unuseable:", tmparray[i])

        print("Loaded" + str(len(mp3s)) + "files, of" + str(len(element)) + "total")

    random.shuffle(mp3s)

    for i in range(0, len(tmparray) - 1):
        print(mediapath + mp3s[i])
        os.system(mediapath + mp3s[i])
        time.sleep(1)
