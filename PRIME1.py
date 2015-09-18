primes = {2}

for i in range(3, 1000000000, 2):
    prime = True

    for j in primes:
        if i % j == 0:
            prime = False
            break
    if prime:
        primes.add(i)

print('gerado')
print(primes)
qtd = int(input())
itens = []
output = ''

for i in range(qtd):
    if output:
        output += '\n'

    min, max = input().split(' ')
    min = int(min)
    max = int(max) + 1

    if min % 2 == 0:
        possibles = set(range(min + 1, max, 2))
    else:
        possibles = set(range(min, max, 2))

    if min <= 2:
        possibles.add(2)

    found = primes & possibles

    found = sorted(list(found))
    for i in found[:100000]:
        output += str(i) + '\n'

print(output[:-1])
