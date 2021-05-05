"""Task1"""
word_dict = {}
word = input(" Введите строку")

for i in word.split():
    if i not in word_dict:
        word_dict[i] = 0
    word_dict[i] += 1
print(word_dict)

"""Task2"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
item = 0
price = 0
stockprice = 0
totalprice = 0
for element in stock:
    items = stock[element]
    price = prices[element]

    totalprice = items * price
    stockprice = stockprice + totalprice
    print(element, ":", items, "*", price, "=", int(totalprice))
print(f"Total price{int(stockprice)}")

"""Task3"""
i = [(i, i * i) for i in range(1, 11)]
print(i)
