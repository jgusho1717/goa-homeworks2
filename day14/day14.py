# 3) შექმენით პროგრამა სადაც 0 დან 50 ის ჩათვლით ყველა 5 ის ჯერად რიცხვებს შეკრიბავთ (5ზე რომელი რიცხვებიც იყოფა) გამოიყენეთ fro ციკლიც და while ციკლიც

# num1 = 0
# for i in range(0, 50+1):
#     if i % 5==0:
#         num1 +=5
# print(num1 )


# for ციკლები

# for i in range(5):
#     print("GOA")

# result = 0
# for i in range(2):
#     print("rezi")
#     print("GOA")
#     result = result + i

# for i in range(0,50 + 1):
#     print(i)

# num = int(input("please enter your age "))
# for i in range(num + 15 + 1):
#     print(i)

# while ციკლები

# i = 1
# while i < 10:
#     print(i)


# i = 5
# while i > 4:
#     print("GOA")

# i = 30
# while i< 40:
#     print(i)
#     i = i + 1


# i = 60
# while i < 70:
#     print(i)
#     i = i % 1

# i = 100
# while i > 50:
#     print(i)
#     i = 1 / 1


# num1 = 0
# num2 = 5
# while  50 > num1:
#     print(num1 + num2)
#     if num1 % num2==0:
#         num1  +=5


result = 0
i = 0

while i <= 50:
    result += i
    i = i + 5

    print(result)