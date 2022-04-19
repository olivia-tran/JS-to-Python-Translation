"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    return result


def print_as_numbered_list(items):
    for i in range(1, len(items)):
        print(i, ".", items[i])


def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    return nums


def censor_vowels(word):
    chars = []
    for char in word:
        if char in 'aeiou':
            chars.append('*')
        else:
            chars.append(char)
    return ''.join(chars)


# print(censor_vowels('hello world'))


def snake_to_camel(string):
    camel_case = []

    for char in string.split("_"):
        camel_case.append(char.title())
    # ['Hello', 'World']
    # camel_str = ''.join(camel_case)
    return ''.join(camel_case).replace(" ", "")


# print(snake_to_camel('hello world'))


def longest_word_length(words):
    longest_word = len(words[0])
    for word in words[1:]:
        if longest_word < len(word):
            longest_word = len(word)
    return longest_word


# print(longest_word_length(['jellyfish', 'zebra']))


def truncate(string):
    result = []
    for char in string:
        if (len(result) == 0) or (char != result[-1]):
            result.append(char)
    return ''.join(result)


# print(truncate('aaaabbbbcccca'))
# print(truncate(''))


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        if parens < 0:
            return False
    return parens == 0  # would parens ever be 0?


# print(has_balanced_parens('((This) (is) (good))'))


def compress(string):
    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)


print(compress('Hello, world! Cows go moooo...'))
