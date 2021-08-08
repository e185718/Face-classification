'''FaceEditedフォルダにある画像の２割をテストフォルダに移行するプログラム。
'''
import shutil
import random
import glob
import os
import time
def main(member):
    in_dir = "./FaceEdited/"+member+"/*"
    in_jpg=glob.glob(in_dir)
    img_file_name_list=os.listdir("./FaceEdited/"+member+"/")
    #img_file_name_listをシャッフル、そのうち2割をtestフォルダに入れる。
    random.shuffle(in_jpg)
    os.makedirs('./Test/' + member, exist_ok=True)
    for t in range(len(in_jpg)//5):
        shutil.move(str(in_jpg[t]), "./Test/"+member)

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
 
