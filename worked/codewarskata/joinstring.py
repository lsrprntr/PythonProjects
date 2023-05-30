def fake_bin(x):
    y=""
    for i in x:
        if int(i) < 5:
            y=y+"0"
        else:
            y=y+"1"
    return y


fake_bin("1234567890")
