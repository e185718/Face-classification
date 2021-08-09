"""画像の水増しを行うプログラムである、inflated.pyを並列処理する。

作成者  185725J
"""
import time
from pathlib import Path
import cv2
import subprocess
IMAGE_PATH = "./arashi_image"

import glob
def main():
    img_dir = "./arashi_image/"
    members = ["二宮和也","櫻井翔","相葉雅紀","大野智","松本潤"]
	
    files = glob.glob(IMAGE_PATH+"/*")
    #print(files)
    
    #files = Path(IMAGE_PATH + "/").glob("*")
    procs = []
    N = 5  #メモリ不足にならないようにNを適切に設定する必要がある
    #print(files)
    for member in members:
        
        proc = subprocess.Popen(["python3", "inflated.py",member])
        procs.append(proc)

        if len(procs) == N:
            # メモリ不足で実行に失敗するので、
            # 子プロセスの数がNになったら、一旦全ての子プロセスの終了を待つ
            for proc in procs:
                proc.communicate()
            procs.clear()
    for proc in procs:
        proc.communicate()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Finished in {} seconds.".format(end-start))