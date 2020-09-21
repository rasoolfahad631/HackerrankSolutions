def kaprekarNumbers(p, q):
    h = []
    for i in range(p, q+1):
        if (i == 1 ):
            h.append(i)
        elif (i ==2):
            continue
        elif (i == 3):
            continue
        else:  
            d = len(str(i))
            k = len(str(i**2))
            sq = str(i*i)
            l = int ( sq[ : k-d] )
            r = int ( sq[ k-d : ])
            if (r + l == i):
                h.append(i)
     
    if len(h) == 0:
        print("INVALID RANGE")
    else:
        for i in h:
            print(i, end=" ") 


               
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)




