
def introTutorial(V, arr):
    m = [arr.index(i) for i in arr if i == V ]
    for i in m:
        print(i)
if __name__ == '__main__':

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    introTutorial(V, arr)

 
