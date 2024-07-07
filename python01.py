for right in range(1, 10):

    for left in range(1, right+1):
        print(f'{left}x{right}={left * right}', end='\t')

    print()
