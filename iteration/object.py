obj_1 = {
    'a': 10,
    'b': '施明德',
    'c': 'abc',
    'd': 20,
}

# for item in obj_1:
#     print(item)
# a b c d

# for item in obj_1.items():
#     print(item)
# ('a', 10)
# ('b', '施明德')
# ('c', 'abc')
# ('d', 20)
# 因為item是一個一個tuple，可以再印出來前，指派給任2變數，就能個別取得值了
# 如下

for item in obj_1.items():
    keys, values = item
    print(keys, values)
# a 10
# b 施明德
# c abc
# d 20

# 然後也可以再簡化
for keys, values in obj_1.items():
    print(keys, values)
# a 10
# b 施明德
# c abc
# d 20

# 個別取keys和values
for keys in obj_1.keys():
    print(keys)
# a
# b
# c
# d

for values in obj_1.values():
    print(values)

# 10
# 施明德
# abc
# 20
