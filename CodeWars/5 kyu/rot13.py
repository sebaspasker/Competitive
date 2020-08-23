def rot13(message):
    encoded = ""
    lim = ord(z)
    limM = ord(Z)
    for i in message:
        if i.isalpha():
            i_n = ord(i) + 13
            if i.isupper():
                if i_n > limM:
                    i_n -= 26
            else:
                if i_n > lim:
                    i_n -= 26
            encoded += chr(i_n)
        else:
            encoded += i
    return encoded
