# class SmartDevice:
#     def __init__(self,Device_name,Power_status,Battery_percentage):
#         self.Device_name=Device_name
#         self.Power_status=Power_status
#         self.Battery_percentage=Battery_percentage
#     def Turn_on(self):
#         self.Power_status="ON"
#     def Turn_off(self):
#         self.Power_status="OFF"
#     def Display_Device_Status(self):
#         print(f'Device Name : {self.Device_name}')
#         print(f'Power Status : {self.Power_status}')
#         print(f'Battery Percentage : {self.Battery_percentage}')
# obj1=SmartDevice("Fan","ON",75)
# obj2=SmartDevice("Watch","ON",34)
# obj3=SmartDevice("AC","OFF",90)
# obj1.Turn_off()
# obj1.Display_Device_Status()
# obj2.Turn_off()
# obj2.Display_Device_Status()
# obj3.Turn_on()
# obj3.Display_Device_Status()




# s="3[a]2[bc]"
s = "2[a3[c]]"
stack=[]
curr=""
num=0
for ch in s:
    if ch.isdigit():
        num=num*10+int(ch)
    elif ch=="[":
        stack.append((curr,num))
        curr=""
        num=0
    elif ch=="]":
        prev,repeat=stack.pop()
        curr=prev+curr*repeat
    else:
        curr+=ch
print(curr)