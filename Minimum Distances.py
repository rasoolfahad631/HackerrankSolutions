def minimumDistances(a):
    l = []
    for  i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                m = abs(i - j)
                l.append(m)
    if(len(l) == 0):
        print(-1)
    else:
        print(min(l))


if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    minimumDistances(a)


