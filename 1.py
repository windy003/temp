列表=[1,1,2,2]

要合并的元素位置=[[0,1],[2,3]]



for 循环参数 in range(0,len(要合并的元素位置)):
    exec('列表{} = []'.format(循环参数))



for 循环参数一 in range(0,len(要合并的元素位置)):
    for 循环参数二 in 要合并的元素位置:
        for  循环参数三  in 循环参数二:
            list('列表{}'.format(循环参数一)).append(列表[循环参数三])

print(1)

print(列表0)
print(列表1)
