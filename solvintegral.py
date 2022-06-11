#!/usr/bin/python3
#*-* coding:utf-8 *-*
try: 
    import sympy
    from sympy import *
    # from sympy import __init__suggestions
    import sys
    import math

except ErrorModuleImport:
    from sympy import  *



def onvalidor(intervand , comp):
    x , y , z  = symbols('x, y , z ')
    oper = ( x  + 5*x**2 )
    # oper
    print(diff(sin(x) * exp(x) - 1))
    
    
    #diff(cos**2x - 10x + 5**3)
    
onvalidor(10, 10)
