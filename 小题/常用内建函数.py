# 一行代码求 1 - 100 和
print(sum(range(1, 101)))

# filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_obj = filter(lambda i: i % 2 != 0, a)
odd = [i for i in odd_obj]
print(odd)

# 列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [i for i in a if i % 2 != 0]
print(odd)