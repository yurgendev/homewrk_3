# homework 3
# task 1
# Write a Python program to print the number entered by user only if the number entered is negative.


text = int(input("Enter negative number: "))
if text >= 0:
    print("Must be negative numbers, sir")
elif text < 0:
    print("Yes, number is negative and its: ", text)

# task 2
# Write a Python program to check if the value a is less than 20 or not.

text_for_check20 = int(input("Numbers checking: "))
if text_for_check20 < 20:
    print("Number less than 20!")
elif text_for_check20 > 20:
    print("Number more than 20")

# task 3
# Write a Python program to check if a given number is Zero or Not.


numcheck = int(input("Enter numbers: "))
if numcheck < 0:
    print("Less than zero")
elif numcheck > 0:
    print("More than zero")
else:
    numcheck == 0
    print("Zero is zero, dude")

#task 4 check if number even or odd

check1 = int(input("?: "))
if check1 % 2 == 0:
    print("odd")
else:
    print("even")

# task 5  Write a Python program to find largest number among three numbers
# entered by user.

a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))

if a > b and a > c:
    print("a is largest number")
elif b > a and b > c:
    print("b is largest number")
else:
    c > a and c > b
    print("c is largest one")

