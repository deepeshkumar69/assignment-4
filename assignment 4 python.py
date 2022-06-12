#Question 1
a=int(input("Enter your marks:"))
if 0<=a<25:
    print("Your corresponding grade='F'")
elif 25<=a<45:
    print("Your corresponding grade='E'")
elif 45<=a<50:
    print("Your corresponding grade='D'")
elif 50<=a<60:
    print("Your corresponding grade='C'")
elif 60<=a<80:
    print("Your corresponding grade='B'")
elif 80<=a<100:
    print("Your corresponding grade='A'")
else :
    print("Enter your marks between 0-100")
          
#Question 2

y=int(input("\nEnter year to know it is leap year or not:"))
if y%4==0 or y%400==0:
    print("Entered year is a leap year")
elif y%100==0 and y%4==0:
    print("Entered year is not a leap year")
else :
    print("Entered year is not a leap year")


#Question 3

n=1
while 10>=n>0 :
    import random
    a1=(random.randint(1,9))
    a2=(random.randint(1,9))

    
    print("Question""(",n,"):",a1,"x",a2)
    ans=int(input("Your answer is="))
    n+=1
    
    
    if ans==a1*a2:
        
        
        print("Right!")
        
    else :
        print("Wrong! \n Correct answer is=",a1*a2)

#Question 4
        
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")
    
