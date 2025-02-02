class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    def get_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers = [10, 3, 5, 8, 11, 17, 20, 23, 29, 30]
prime_filter = PrimeFilter(numbers)

print("Prime numbers:", prime_filter.get_primes())
