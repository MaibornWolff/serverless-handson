import sys
import fibonacci

def main():
    if len(sys.argv) != 2:
        print("Usage: %s n" % sys.argv[0])
        return 1
  
    n = int(sys.argv[1])
  
    if n < 1:
        print("We do not define fibonacci(%d)" % n)
        return 1
  
    f_n = fibonacci.fibonacci(n)
    print(f_n)


if __name__ == "__main__":
    main()
