#write a program to find wether a number is prime or not?
num = int(input("Enter a number: "))#10
if num>1:
    i=2
    while 1<num:
        if num%1==0:
            i+=1
            print(f"{num} it is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
            break
    else:
        print("enter a valid number")