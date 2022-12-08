import time
from multiprocessing import current_process, Pool

def is_prime(number):
    """
    Checks if given number is a prime number, otherwise return False
    :param number:
    :return:
    """
    divisors = 0
    if number % (number / 2) == 0:
        divisors += 1

    for n in range(2, (number // 2) + 1):
        if number % n == 0:
            divisors += 1
            if divisors >= 2:
                return ''

    print(str(number) + ' Found by' + current_process().name)

    return number


def iterate_primes(last_number) -> list:
    """
    Checks numbers from 2 to last_number and if prime adds to list
    :param last_number:
    :return list of primes:
    """
    work = []
    # number of parallel processes
    p = Pool(16)
    for n in range(2, (last_number + 1)):
        work.append(n)

    output = p.map(is_prime, work)
    primes_list = [elem for elem in output if elem != '']
    return primes_list

if __name__ == '__main__':

    end_number = int(input("Enter number "))

    start = time.perf_counter()  # badamy ile trwal watek
    experimental = []

    primes = iterate_primes(end_number)  # moja wlasna funkcja filtrujaca
    # primes = list(filter(is_prime, range(2,end_number)))            #wbudowana funkcja fitrujaca - przekaujemy funkje zwracajaca true

    end = time.perf_counter()

    print(primes)
    print(f"Found {len(primes)} prime numbers.")
    print(f"Operation took {end - start:0.6f} s")

    #print(f'Number of CPU: {multiprocessing.cpu_count()}')