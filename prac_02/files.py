# Question 1
out_file = open("name.txt", "w")
name = input("Please enter your name: ")
out_file.write(name)
out_file.close()

# Question 2
out_file = open("name.txt", "r")
print("Your name is {}".format(out_file.read()))
out_file.close()

# Question 3
out_file = open("numbers.txt", "r")
number1 = int(out_file.readline())
number2 = int(out_file.readline())
ans = number1 + number2
print(ans)
out_file.close()

# Question 4
total = 0
out_file = open("numbers.txt", "r")
for line in out_file:
    number = int(line)
    total += number
print(total)
out_file.close()
