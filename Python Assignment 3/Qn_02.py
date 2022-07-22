

list1 = ['x','y','z']
result =[item*num for item in list1 for num in range(1,5) ]
print(result)
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']


list2 = ['x','y','z']
result =[item*num for num in range(1,5) for item in list2  ]
print(result)

list3 = [2,3,4]
result = [[item+num] for num in range (0,3) for item in list3 ]
print(result)


list4 =[2,3,4,5]
result = [[item+num for item in list4] for num in range (0,4) ]
print(result)


list5 = [1,2,3]
result = [(item,num) for num in range(1,4) for item in list5 ]
print(result)
result1  = [(num,item) for item in list5  for num in range(1,4) ]
print(result1)