# 字典删除键，合并两字典
dic = {'name': 'hj', 'age': 21}
print(dic)
del dic['age']
print(dic)
dic2 = {'age': 22}
dic.update(dic2)
print(dic)

# 字典根据键从小到大排序
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

d = sorted(dic.items(), key=lambda k: k[0])
print(d)

# 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
s = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h".split(';')
c = Counter(s)
print(c)