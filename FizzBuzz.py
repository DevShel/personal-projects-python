num = 0
num = 0

while (num<16):
    num = num+ 1
    if (num%3 ==  0):
        if (num%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
        
    elif (num%5 == 0):
        print("Buzz")
    else:
        print(num)
    
    
