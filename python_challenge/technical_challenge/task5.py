# Write a python program that checks if a string is a palindrome.
# Then optionally write a unit test to check your program's correctness
# PS: A palindrome Python program is used to check whether a string is the same from forward to backward.

a_string = 'Was it a car or a cat I saw'

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    return a_string == a_string[::-1]

print(palindrome(a_string))