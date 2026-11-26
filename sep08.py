# class Developer:
#     def __init__(self,name):
#         self.name=name
#         print(f'Employee : {self.name} , Role : Developer')
# class Tester:
#     def __init__(self,name):
#         self.name=name
#         print(f'Employee : {self.name} , Role : Tester')
# class Manager:
#     def __init__(self,name):
#         self.name=name
#         print(f'Employee : {self.name} , Role : Manager')


# def Employee_factory(role,name):
#     if role=="Developer":
#         return Developer(name)
#     elif role=="Tester":
#         return Tester(name)
#     elif role=="Manager":
#         return Manager(name)
# Employee_factory("Developer","Harsha")


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        self.old_salary=salary
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,new_salary):
        if new_salary<0:
            print("Negative values not accepted ! ")
        else:
            self.__salary=new_salary
e=Employee("harsha",50000)
e.salary=100000
print(e.name)
print(e.old_salary)
print(e.salary)

