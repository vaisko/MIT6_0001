list = ['bcd','cbd','cba']
list2 = ['b']
a = 'a'
new_list = []
string = ''
dict = {"raj": 2, "striver": 3, "vikram": 0}

# for item in list:
#     # for i in range(len(item)+1):
#     #     new_list.append(item[:i]+a+item[i:])
#     #     # print(item[:i]+a+item[i:])
#     string += item

for i in dict:
    if dict[i] == max(dict.values()):
            s = i

print(max(dict.values()))
print(s)