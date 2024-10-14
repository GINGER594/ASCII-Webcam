import cv2, os
from PIL import Image

#list of ascii chars
chars = ["@", "#", "$", "%", "&", "8", "*", "o", "0", "+", "=", "-", ":", ";", ",", ".", " "]

def DisplayFrame(asciilist):
    #displaying frame (for best experience, ctrl- to zoom out)
    os.system("cls")
    print("-" * (len(asciilist[0]) * 2 - 1))
    for row in asciilist:
        print(" ".join(row))
    print("-" * (len(asciilist[0]) * 2 - 1))
    print(f"\nWidth: {len(asciilist[0])} Height: {len(asciilist)}")

def processFrame(frame):
    asciilist = []
    #looping through each pixel
    for y in range(frame.height):
        row = ["|"]
        for x in range(frame.width):
            #getting an avg rgb value and inverting it
            avg = 255 - (frame.getpixel((x, y))[0] + frame.getpixel((x, y))[1] + frame.getpixel((x, y))[2]) // 3
            index = int((avg / 255) * (len(chars) - 1))
            row.append(chars[index])
        row.append("|")
        asciilist.append(row)
    return asciilist

def captureVideo():
    #start recording
    cap = cv2.VideoCapture(0)
    while True:
        #capturing each frame
        frame = cap.read()[1] #cap.read returns 2 items, a boolean status and a frame
        #converting frame to a pillow img
        frame = Image.fromarray(frame)
        #scaling frame
        height = 100
        width = int(frame.width * (height / frame.height) * 1.8)
        frame = frame.resize((width, height))

        #processing and displaying frame
        asciilist = processFrame(frame)
        DisplayFrame(asciilist)

captureVideo()