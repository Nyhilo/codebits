import time

def main():
    print("This may take up to 30 seconds. Please be patient...")
    iteration_factor = 50000000

    start = time.time()
    pi = crunchPi(iteration_factor)
    end = time.time()

    print(f'Pi calculated to {iteration_factor} iterations using the Nilakantha series is {pi:.13f}\n'
          f'This calculation took approximately {(end - start):.5f} seconds.\n')
    input('\n\nPress ENTER to close...')


def crunchPi(series: int) -> float:
    pi = 3.0

    for i in range(0, series, 1):
        pi += (-1)**(i+1) * (4 / ((2*n)*(2*n+1)*(2*n+2)))

    return pi


if __name__ == '__main__':
    main()
