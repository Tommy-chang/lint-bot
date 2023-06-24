from sympy import *
from linebot.models import *
def normal(a1=1,an=100,d=1):  
    # sum = 0
    a1 = int(a1)
    an = int(an)
    d = int(d)
    n = ((an - a1) / d) + 1
    sum = int(((an + a1)* n) / 2)
    return sum

def polyn(formula):
    formula = formula.replace("robot.poly ", "")
    result = poly(formula)
    print(result)
    result = str(result).replace("Poly", "")
    message = TextSendMessage(text=result)
    return message
    
def equation(formula):
    formula = formula.replace("robot.equation", "") 
    x = Symbol("x")
    result = str(solve(formula, x))
    message = result.replace("[", "").replace("]", "")
    message = TextSendMessage(text=message)
    return message

    






