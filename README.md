# Name
顔分類システム

# 概要
嵐のメンバー5人の顔全体や顔のパーツごとのデータセットを作成し、学習する。
それによって、どのくらいの割合で似ているかを判別する。

前処理に関して並列処理を行い、さらに速い処理を目指した。

# テストデータ
私達が用いたデータは著作権的に問題視されかねないため載せておらず、動作確認ができるように公開許可をもらった画像をデータセットとして公開しています。

# 使用方法

## 学習までの流れ
１．icrawlerによる画像の収集(大野智の画像を200枚集める場合)
```
from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "大野智"})
crawler.crawl(keyword="大野智", max_num=200)
```

２．OpenCVを利用して顔部分を抽出し、抜き出す
```
$ python main_img_collection.py

```

３．画像の水増し
```
$ python main_inflated.py

```
４．FaceEditedフォルダにある画像の２割をテストフォルダに移行する
```
$ python main_img_split.py

```

５．(２．)で作成したdatasetを元に学習させる．結果はグラフと正解率を表示．
```
$ python learning.py
```

６．用意しておいてオリジナルの写真で顔判別を行う
```
$ python predict.py
```
# ファイルの説明

## main_img_collection.py：画像の顔の部分だけを抽出する
+  入手した画像をカスケード分類器で顔の部分を抽出するプログラム。img_collection.pyを並列的に処理する。

## main_inflated.py：画像の水増しを行う
+ 学習画像を垂直方向への反転、90度回転、270度回転、グレー化、ヒストグラムの変更を行うことで画像の水増しを実行するプログラム。inflated.pyを並列的に処理する。

##main_img_split.py：画像の分割を行う
FaceEditedフォルダにある画像の２割をテストフォルダに移行するプログラム。img_split.pyを並列的に行う。

## learning.py：datasetの学習を行う
+ datasetを元に、kerasでモデルを構築し、VGG16をFine-tuningしてモデルの学習を行う。
+ 結果はグラフと正解率を表示．

## predict.py：顔判別を行う
+ 用意しておいた写真の人物と学習した顔で認証を行う
+ 結果出力では切り取られた顔写真と,それぞれのメンバー(松本潤,二宮和也,相葉雅紀,櫻井翔,大野智)に似ているかを数値で表す。


# 動作環境
+ Python 3.6.4
+ tensorflow 2.0.0

##作成情報

#開発メンバー
+ 185718F 喜瀬大地 
+ 185725J 識名俊樹


#所属
+ 琉球大学 工学部 工学科 知能情報コース

# 連絡先
+ e185718@ie.u-ryukyu.ac.jp
+ e185725@ie.u-ryukyu.ac.jp
