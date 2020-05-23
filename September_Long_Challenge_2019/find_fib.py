def find_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return find_fib(n - 1) + find_fib(n + 1)


# for i in range(50):
#    print(find_fib(i))

a = 0
b = 1

# print(a, " ", b, end=" ")

for i in range(65):
    if i == 1:
        print(i, " : ", a)
    elif i == 2:
        print(i, " : ", b)
    else:
        temp = b
        b = (a + b) % 10
        a = temp
        if i == 64:  # i % 59 == 0 or i % 60 == 0:
            print(i, " : ", b)
