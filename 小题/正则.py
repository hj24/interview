# <div class="name">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
pattern = re.compile('<div.*?class=".*?">(.*?)</div>')
s = '<div class="name">中国</div>'
print(re.findall(pattern, s))

# 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
a = "not 404 found 张三 99 深圳"
list_a = a.split(' ')
res = re.findall('\d+|[a-zA-Z]+', a)
list_res = [ch for ch in list_a if ch not in res]
print(' '.join(list_res))

# 字符串a = "not 404 found 张三 99.58 深圳"，每个词中间是空格，用正则过滤掉英文和小数，最终输出"张三 深圳"
a = "not 404 found 张三 99.58 深圳"
list_a = a.split(' ')
reg = re.findall('\d+\.?\d*|[a-zA-Z]+', a)
list_res = [ch for ch in list_a if ch not in reg]
print(' '.join(list_res))

# a="张明 98分"，用re.sub，将98替换为100
a="张明 98分"
res = re.sub('\d+', '100', a)
print(res)

#正则匹配，匹配日期2018-03-20
# url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
s = re.findall('dateRange=(.*?)%7C', url)
print(s)