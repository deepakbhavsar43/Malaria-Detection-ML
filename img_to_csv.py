import glob
import os, cv2
from PIL import Image

basepath = "cell_images"
label = "Parasitized"
dirlist = glob.glob("cell_images/" + label + "/*.png")
file, im = None, None
try:
    file = open("csv/dataset.csv", "a+")
except:
    os.mkdir('csv')

dir = os.walk(basepath + '\\' + label)

for img_path in dirlist:
    # print(img_path)
    im = cv2.imread(img_path)
    im = cv2.GaussianBlur(im, (5, 5), 2)

    img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, 1, 2)
    # To draw contours
    # for contour in contours:
    #     cv2.drawContours(im, contour, -1, (90, 166, 55), 3)
    file.write(label)
    file.write(",")

    for i in range(5):
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")

        file.write(",")

    file.write("\n")
