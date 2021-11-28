def per(Maths,Hindi,English):
    if Maths>=33:
        print ("Pass in Maths")
    else:
        print("fail in Maths")

    if Hindi>=33:
        print("Pass in Hindi")
    else:
        print("Fail in Hindi")

    if English>=33:
        print("Pass in English")
    else:
        print("Fail in English")

    a=((English+Hindi+English)/3)
    if a>=40:
        print("Pass overall")
    else:
        print("Fail overall")

per(33,33,33)

