numbers = [10,25,8,0,7,63,100,92,98,13]

largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num

print("Largest number in List is {}".format(largest))
