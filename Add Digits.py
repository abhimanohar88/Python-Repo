def add_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Input
num = int(input())
# Output
print(add_digits(num))
