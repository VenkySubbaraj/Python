import hashlib

def md5():
with open("./test.csv", "rb") as f :
    hash_type = hashlib.md5()
    while temp := f.read(8192):
        hash_type.update(temp)

#print(hash_type.digest())
print(hash_type.hexdigest())

if "__name__" = "__main__":
    md5():
