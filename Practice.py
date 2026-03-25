#Find the largest element in a list.
def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

#Check if a number is even or odd.
def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

#Reverse a string (without slicing).
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

#Count vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

#Find the sum of digits of a number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

#Check if a string is a palindrome.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

#Print Fibonacci series up to N terms.
def print_fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

#Swap two variables without a third variable.
def swap_variables(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

#Count words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

#Find minimum and maximum in a list.
def find_min_max(lst):
    if not lst:
        return None, None
    min_val = max_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

#Find the second largest number in a list.
def find_second_largest(lst):
    if not lst or len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

#Remove duplicates from a list (without set).
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

#Count frequency of elements in a list.
def count_frequency(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

#Merge two sorted lists.
def merge_sorted_lists(lst1, lst2):
    merged = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

#Find the intersection of two lists.
def find_intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]

#Rotate a list by k positions.
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

#Check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

#Find the first non-repeating character.
def find_first_non_repeating(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None

#Flatten a nested list.
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

#Find all pairs with a given sum.
def find_pairs_with_sum(lst, target_sum):
    pairs = []
    num_dict = {}
    for num in lst:
        complement = target_sum - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = True
    return pairs

#Print a right triangle pattern.
def print_right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

#Print a pyramid pattern.
def print_pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

#Print all prime numbers in a range.
def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

#Check if a number is Armstrong.
def is_armstrong_number(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n