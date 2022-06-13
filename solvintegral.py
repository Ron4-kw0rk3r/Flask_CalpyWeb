#!/usr/bin/python3
#*-* coding:utf-8 *-*
# from this import d


try: 
    import sympy
    
    from sympy import init_session
    # from sympy import __init__suggestions
    import sys
    import math

except ErrorModuleImport:
    from sympy import  *



def limitation(intervand):
    x, y ,z = symbols('x, y ,z')
    init_printing(use_unicode=True)
    # how to create code a str in transform value comparating 
    limas = str(intervand)
    lamber = limit(limas)
    # how operation is x example testings appp( sin(x) / x , 0) << -- constant>
    print(f'result limit ; {lamber}')




def decliff(intervand):
    x , y , z = symbols('x, y, z')
    init_printing(use_unicode=True)
    # how to create code a str in transform value comparating 
    looader = str(intervand)
    cod = diff(looader)
    print(f'result derivate ; {cod}')
    



def intervaldor(intervand):
    x , y , z  = symbols('x, y , z ')
    init_printing(use_unicode=True)
    oper = ( x  + 5*x**2 )
    # oper
    sup = diff(oper)
    # print(diff(oper))
    # print(integrate(sin(x) * exp(x) - intervand))
    print(f'result integral ; {sup}')
    
    #diff(cos**2x - 10x + 5**3)
def matrxxx(intervand):
    x , y ,z, t = symbols
    init_printing(use_unicode=True)
    champ = str(intervand)
    build = Matrix(champ)
    print(f'result matrix ; {build}')
       


    
# intervaldor(10, 10)
