def pat(n):
    for i in range(1,n+1):
        print(("* ")*(n+1-i)+(" "*(i-1)))

pat(3)
pat(4)
pat(8)