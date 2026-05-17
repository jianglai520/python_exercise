# coding = UTF-8

#基本的列表操作

#增加元素
a_list = ['a', 'b', 'dffgggghrgjgjg']

a_list.append("i love you")   
print(a_list)

a_list.insert(1, 'a+++++++')
print(a_list)

a_list.extend(['n', 'm'])
print(a_list)


#搜索元素
b_list = ['i', 'love', 'you']

print(b_list.index('i'))

print('i' in b_list)


#删除元素
c_list = ['i', 'hate', 'hate', 4, 0000000000000000]

c_list.remove('i')
print(c_list)

c_list.remove('hate')   #删除首次出现的值
print(c_list)

c_list.pop()   #pop会做两个事：删除List中的最后一个元素， 然后返回删除元素的值
print(c_list)



#list运算符

a_list = [1,2]
b_list = [3, 4]

print(a_list + b_list)   #两个列表相加

a_list += ['11111111']  #添加元素
print(a_list)

print(b_list * 2)  #重复

#list过滤

li = ['a', 'floor', 'flour', 'hate', 'you', 'you']
a_li = [i for i in li if len(i) >= 3]
print(a_li)

print([i for i in li if len(i) >= 3])

b_li = [i for i in li if li.count(i) == 1]   #count统计元素的出现次数
print(b_li)


#list的映射解析

li = [1, 2, 3, 4]
print([i ** 2 for i in li])

#list分割字符串
li = ['jiayou', 'deterrence', 'reduce', 'sacrifice']
s = ';'.join(li)
print(s)

print(s.split(';'))

#dictionary中的解析
params = {'floor':'flour', 'ascent' :'ink', 'advict':'desk', 'sterotype': 'type'}
print(params.keys())
print(params.values())
print(params.items())

print([k for k, v in params.items()])
print([v for k, v in params.items()])
print([(k, v) for k, v in params.items()])
print(["%s = %s" % (k, v) for k, v in params.items()])

print(";".join(["%s = %s" % (k, v) for k, v in params.items()]))