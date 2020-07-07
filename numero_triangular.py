def tri(n):
    from functools import reduce
    return reduce(lambda x,y: x + y, list(range(1,n+1)))

def main(n):
    print('número triangular %d' %(tri(n)))
if __name__ == '__main__':
    n = 12
    main(n)