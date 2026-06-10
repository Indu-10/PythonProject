def greet():#defining the function
    #function can be with empty parameter
    print("Hi")#inbuilt function
greet()#it calls the function then only output prints

#with parameter
def greets(name):#parameter
    print(f"Hello {name}")
greets("Hari")#passing arguments
'''instead of above name="Hari" and pass name as parameter'''
print("************")
greets("Indu")#it cannot be empty while calling

#with 2 param
def twoparam(name,age):
    print("Hello",name)
    print("Age is:",age)
twoparam("Indu",18)
n="Kavin"
a=18
twoparam(n,a)#we can assign already and call using this variables as well
twoparam(age=18,name="Indu")#we can change the order as well

#sum of first n natural numbers
def sum(num):
    sum_form=num*(num+1)/2
    return sum_form
val=sum(2)
print(val)
print(sum(1))

