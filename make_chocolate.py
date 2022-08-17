# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.
#
#
# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 3, 11) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
    bbars = goal//5
    if bbars > big:
        bbars = big
    goal = goal - (bbars*5)
    if goal <= small:
        return goal
    return -1