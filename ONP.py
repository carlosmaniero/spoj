def onp(expression):
    stack = []
    operators = '+-*/^'
    output = ''

    for char in expression:
        if char.isalpha():
            output += char
        elif char in operators:
            stack.append(char)
        elif char == ')':
            output += stack.pop()

    return output

output = ''
t = int(input())

for _ in range(t):
    output += onp(input()) + '\n'

print(output[:-1])
