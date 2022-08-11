# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
#
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
    first_word = str.split()[0]
    if first_word != "not":
        return("not " + str)
    else:
        return(str)

x = not_string("not candy")



print(x)