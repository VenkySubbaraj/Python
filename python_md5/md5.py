import hashlib 
import os
import glob
from datetime import datetime

def timeanddate():
    timeanddate = datetime.now()
    today_date = timeanddate.strftime("%d %B %y %H:%M:%S")
    print(today_date)
    return(today_date)


def algorithm():
    path = os.listdir('./')
    for x in path :
        if ".csv" in x :
            file_path = os.path.abspath(x)
            created_time = os.path.getmtime(file_path)
        #print(created_time)
            date_time = datetime.fromtimestamp(created_time)
        #print(date_time)
            list_of_files = glob.glob(file_path)
            print(list_of_files)
            latest_file = max(list_of_files, key=os.path.getctime)
           # print(latest_file+ "life_style")
            with open(file_path, "rb") as f :
                hash_type = hashlib.md5()
                while temp := f.read(4082):
                    hash_type.update(temp)
                    hash_type_digest = hash_type.hexdigest()
                    file = open("./hashtag.txt", 'a')
                    file.write("{}|{}\n".format(file_path,hash_type_digest))
                    file.close()
                    print(file)
        else :
            print("One file is failed That is apart from csv")

def checking_on_prem_md5():
    on_prem_file = os.path.abspath('./on-prem.txt')
    with open(on_prem_file, "r") as open_file :
        #print(open_file)
        for check in open_file :
            #print(check)
            file_path = os.path.abspath('./hashtag.txt')
            with open(file_path, "r") as hashtag_file :
                #print(hashtag_file)
                for check_hash in hashtag_file :
                    #print(check_hash)
                    if check in check_hash :
                        #print("both the file are same")
                        compare_file = open("./compare_hash", "a")
                        compare_file.write("{}|{}|{}|{}\n".format(check,check_hash,"pass",timeanddate()))





if __name__ == "__main__" :
    algorithm()
    timeanddate()
    checking_on_prem_md5()
 
