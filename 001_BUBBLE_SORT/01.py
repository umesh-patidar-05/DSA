numbers = [1,9,7,2,3,4,5]
n = len(numbers)
for i in range(n-1):
    swap = False
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1], numbers[j]
            swap = True
    if not swap:
        break
print(numbers)            