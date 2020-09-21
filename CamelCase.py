def camelcase(s):
    count = 1
    for i in s:
        if i == i.upper():
            count += 1 
    print(count)

if __name__ == '__main__':
    s = input()
    camelcase(s)

