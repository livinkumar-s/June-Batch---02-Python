# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# a=int(input("Enter your Number: "))
# print(a+100)
# print(a-100)

# age=int(input("Enter Your Age: "))
# if age>=18:
#     print("Can Vote")
# else:
#     print("Cannot Vote")

# print(6)

# a=10

# if a<10:
#     print("Step1")
#     print("Step2")
#     print("Step3")
# else:
#     print("From else block...!")

# print("Step Last")

# a=10

# if a<10:
#     print("From IF Block...!")
# elif a<10:
#     print("From Elif1 Block")
# elif a>10:
#     print("From Elif2 Block")
# else:
#     print("From else Block...!")

# marks = int(input("Enter your marks: "))
 
# if marks >= 90 and marks <= 100:
#     print("Grade: O")
# elif marks >= 80 and marks <= 89:
#     print("Grade: A+")
# elif marks >= 70 and marks <= 79:
#     print("Grade: A")
# elif marks >= 60 and marks <= 69:
#     print("Grade: B")
# elif marks >= 50 and marks <= 59:
#     print("Grade: C")
# elif marks >= 0 and marks <= 49:
#     print("Grade: Fail")
# else:
#     print("Invalid Marks")

# num=int(input("Enter your Number: "))

# if num>10:
#     if num>15:
#         print("Very Large...!")
#     else:
#         print("Large")
# else:
#     if num<5:
#         print("Very Small")
#     else:
#         print("Small")

# Loop 

# i=0

# while i>5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("-------------------")
#     i-=1

# no of iteration --> 0
#i -->0,1,2,3,4,5

# str1="Dhonihello"

# print(str1[-4])

# print(list(range(3,30,3)))

# for x in range(10,20,2):
#     print(x)
#     print("-------------------")


# No of Iteration --> 

# 1-100
# 100-1

# for i in range(100, 0, -1):
#     print(i)

# Break 

# i=1

# while i<=100:
#     if i<=50:
#         break
#     print(i)
#     i+=1

# no of iteration --> 51

# for i in range(1,101):
#     print(i)
#     print("--------------")
#     if i>50:
#         continue

# No of Iteration--> 100

secret=33
notFound=True

while notFound:
    inp=int(input("Enter the number: "))
    if secret==inp:
        print("You won..!")
        notFound=False
    else:
        print("Try again..!")