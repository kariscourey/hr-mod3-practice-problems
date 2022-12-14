def can_make_row(num_short, num_long, goal):

    # check how many times 5 can go into goal
    long_times = goal // 5

    # check how many times 1 can go into remainder
    short_times = (goal - long_times * 5) // 1

    # see if number of times 5 goes into goal <= num_long
    # see if number of times 1 goes into remainder <= num_short
    return long_times <= num_long and short_times <= num_short


num_short = 1
num_long = 2
goal = 8

print(can_make_row(num_short, num_long, goal))
