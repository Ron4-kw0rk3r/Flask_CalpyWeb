import math
import sys

from click import command


def brainsolver( w , t, changer):
    if float(w) and float(t):


        w = float(w)
        t = float(t)
        # isnumeric is simple number dectec condtcional code
        if changer == 'sum':
            confuser  = lambda x , y : x + y 
            oneployed = confuser( w , t )
            comon = eval("w + t")
            print(comon)
            # confuser =  w + t
            # confuser = w + t
            #print(confuser(w, t))
            # return  brainsolver( ,y w )
        elif changer == 'rest':
            confuser = lambda x , y : x - y 
            oneployed =  confuser(w , t )
            comon = eval("w - t")
            print(comon)
            # confuser = w - t 
        elif changer == 'multiply':
            confuser = lambda x , y : x * y 
            oneployed = confuser(w , t)
            comon = eval("w * t")
            print(comon)
        elif changer == 'divi':
            confuser = lambda x , y : x / y 
            # confuser =  w / t 
            comon=eval("w / t")
            oneployed = confuser(w,t ) 
            print(comon)
           
        elif changer == 'mod':
            confuser = lambda x , y : x / y 

            oneployed = confuser(w ,t )
            comon =  eval("w % t")
            print(comon) 
            
        else:
            confuser = "Error not operation !!!"
    else:
        confuser="please attemp  problem resolv"

    # return  
    # # confuserd
    return oneployed
    # return  confuser

# print(brainsolver(10, 10 , str(rest)))
