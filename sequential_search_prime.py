def sequential_search_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if sequential_search_prime(num):
            prime_numbers.append(num)
    return prime_numbers


numbers = [1, 3, 13, 5, 19, 22, 4]
prime_numbers = find_prime_numbers(numbers)
print("Bilangan prima dalam daftar:", prime_numbers)
