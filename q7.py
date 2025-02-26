import random

# generates a list of 10 random numbers between 1 and 100.
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# loops all of list to modify the numbers.
for index in range(len(random_numbers)):
    number = random_numbers[index]

    # if the number is greater than 80, it becomes negative
    if number > 80:
        random_numbers[index] = -number
    # but if the number is lower than 40, the sums of its digits are printed
    elif number < 40:
        # convert the number to a string so we can iterate over each digit
        sum_digits = 0
        for digit in str(number):
            # converts the digit back to an integer and add it to sum_digits.
            sum_digits += int(digit)
        random_numbers[index] = sum_digits

# Print the modified list.
print(random_numbers)


