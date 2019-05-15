#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
            continue
        lp = int(str(grade)[-1])
        if lp == 4 or lp == 9:
            result.append(grade+1)
        elif lp == 3 or lp == 8:
            result.append(grade+2)
        else:
            result.append(grade)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

