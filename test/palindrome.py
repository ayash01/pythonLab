def palindrome(str):
    if str[0:] == str[::-1]:
        return True

str1 = input("Enter a string: ")

if(palindrome(str1)):
    print(str1, 'is a palindrome')
else:
    print(str1, 'is not a palindrome')

    