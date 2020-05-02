def design_mat(height, width):
    message = 'WELCOME'
    characters = '.|.'
    nums = [2 * i + 1 for i in range(height // 2)]
    # Top
    for i in nums:
        yield str(characters * i).center(width, '-')
    # Middle
    yield str(message).center(width, '-')
    # Bottom
    nums = nums[::-1]
    for i in nums:
        yield str(characters * i).center(width, '-')


if __name__ == '__main__':
    n, m = list(map(int, input().rstrip().split()))
    assert n % 2 == 1  # make sure n is an odd natural number
    assert m == n * 3  # make sure m is 3 times n
    mat = design_mat(n, m)
    print(*mat, sep='\n')
