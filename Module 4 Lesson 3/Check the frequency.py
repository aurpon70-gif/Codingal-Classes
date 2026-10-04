test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

print("The original dictionary is:", test_dict)

k = 2

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("The number of keys with the frequency is : " + str(res))

