number=int(input("Please enter a six-digit number= "))
SecondDigit=(number//10%10)
FifthDigit=(number//10000%10)
sum=SecondDigit+FifthDigit
print(sum)
