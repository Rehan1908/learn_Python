n = int(input("Enter a Positive Integer: "))


factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")
