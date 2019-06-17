import time
import sys
sys.setrecursionlimit(5000)

def main():
    print("This may take up to 30 seconds. Please be patient...")
    # iteration_factor = 50000000
    iteration_factor = 4500

    start = time.time()
    pi = crunchPi(iteration_factor)
    end = time.time()

    print(f'Pi calculated to {iteration_factor} iterations using the Gregory-Leibniz series is {pi:.7f}\n'
          f'This calculation took approximately {(end - start):.5f} seconds.\n')
    input('\n\nPress ENTER to close...')


def crunchPi(series: int, iteration: int = 0, pi: float = 0.0) -> float:
    if iteration == series:
        return pi

    i = iteration + 1
    if not isEven(i):
        if (i+1) % 4 == 0:
            pi -= (4 / i)
        else:
            pi += (4 / i)

    return crunchPi(series, i, pi)


def isEven(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

