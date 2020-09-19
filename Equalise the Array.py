import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    l = []
    arr1 = set(arr)
    for i in arr1:
        l.append(arr.count(i))
    print(n-max(l))


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    equalizeArray(arr)

