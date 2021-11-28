'''
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
'''
def prime_list(start, stop):
    def is_prime(n):
        counter = 0
        for i in range(2, n + 1):
            if n % i == 0:
                counter += 1
        if counter == 1:
            return True
        return False
    lst = []
    for i in range(start, stop + 1):
        if is_prime(i):
            lst.append(i)
    return lst

print(prime_list(1, 150))