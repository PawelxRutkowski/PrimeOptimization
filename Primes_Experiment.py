import time

def is_prime(number) -> bool:  # funkcja ma zwracac bool
    """
    Checks if given number is a prime number
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
                return False

    return number


def iterate_primes(last_number) -> list:
    """
    Checks numbers from 2 to last_number and if prime and adds to list
    :param last_number:
    :return list of primes:
    """
    primes_list: list[bool] = []
    for n in range(2, (last_number + 1)):
        if prime := is_prime(n):
            primes_list.append(prime)
            # print(f"{prime}")
    return primes_list


if __name__ == '__main__':
    end_number = int(input("Podaj liczbe calkowita "))

    start = time.perf_counter()  # badamy ile trwal watek

    primes = iterate_primes(end_number)  # moja wlasna funkcja filtrujaca
    # primes = list(filter(is_prime, range(2,end_number)))            #wbudowana funkcja fitrujaca - przekaujemy funkje zwracajaca true

    end = time.perf_counter()

    print(primes)
    print(f"Znaleziono {len(primes)} liczb pierwszych.")
    print(f"Calosc operacja zajela {end - start:0.6f} s")


