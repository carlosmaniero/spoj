n = int(raw_input())

for i in range(0, n):
        a = raw_input()
        num1, num2 = a.split(" ")
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        num = num1 + num2
        b = str(num)[::-1]
        print int(b)
