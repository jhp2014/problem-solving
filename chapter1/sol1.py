def solution(n):
    if n == 1:
        return 0

    is_prime = [1 for _ in range(n)]
    is_prime[0], is_prime[1] = 0, 0
    

    for i in range(2, n):
        num = i * 2
        while num < n:
            is_prime[num] = 0
            num += i
    
    return sum(is_prime)


def my_solution(n):
    if n == 1:
        return 0
    
    is_prime = [1 for _ in range(n)]
    is_prime[0], is_prime[1] = 0, 0

    for i in range(2, n):
        apply = 2
        num = i
        while num < n:
            is_prime[num * apply] = 0
            apply += 1

    return sum(is_prime)

        