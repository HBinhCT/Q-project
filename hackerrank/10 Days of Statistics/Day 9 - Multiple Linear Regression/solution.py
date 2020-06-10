from sklearn import linear_model

m, n = map(int, input().strip().split())
y = []
x = []
x_pred = []
for _ in range(n):
    *features, y_val = map(float, input().strip().split())
    x.append(features)
    y.append(y_val)
for _ in range(int(input())):
    features = list(map(float, input().strip().split()))
    x_pred.append(features)
lm = linear_model.LinearRegression()
lm.fit(x, y)
result = lm.predict(x_pred)
for num in result:
    print(f'{num:.3f}')
