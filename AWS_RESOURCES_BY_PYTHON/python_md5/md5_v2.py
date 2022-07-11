import hashlib
import os
import glob
from datetime import datetime
import boto3

def bucket_download():
    bucketres = boto3.resource(s3)

def timeanddate():
    timeanddate = datetime.now()
    today_date = timeanddate.strftime("%d %B %y %H:%M:%S")
    print(today_date)
    return(today_date)


def algorithm():
    path = os.listdir('./dockercontainer')
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
                    file = open("./dockercontainer/hashtag.txt", 'a')
                    file.write("{}|{}\n".format(file_path,hash_type_digest))
                    file.close()
                    print(file)
        else :
            print("One file is failed That is apart from csv")

def checking_on_prem_md5():
    on_prem_file = os.path.abspath('./dockercontainer/on-prem.txt')
    with open(on_prem_file, "r") as open_file :
        #print(open_file)
        for check in open_file :
            #print(check)
            file_path = os.path.abspath('./dockercontainer/hashtag.txt')
            with open(file_path, "r") as hashtag_file :
                #print(hashtag_file)
                for check_hash in hashtag_file :
                    #print(check_hash)
                    if check in check_hash :
                        #print("both the file are same")
                        compare_file = open("./dockercontainer/compare_hash", "a")
                        compare_file.write("{}|{}|{}|{}\n".format(check,check_hash,"pass",timeanddate()))
                    else :
                        compare_file.write("{}|{}|{}|{}\n".format(check,check_hash,"fail",timeanddate()))

s3_client = boto3.client('s3')

bucket = "dockercontainer1"
local = '/home/ubuntu/dockercontainer'
print(local)
client = s3_client

def download_dir():
    """
    params:
    - prefix: pattern to match in s3
    - local: local path to folder in which to place files
    - bucket: s3 bucket with target contents
    - client: initialized s3 client object
    """
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket':bucket
    }

    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        client.download_file(bucket, k, dest_pathname)





if __name__ == "__main__" :
    algorithm()
    timeanddate()
    checking_on_prem_md5()
    download_dir()
