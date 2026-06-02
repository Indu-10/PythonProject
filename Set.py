#set we can store unique values , not ordered
colors={'red','yellow','yellow','violet'}
print(colors)
#output is {'yellow', 'red', 'violet'} as it will store only unique values, no error will be thrown
#converting to list
colors_list=list(colors)#it passes only unique values
print(colors_list)
lis_2=('r','r','l')#here duplicate value displays
print(lis_2)
set_value=set(lis_2)#list to set conversion
print(set_value)#here unique value displays
