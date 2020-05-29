
# # def sum_mul_sub(a, b):
# # 	return a+b, a*b, a-b



# # s1, m1, sub1 = sum_mul_sub(5, 7)
# # print(s1, m1, sub1)


# # a=3
# # b=5
# # a, b= b,a
# # print('a={} and b={}'.format(a, b))



# mydict = {"rutvik":11,"sahil":11,"nikunj":11,"kishan":7}

# print(mydict["sahil"])

# for a in mydict:
# 	print("{} prefers {}".format(a, mydict[a]))



fruits = ["Apple", "Banana", "Orange"]
quantities = [12, 26, 6]
prices = [100, 10, 25]


f = {x:{} for x in fruits}
# print(f)
for fr, q, p in zip(fruits, quantities, prices):
	f[fr] = {"quantity":q, "price":p}

print(f)












                                  
