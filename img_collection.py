'''arashi_imageファイルにある画像をOpenCVで顔を検出し、切り出すプログラム。
顔の検出にはOpenCVのデフォルトの分類器(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)を使用する。
'''
import cv2, os, re,requests, time, bs4
from urllib.request import urlretrieve
from urllib import request as req
from urllib import error,parse
from PIL import Image
import numpy as np
import glob
import sys
def main(member):
    img_dir = "./arashi_image/"
    cascade_file = "./haarcascade_frontalface_alt.xml"#OpenCVのデフォルトの分類器のpath
    cascade = cv2.CascadeClassifier(cascade_file)

    files = glob.glob(img_dir+member+"/*.jpg")
    print("{}の写真は{}枚です。顔認識を始めます。".format(member, len(files)))
    for index, file in enumerate(files,1):
        img = cv2.imread(file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #minSizeを5の倍数で5から100まで変更して検出することで、顔の検出率を高める。
        for i in range(1,20):
            minValue = i * 5
            facerect = cascade.detectMultiScale(img_gray, minSize=(minValue,minValue))
            if len(facerect) == 1:
                break
        if len(facerect) != 1:
                continue
        for x,y,w,h in facerect:
            img = img[y:y+h, x:x+w]
        face_path = img_dir+member+"/face"
        if not os.path.exists(face_path):
            os.makedirs(face_path)
        cv2.imwrite(face_path  + "/" + str(index)+".jpg", img)
        
if __name__ == "__main__":
    """
    _,member = sys.argv
    main(member)
    """
    member = ["二宮和也","櫻井翔","相葉雅紀","大野智","松本潤"]
    start = time.time()
    for i in range(5):
        main(member[i])
    end = time.time()
    print("Finished in {} seconds.".format(end-start))