'''モデルの重みを読み込み、画像を識別テストするプログラム。
learning.pyで学習させたモデルの重みを読み込んでtest_sampleの中のfaceフォルダの中の画像を識別する。
'''
import os
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Activation, Dropout, Flatten, Dense
from tensorflow.keras import optimizers
import numpy as np
import time
from tensorflow.keras.utils import to_categorical

#事前に設定するパラメータ
members = ["松本潤","二宮和也","相葉雅紀","櫻井翔","大野智"]
nb_members = len(members)
img_width, img_height = 150, 150#画像の大きさ
#重みを保存したモデルと同様のモデルを定義する。

# VGG16のロード。
input_tensor = Input(shape=(img_width, img_height, 3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)
# FC層の作成。
top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_members, activation='softmax'))
# VGG16とFC層を結合してモデルを作成。
vgg_model = Model(inputs=vgg16.inputs, outputs=top_model(vgg16.outputs))

from tensorflow.keras.models import load_model
#定義したモデルに重みを読み込ませる。
vgg_model.load_weights('./results/Weight.h5')

from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
def img_predict(filename):
	'''画像を読み込んで予測する。
    Argments:
        filename(str): atest_sampleの中のfaceファイルにある画像データの名称。
    Returns:
        なし。
    '''
	img = image.load_img(filename, target_size=(img_height, img_width))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
    # 学習時にImageDataGeneratorのrescaleで正規化したので同じ処理が必要。
	x = x / 255.0
    #画像の表示。
	plt.imshow(img)
	plt.show()
    # 指数表記を禁止にする。
	np.set_printoptions(suppress=True)
    #画像の人物を予測。
	pred = vgg_model.predict(x)[0]
    #結果を表示する。
	print("'松本潤': 0, '二宮和也': 1, '相葉雅紀': 2, '櫻井翔': 3, '大野智': 4")
	print(pred*100)
    
import cv2, os, re,requests, time, bs4
import glob
test = glob.glob('./test_sample/face/*')
#test_sampleの中のfaceフォルダの中の画像を識別する。
for index, file in enumerate(test,1):
	print(type(file))
	img_predict(file)
	
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)