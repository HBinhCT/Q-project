from collections import OrderedDict

item_price = OrderedDict()
for _ in range(int(input())):
    item, price = input().rstrip().rsplit(' ', 1)
    item_price[item] = item_price.get(item, 0) + int(price)
for item in item_price:
    print(item, item_price[item])
