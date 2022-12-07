i = ''
n = 100
for i in range(n):
    print(i)
    if ((i%3==0) & (i%5==0)):
        print("Number is divisible by both the values so it is BLACKRED combination")
    elif (i%3==0):
        print("Number is divisible by 3, so it is BLACK")
    elif (i%5==0):
        print("Number is divisible by 5, so it is RED")
    
