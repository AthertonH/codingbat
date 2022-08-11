# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
    if abs(100-n) <= 10:
        return True
    elif abs(200-n) <= 10:
        return True
    else:
        return False

def near_hundred_short(n):
    return((abs)(100-n) <=10 or (abs)(200-n) <=10)


x = near_hundred(93)
print(x)


x = near_hundred_short(83)
print(x)