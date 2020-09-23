#!/bin/python3

def beautifulTriplets(d, arr):
    gc= 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc+=1
    print (gc)

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])                   

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    beautifulTriplets(d, arr)
