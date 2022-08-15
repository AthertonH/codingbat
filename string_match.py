# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#
#
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] and a[i+1] == b[i] and b[i+1]:
            count += 1
    return count

string_match('xxcaazz', 'xxbaaz')

print(x)