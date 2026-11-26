# class Person:
#     def __init__(self,name):
#         self.name=name
# class Employee(Person):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.salary)
#         print("department:",self.department)
# obj=Manager('ravi',50000,'HR')
# obj.display()

# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
# class Electric_Car(Car):
#     def __init__(self,brand,model,battery_capacity):
#         super().__init__(brand,model)
#         self.battery_capacity=battery_capacity
#     def display(self):
#         print(f'Brand : {self.brand}')
#         print(f'Model : {self.model}')
#         print(f'Battery Capacity : {self.battery_capacity}')
# obj=Electric_Car("Tesla","Model 3","75 kwh")
# obj.display()


# class Product:
#     def __init__(self,product_name):
#         self.product_name=product_name
# class Price:
#     def __init__(self,price):
#         self.price=price
# class Bill(Product,Price):
#     def __init__(self,product_name,price,GST):
#         Product.__init__(self,product_name)
#         Price.__init__(self,price)
#         self.gst=GST
#     def display(self):
#         print(f'Product : {self.product_name}')
#         print(f'Price : {self.price}')
#         print(f'Final bill : {self.price + (self.price*self.gst/100)}')
# obj=Bill("Laptop",50000,18)
# obj.display()


class Player:
    def __init__(self,player_name):
        self.player_name=player_name
class Sport:
    def __init__(self,sport_name):
        self.sport_name=sport_name
class Athlete(Player,Sport):
    def __init__(self,player_name,sport_name):
        Player.__init__(self,player_name)
        Sport.__init__(self,sport_name)
    def display(self):
        print(f'Player Name : {self.player_name}')
        print(f'Sport : {self.sport_name}')
obj=Athlete("Virat Kohli","Cricket")
obj.display()
