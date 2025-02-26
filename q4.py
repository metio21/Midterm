def palindrome():
    word = input("Enter a string to check if it's a palindrome: ").strip()
    if word == word[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

# Call the function
palindrome()


