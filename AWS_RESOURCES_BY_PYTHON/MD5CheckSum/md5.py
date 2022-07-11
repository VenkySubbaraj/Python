import hashlib 
import os
import glob
from datetime import datetime

def timeanddate():
    timeanddate = datetime.now()
    today_date = timeanddate.strftime("%d %B %y %H:%M:%S")
    print(today_date)


def algorithm():
    path = os.listdir('./')
    for x in path :
        if ".csv" in x :
            file_path = os.path.abspath(x)
            created_time = os.path.getmtime(file_path)
            date_time = datetime.fromtimestamp(created_time)
            list_of_files = glob.glob(file_path)
            latest_file = max(list_of_files, key=os.path.getctime)
            with open(file_path, "rb") as f :
                hash_type = hashlib.md5()
                while temp := f.read(4082):
                    hash_type.update(temp)
                    hash_type_digest = hash_type.hexdigest()
                    file = open("./hashtag.txt", 'a')
                    file.write("{}|{}|{}\n".format(file_path,hash_type_digest,date_time))
                    file.close()
                    print(file)
        else :
            print("One file is failed That is apart from csv")

if __name__ == "__main__" :
    algorithm()
    timeanddate()
 
