import hashlib 
def algorithm():
    with open("./test.csv", "rb") as f :
        hash_type = hashlib.md5()
        while temp := f.read(4082):
            hash_type.update(temp)
            hash_type_digest = hash_type.hexdigest()
            #print(hash_type_digest)
    return(hash_type_digest)

def writeline():
    file = open("./hashtag.txt", "w")
    file.write(algorithm())
    file.close()
    print(file)

if __name__ == "__main__" :
    print("INN")
    print(algorithm())
    writeline()
