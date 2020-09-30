def serviceLane(n, cases,width):
    m = []
    for i in range(cases[0],cases[1]+1):
        m.append(width[i])
    print(min(m))
        

if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        # cases.append(list(map(int, input().rstrip().split())))
        cases=(list(map(int, input().rstrip().split())))

        serviceLane(n, cases,width)

