#Built-in
import builtins
print(dir(builtins))

#Global
y = 2
def degree(x):
    return y ** x
print(degree(4))

#Local
def degree(x):
    y1 = 3
    return y1 ** x
print(degree(4))
# print(y1) # It wont work because y1 is local and defines only inside 'degree'

#Enclosing
def degree(x):
    y1 = 3
    def degree_two():
        return y1 ** x
    return degree_two()
print(degree(4))

# Function Encapsulation
# Encapsulation is used to hide the values or state of a structured data object inside a class, preventing direct access to them by clients in a way that could expose hidden implementation details or violate state invariance maintained by the methods.
def message(number):
    def printMessage():
        return 'Number ' + str(number)
    return printMessage()
print(message(12))
# print(printMessage()) shows nothing

# Closure (or function closure)
def message(x):
    def print_message(y):
        return x,y
    return print_message
d = message(4)
print(d)
print(d(5))
print(d(7))
