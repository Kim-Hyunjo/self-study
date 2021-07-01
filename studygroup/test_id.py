'''
lst = []  
print(id(lst))  # 2450925392960
lst.append(1)
print(id(lst))  # 2450925392960
lst = []
print(id(lst))  # 2450925393216
lst.append(2)
print(id(lst))  # 2450925393216
lst = [2]
print(id(lst))  # 2450925392960
lst.append(3)
print(id(lst))  # 2450925392960
lst = []
print(id(lst))  # 2450925393216
'''
lst = []
print(id(lst))  # 2284959077504
lst.append(4)
print(id(lst))  # 2284959077504
lst.clear()
print(id(lst))  # 2284959077504
lst.append(5)
print(id(lst))  # 2284959077504