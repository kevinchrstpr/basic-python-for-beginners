# Input Data User

# The input data must be string
data = input("Input Data = ")

print("Data = ", data,"type ",type(data))

# If we want to input an integer / float, then
number = float(input("Input number = "))
number1 = int(input("Input number = "))

print("Input Number = ", number,"type =", type(number))
print("Input Number = ", number1,"type =", type(number1))

# Boolean
data_boolean = bool(input("Input Boolean : ")) #this input would result true even if its 0

print("Input Boolean = ", data_boolean, "type =", type(data_boolean))

data_boolean = bool(int(input("Input Boolean : "))) #this one perfectoo

print("Input Boolean = ", data_boolean, "type =", type(data_boolean))