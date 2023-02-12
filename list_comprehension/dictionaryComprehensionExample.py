names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#zip return a iterator 
#print(list(zip(names,heros)))


# my_dic = {}
# for name, hero in zip(names,heros):
#     my_dic[name] = hero
# print(my_dic)

my_dic = {name:hero for name,hero in zip(names,heros) if name !="Peter"}
print(my_dic)