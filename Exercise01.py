# print("Hello World")
# print("Mary's cosmetics")
# print("신씨가 소리질렀다. \"도둑이야\"") #escape
# print("C:\Windows")
# print("오늘은","일요일") #구분은 space 로, comment=#
print('Hello','python!') #space 중간에 넣어줌. Hello python!
print('hello'+'python!') #중간에 공백 없음. hellopython!
# #-----------------------------------------------
# a = 5000
# b = 5000 * 10
# print(b)
# #-----------------------------------------------
# c=50
# d=40
# result = c/d
# print(result)
#
# result = c//d #몫
# print(result)
#
# result = c%d #나머지
# print(result)
# #Boolean-------------------------------------
# live_in_Canada = True
# print(live_in_Canada)
#
# live_in_China = False
# print(live_in_China)
# #List----------------------------------------
# odd_number = [1,3,5,7,9]
# print(odd_number)
# user_data = [20, 'abc', 'defg', True]
# print(user_data)
# #dictionary----------------------------------
# user = {} #dictionary name = user, has two keys
# user['age'] = 25 #age = key
# user['address'] = 'Canada'
#
# print(user)
# print(user['age'])
# print(user.get('age'))
# user['age'] = 90
# print(user.get('age'))
# #if--------------------------------
# if live_in_China: #False
#     print("I am living in China")
#
# #if2--------------------------
# name = 'lala'
# if name == 'lala':
#     print("my name is lala")
# else:
#     print("eeeeeee")
# #for--------------------------------
# for num in odd_number: #num is variable inside odd_number
#     print(num)
#
#
# #function----------------------------
# def add(x,y,z):
#     return x + y + z
#
# result = add(10,30,50)
#
# print (result)



#String Slicing-----------------------
q="hi yuzhang"
print(q)
print(q[0])
print(q[-1]) #last character
print(q[3:10])




#input---------------------------------
w = input("what is your name?") #default : String
z = int(input("age?"))
print(w)
print(z)
