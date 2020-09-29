def fairRations(b):
    count = 0
    sum = 0
    for i in range(len(b)):
        sum = sum + b[i]
    if sum%2 == 1:
        print("NO")
    else:
        for i in range(len(b)):
            if b[i] %2 != 0:
                b[i] = b[i] + 1
                b[i+1] = b[i+1] + 1
                count+=2
        print(count)
    
        

if __name__ == '__main__':

    n = int(input())

    b = list(map(int, input().rstrip().split()))

    result = fairRations(b)


