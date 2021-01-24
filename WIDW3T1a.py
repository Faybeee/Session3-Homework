#Write a program that allows you to enter 4 numbers
#and stores them in a file called “Numbers”
#3,45,83,21
#Have a go at ‘w’ ‘r’ ‘a’

print("Hi, please enter the numbers 3, 45, 83 and 21 when prompted.")
num1 = int(input("Please enter 3?"))
num2 = int(input("Please enter 45?"))
num3 = int(input("Please enter 83?"))
num4 = int(input("Please enter 21?"))

my_file = open("numbers.txt", "w")
my_file.write(str(num1) +"\n")
my_file.write(str(num2) +"\n")
my_file.write(str(num3) +"\n")
my_file.write(str(num4) +"\n")
my_file.close()


