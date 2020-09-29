def chocolateFeast(n, c, m):
    bars = int(n/c)
    wrappers = bars
    rem = 0 
    while(wrappers >=m ):
        rem = int(wrappers/m)
        bars = bars + rem
        rem = rem + int(wrappers%m)
        wrappers = rem
    print(bars)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

    n    = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        chocolateFeast(n, c, m)

