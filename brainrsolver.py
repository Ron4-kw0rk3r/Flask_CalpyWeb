import math
import sys




def brainsolver( x , y, w):
    if w == 'add':
        confuser =  lambda x , y : x + y 
        # return  brainsolver( ,y w )

    elif w == 'rest':

        confuser =  lambda x , y : x - y 

    elif w == 'mult':
        confuser =  lambda x , y : x * y 
    elif w == 'divi':
        confuser =  lambda x , y : x / y 
    elif w == 'mod':
        confuser =  lambda x , y : x % y 