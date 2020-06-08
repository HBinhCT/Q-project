mean_x, mean_y = map(float, input().strip().split())
print(f'{160 + 40 * (mean_x + mean_x ** 2):.3f}')
print(f'{128 + 40 * (mean_y + mean_y ** 2):.3f}')
