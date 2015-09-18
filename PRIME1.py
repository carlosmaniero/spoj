from array import array


# Criação de um array com todos os primos divisores
primes = array('i', [2])
# Define o divisor máximo (raiz do numero)
max_div = int(1000000000 ** 0.5) + 1
max_div = 32000

# Gera todos os primos divisores
for i in range(3, max_div, 2):
    is_prime = True
    max = i ** 0.5 + 1

    for prime in primes:
        if prime >= max:
            break

        if i % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)

# Recebe a quantidade de linhas
t = int(input())
output = ''

for _ in range(t):
    if _ > 0:
        output += '\n'

    # Pede os intervalos
    m, n = input().split(' ')
    m, n = int(m), int(n)

    if m < 2:
        m = 2

    if n < max_div and 1 != 2:
        # Se o final do intervalo for menor do que os primos conhecidos
        # só imprime
        for prime in primes:
            if prime >= m and prime <= n:
                output += str(prime) + '\n'
            elif prime > n:
                break
    else:
        max = n ** 0.5 + 1
        isprime = [True] * 100001

        for prime in primes:
            if prime >= max:
                break

            # start é o próximo múltiplo do número primo a partir de m
            if prime >= m:
                start = prime * 2
            else:
                start = m + ((prime - m % prime) % prime)

            # percorre o array de i em i colocando false
            # para todos os multiplos de i
            mult_slice = slice(start - m, n + 1 - m, prime)
            falses = [False] * len(isprime[mult_slice])
            isprime[mult_slice] = falses

        for i in range(m, n + 1):
            if isprime[i - m]:
                output += str(i) + '\n'

print(output[:-1])
