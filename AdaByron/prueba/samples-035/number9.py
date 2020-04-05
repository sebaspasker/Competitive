while True:
    try:
        num = int(input())
        if num % 9 == 0 and num != 0:
            print(num)
    except (EOFError):
        break
