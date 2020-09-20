def jumpingOnClouds(c):
    c.insert(n,0)
    count = 0
    i = 0 
    while (i < n-1):
        i += (c[i+2] == 0) + 1
        count += 1
    print(count)

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    jumpingOnClouds(c)





