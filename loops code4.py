start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))


print("Even numbers:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd numbers:")

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")