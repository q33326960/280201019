x = input("enter the numbers with a space between them") 
numbers = x.split()
print(numbers)
even = 0
for i in numbers:
    if int(i) % 2 !=0:
        even = even + 1
print(even / len(numbers) * 100)
