# -*- coding: utf-8 -*-
"""Python Practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qtkbVbB1DRkuwnl0c_buIUk_088SKRSM
"""

#Print every character of a string entered by the user in a new line using a loop
str=input("Enter a string: ")
for i in str:
    print(i)

#Length of the string "machine learning" with and without using len function
str="machine learning"
count=0
for i in str:
    count+=1
print("Length of the string is: ",count)

#check if the word 'orange' is present in the "This is orange juice"
str="This is orange juice"
if "orange" in str:
    print("orange is present")
else:
    print("orange is not present")

#Find the number of vowels, consonants, digits, and white space characters in a string
def count_character(text):
  vowels = 0
  consonants = 0
  digits = 0
  spaces = 0

  for char in text:
    if char in 'aeiouAEIOU':
      vowels += 1
    elif char.isalpha():
      consonants += 1
    elif char.isdigit():
      digits += 1
    elif char.isspace():
      spaces += 1

#Count Uppercase, Lowercase, special character and numeric values in a given string
def count_character(text):
  upper = 0
  lower = 0
  special = 0
  numeric = 0

  for char in text:
    if char.isupper():
      upper += 1
    elif char.islower():
      lower += 1
    elif char.isdigit():
      numeric += 1
    else:
      special += 1
  return upper, lower, special, numeric

#Make a new string with all consonants deleted from string "Hello, have a good day"
def remove_consonants(text):
  vovels = 'aeiouAEIOU'
  new_string = ''

  for char in text:
    if char in vovels:
      new_text += char
  return new_string

#Remove the nth index character from a non-empty string
def remove_nth_character(text, n):
    new_string = text[:n] + text[n+1:]
    return new_string

#Change a given string to a new string where first and last characters have been exchanged
def swap_first_last(text):
  if len(text) <= 1:
    return text
  else:
    return text[-1] + text[1:-1] + text[0]

#Count the occurrences of each word in a given sentence
def word_count(sentence):
  words = sentence.split()
  word_count = {}

  for word in words:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  return word_count

#Count the occurrence of a given character in a string
def count_character(text, char):
    return text.count(char)

# Example usage:
result = count_character("Hello, world!", 'o')
print(result)

# Find last 10 characters of a string
def last_10_characters(text):
  return text[-10:]

#convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
def uppercase(text):
  count = 0
  for char in text[:4]:
    if char.isupper():
      count += 1
  if count >= 2:
    return text.upper()
  else:
    return text

# Remove a newline in Python
str1='hello\n'
print(str1)
print(str1.rstrip())

#Python program to swap commas and dots in a string
#Sample string: "32.054,23"
#Expected Output: "32,054.23"

def swap_commas_dots(text):
    # Replace commas with a temporary placeholder
    temp_text = text.replace(',', '#')
    # Replace dots with commas
    temp_text = temp_text.replace('.', ',')
    # Replace the temporary placeholder with dots
    swapped_text = temp_text.replace('#', '.')
    return swapped_text

# Find the first repeated character in a given string
def first_repeated_character(text):
  for char in text:
    if text.count(char) > 1:
      return char
  return None

# Find the 2 most repeated word in a given string
from collections import Counter

def repeated_word(text):
    words = text.lower().split()

    word_counts = Counter(words)

    most_common = word_counts.most_common()

    if len(most_common) < 2:
        return None
    return most_common[1][0]

# Count Even and Odd numbers in a string
def count_even_odd(text):
  even_count = 0
  odd_count = 0
  for char in text:
    if char.isdigit():
      num = int(char)
      if num % 2 == 0:
        even_count += 1
      else:
        odd_count += 1
  return even_count, odd_count

# Check if a string contains only digits
def contains_only_digits(text):
  return text.isdigit()

# Remove a given character/word from String
def remove_word(text, word):
    # Replace the given word with an empty string
    return text.replace(word, '')

# Remove the characters which have odd index values of a given string
def remove_odd_index(text):
  return text[::2]

# Reverses a string if its length is a multiple of 5
def reverse_string(text):
  if len(text) % 5 == 0:
    return text[::-1]
  else:
    return text

# Format a number with a percentage(0.05 >> 5%)
def format_percentage(number):
  return "{:.0%}".format(number)

# Reverse words in a string
def reverse_words(text):
  words = text.split()
  reversed_words = words[::-1]
  return ' '.join(reversed_words)

# Swap cases of a given string
def swap_cases(text):
  return text.swapcase()

# Remove spaces from a given string
def remove_spaces(text):
  return text.replace(' ', '')

# Remove duplicate characters of a given string
def remove_duplicates(text):
  result = ''
  for char in text:
    if char not in result:
      result += char
  return result

# Find the area of a circle
import math

def area_of_circle(radius):
  return math.pi * radius ** 2

#  Sum of squares of first n natural numbers
def sum_of_squares(n):
  return (n * (n + 1) * (2 * n + 1)) // 6

# Cube sum of first n natural numbers
def cube_sum(n):
  return (n * (n + 1) // 2) ** 2

#  Simple interest and compound interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

# Whether a number is Prime or not
def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True