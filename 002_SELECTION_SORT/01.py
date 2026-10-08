numbers = [10, 5, 8, 2, 1, 3]
n = len(numbers)
for i in range(n-1):
    minindex = i
    for j in range(i+1, n):
        if numbers[j] < numbers[minindex]:
            minindex = j
    numbers[i], numbers[minindex] = numbers[minindex], numbers[i]
print(numbers)            
