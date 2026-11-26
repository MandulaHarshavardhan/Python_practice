# x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
# a=0
# for i in x:
#     cnt=0
#     for j in i:
#         if j%2==0:
#             cnt+=1
#     if cnt>a:
#         a=cnt
#         res=i
# print(res)

# x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
# dici={}
# for i in x:
#     for j in i:
#         dici[j]=dici.get(j,0)+1
# a=[]
# for k,v in dici.items():
#     if v==1:
#         a.append(k)
# print(a)

# x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
# max_diff=0
# for i in x:
#     smallest=min(i)
#     largest=max(i)
#     diff=largest-smallest
#     if diff>max_diff:
#         max_diff=diff
#         res=i
# print(res)


# class Cart:
#     def __init__(self,name,price,quantity,category):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#         self.category=category
#         self.totalcost=0
#         self.Highest_subtotal_product={}
#     def Subtotal(self):
#         print(f' {self.name} Subtotal : {self.quantity*self.price}')
#         self.totalcost+=self.quantity*self.price
#         self.Highest_subtotal_product[self.name]=self.price

# item1=Cart("Laptop",50000,1,"Electronics")
# item2=Cart("Mouse",1000,2,"Accessories")
# item3=Cart("Keyboard",2000,1,"Accessories")
# item1.Subtotal()
# item2.Subtotal()
# item3.Subtotal()

# cart = {
#     "item1": {
#         "name": "Laptop",
#         "price": 50000,
#         "quantity": 1,
#         "category": "Electronics"
#     },
#     "item2": {
#         "name": "Mouse",
#         "price": 1000,
#         "quantity": 2,
#         "category": "Accessories"
#     },
#     "item3": {
#         "name": "Keyboard",
#         "price": 2000,
#         "quantity": 1,
#         "category": "Accessories"
#     }
# }
# totalcost=0
# Highest=0
# Discount=0
# for item,product in cart.items():
#     subtotal=0
#     subtotal+=product["price"]*product["quantity"]
#     totalcost+=subtotal
#     print(f'{product["name"]} Subtotal : {subtotal}')
#     if product["price"]>Highest:
#         Highest=product["price"]
#         res=product["name"]
# print(f'Total Cost : {totalcost}')
# print(f'Highest Subtotal Product : {res}')
# if totalcost>50000:
#     Discount=totalcost*10//100
#     print(f'Discount : {Discount}')
# finalprice=totalcost-Discount
# print(f'Final Price : {finalprice}')


# s="3[a]2[bc]"
# num=0
# curr=""
# stack=[]
# for i in s:
#     if i.isdigit():
#         num=num*10+int(i)
#     elif i=="[":
#         stack.append((curr,num))
#         curr=""
#         num=0
#     elif i=="]":
#         prev,repeat=stack.pop()
#         curr=prev+curr*repeat
#     else:
#         curr+=i
# print(curr)

# length="2.3"
# length=int(length)
# print(length)

temperatures = [30,38,30,36,35,40,28]
stack=[]
res=[0]*len(temperatures)
for i,t in enumerate(temperatures):
    while stack and t>temperatures[stack[-1]]:
        stackind=stack.pop()
        res[stackind]=i-stackind
    stack.append(i)
print(res)





