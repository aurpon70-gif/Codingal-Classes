s1 = [2, 3, 1]
s2 = [4, 5, 6]
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))
