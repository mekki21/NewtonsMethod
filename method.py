# inputs : equation function and 1 point
from tokenize import Pointfloat
from turtle import color
from sympy import Symbol, Derivative
import sympy as sym
from prettytable import PrettyTable 
import matplotlib.pyplot as plt

#takes the expression and substitutes with point given
def func(expr, point):
    return round(sym.N(expr.subs(x, point)),4)


#takes the expression derivative and substitutes with point given
def deriv(derived_expr,point):
   return round(sym.N(derived_expr.subs(x, point)),4)


#takes expression and derivative and point given to substitute in newton's formula
def newtonEq(input_expr,derived_expr, initial_point):
  return round(initial_point - (func(input_expr, initial_point) /  deriv(derived_expr, initial_point)),4)
    



x = sym.Symbol('x') #to define that from now on x is a symbol for the equation
input_expr = input('Enter an expression in x: ') #takes input from user as string
fx = eval(input_expr, {'x': x, 'sin': sym.sin, 'cos': sym.cos, 'e': sym.E}) #turns that string into a function with understandable trig
fxDash = sym.diff(fx, x) #derives function once for the whole code
initial_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))
tempFirst = initial_point #save initial point for graphing purpose, as intial point is overwritten every step


# will be changed with GUI
# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

# arrays for x and y axis of function(x) and d(x) (used for graphing function and tangent only)
funcY = []
funcX = []
dfuncY = []
dfuncX = []



for i in range(iterations):
    first_point = initial_point #Xo
    initial_point = round(newtonEq(fx,fxDash,first_point),4) #X1 using Xo
    #next arrays are for tangent drawing
    dfuncY.append([func(fx,first_point),0]) 
    dfuncX.append([first_point,initial_point])
    
    
    myTable.add_row([i, first_point, func(fx,first_point), deriv(fx, first_point), initial_point, abs(round(initial_point - first_point,4))])
   
print(myTable)



#by the end of the iterations, initial point is actually the last point we reached
last_point = int(initial_point)

steps = abs(tempFirst - last_point) + 4 # for seen range of the curve "2 before the root and 2 after"

for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve
    funcY.append(func(fx,(last_point-2)+(i/2))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
    funcX.append((last_point-2)+(i/2)) # x axis


def plot(x,y ,dx, dy):
    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')

    # plotting the d(x) tangent
    for i in range (iterations-1): # to skip last point " as the function stopped "
        plt.plot(dx[i], dy[i], color="red")
  
    plt.legend(["F(x)" , "F'(x)"],loc='upper left')
    plt.show()

# plot
plot(funcX,funcY,dfuncX,dfuncY)
