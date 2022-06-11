#!/usr/bin/python3.8



def uname(w):
    sturn =  lambda x : x - w + 1 
    return sturn(w)

print(uname(10))
