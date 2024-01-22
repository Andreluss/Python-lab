# This is a sample Python script.
import random
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pi_approx(radius, attempts=1000):
    cnt_inside = 0
    for i in range(attempts):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        distance_squared = x**2 + y**2
        if distance_squared <= radius ** 2:
            cnt_inside += 1

    return 4.0 * cnt_inside / attempts



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(pi_approx(10, 330000))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
