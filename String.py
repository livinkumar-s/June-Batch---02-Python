# print("Hi"*7)

# a="Hello"
# print(id(a))
# a+="123" # new String "Hello"+"123"
# print(id(a))
# print(a)

# print(id(66))

# l1=[1,2,3]
# print(id(l1))
# l1.append(77)
# print(id(l1))

# a="hello World"
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.capitalize())

# a="        hello world       "
# print("."+a.strip()+".")
# print("."+a.lstrip()+".")
# print("."+a.rstrip()+".")

# a="Hello guys I would love to play football"
# print(a.split("s"))

# a=("Hello","world","...!")
# print("---".join(a))

# a="Hello world"
# print(a.find("wo"))
# print(a.count("he"))

# str1="Keep Going...!"
# print(str1.startswith("Ke"))
# print(str1.endswith("!."))

# a="wrgwergw 23134134134"
# print(a.isalpha())
# print(a.isdigit())
# print(a.isalnum())

# name="Leo"
# age=44

# His name is Leo. He is 44.

# print("His name is "+name+". He is "+str(age))
# print(f"His name is {name}. He is {age}.")

# str1="Hello\tworld"
# str1="Hello\nworld"
# print(str1)

# I'm Lee. I said "Hello"

# str1='I\'m Lee. I said "Hello"'

# str1='''Hello
# Hi
# world'''

# print(str1)


# for i in range(5):
#     print("From outer Loops...!")
#     for j in range(5):
#         print("From inner loop..!")

# i=0,1,2,3,4

# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==5 or j==1:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

# i = 1,2,3,4,5
# 1,1

for i in range(3):
    for j in range(3):
        for k in range(3):
            print("Hi")