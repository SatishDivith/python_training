def palindrome(num): 
    return str(num) == str(num)[::-1]

num=int(input("Enter palindrome number"))
if palindrome(num):
    print("number is palindrome",num)
else:
    print("number is not palindrome",num)