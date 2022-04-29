size = 40


def generate_code(x, arr):
    code = ''
    flag = False
    for i in range(size - 1, -1, -1):
        if arr[i] <= x:
            flag = True
            code += '1'
            x -= arr[i]
            continue
        if flag:
            code += '0'
    return code


fibonacci = [0] * size
fibonacci[0] = 1
fibonacci[1] = 2
for i in range(2, size):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
t = int(input())
for _ in range(t):
    k = int(input())
    print(generate_code(k, fibonacci))
