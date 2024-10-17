num = 30
fibonacci = [1,1]

while len(fibonacci) < num:
    next_number = sum(fibonacci[-2:])
    fibonacci.append(next_number)

print(fibonacci)