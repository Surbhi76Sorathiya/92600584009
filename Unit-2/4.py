num=int(input("Enter a digits : "))
sum1=0

while num>0:
    sum1 +=num%10 #extract last digit
    num//=10 #remove last digit
print("The sum of digits : ",sum1)
