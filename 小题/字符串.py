# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = list(set(s))
s.sort(reverse=False)
print(''.join(s))