import random
import math

def generateOtp():
    digit = "0123456789ASDFGHJKLQWERTYUIOPMZXNCVBasdfghjklqwertyuiopzxcvbnm"
    OTP = ""
    length = len(digit)
    for i in range(10):
        OTP = OTP + digit[math.floor(random.random()*length)]
    return OTP

if __name__ == "__main__":
    print(generateOtp())
    
