mrp_price = [100, 213, 123.43, 456, 357, 342, 3423]
sale_price = [214, 234, 343.3, 345.24, 12, 244, 6421 ]

for x, y in zip(mrp_price, sale_price):
    print(f"MRP PRICE: {x} | SALE PRICE: {y} | Profit: {round(y-x, 2)}")
