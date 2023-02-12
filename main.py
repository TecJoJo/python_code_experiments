# li = [9,1,8,2,7,3,6,4,5]
# li.sort()
# li.sort(reverse=True)
# # s_li = sorted(li)
# s_li = sorted(li,reverse=True)



# print("Sorted Variable:\t",s_li)
# print("original Variable:\t",li)

# #tuple can't be sorted by calling .sort() method
# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)
# print("tuple\t", s_tup)

# di = {"name": "Corey", "job":"programming","age":None, "os":"Mac"}
# s_di = sorted(di)
# print("Dict\t", s_di)

li = [9,1,8,2,7,3,-6,-4,-5]
s_li = sorted(li, key=abs)
print(s_li)