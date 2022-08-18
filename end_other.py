# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
#
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    if len(a) >= len(b):
        for i in range(0, len(a)):
            if a.lower()[-i:] == b.lower()[-i:]:
                return True
        return False
    elif len(b) >= len(b):
        for i in range(0, len(b)):
            if b.lower()[-i:] == a.lower()[-i:]:
                return True
        return False

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):]