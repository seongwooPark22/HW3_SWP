
def factorial(N) :
    if (N == 0) :
        return 1
    return N*factorial(N-1)

def main() :
    for i in range(0,14+1)[::2] :
        print("{0:d}! :".format(i),factorial(i))

if __name__ == "__main__" :
    main()

