# Question 1: Count Vowels

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels("hello world"))        


# Question 2: Reverse a string

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("hello"))  
print(reverse_string("A man a plan a canal Panama"))


# Question 3: Filter even numbers

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
    

print(filter_even_numbers([1, 2, 3, 4, 5]))