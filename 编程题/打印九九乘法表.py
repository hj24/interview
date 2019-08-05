# 左对齐和右对齐两种方式打印九九乘法表
# reverse = False 左对齐，反之右对齐

def show(reverse=False):
    for i in range(1, 10):
        if reverse:
            for j in range(9 - i):
                print('         ', end='\t')
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}', end='\t')
        print(end='\n')

if __name__ == '__main__':
    show(reverse=False)