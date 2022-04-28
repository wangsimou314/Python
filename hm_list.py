
'''
name_list = ['simon', 'allen', 'kevin']
name_list[1] = 'william'
print(name_list[1])
name_list.append('kevin')

name_list[3] = 'ivy'

print(name_list)

name_list.insert(0,'ryan')
print(name_list)

expend_list = ['lei' , 'michael']

name_list.extend(expend_list)
name_list.reverse()
print(name_list)

name_list.remove('simon')
print(name_list.count('ivy'))

name_list.pop(1)
print(len(name_list))

for name in name_list:
    print(name)

brand_list = ('nike','adidas','puma')

for brand in brand_list:
    print(brand)

new_tupe = list(brand_list)
print(type(new_tupe))

print(new_tupe)

my_name = "simou"
for char in my_name:
    print(char,end='|')

'''

'''''''''''
for语句钟如果没有break掉，最后可以执行一个ELse
'''''''''''
a = [1,2,3,4]

for char in a:
    print(a.index(char))
    if a.index(char) == 2:
        break
else:
    print('this is a test')
