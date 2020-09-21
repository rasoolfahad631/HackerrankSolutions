def repeatedString(s, n):
    l = len(s)
    p = n//l
    m = n%l
    print(s.count("a") * p + s[:m].count("a"))

if __name__ == "__main__":

    s = input()
    n = int(input())
    repeatedString(s, n)

