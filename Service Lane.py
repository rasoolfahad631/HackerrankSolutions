def serviceLane(n, cases):
    # Returning a array with minimum width for each test case
    # slice[start:stop] will omit stop'th index hence add 1 to stop
    return [min(width[i[0] : i[1] + 1]) for i in cases]
        

if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        # cases.append(list(map(int, input().rstrip().split())))
        cases=(list(map(int, input().rstrip().split())))

        serviceLane(cases, width)

