#!/usr/bin/python3

# from pydoc import ErrorDuringImport


# from numbers import Integral


# rom re import I


#from crypt import methods


from crypt import methods
from tabnanny import check
from tkinter import W


try: 

    import flask
    from solvintegral import intervaldor
    from solvintegral import limitation
    from solvintegral import  decliff
    from solvintegral import matrxxx
    from brainrsolver import  brainsolver
    from flask import Flask, render_template
    from flask import request
    import time
#    from flask import render_template # import function render_template using file
except  ErrorImportModule:
    import flask


########################### 




# function time to worker hawww

assemb = time.localtime()
status_time =  time.strftime( "%H:%M:%S", assemb)


app = Flask(__name__)

@app.route('/')
# defin route traccing create socket

def function():
    #return "Hello Wrong!"   
    return render_template('jumper.html')
    #    @app.route('/')
#    return "hello wrong"


# capture data
# fetch server incomming  not creater path

@app.route('/operative', methods=["POST"])
def operative():
    #print('hellow rose')
    value_1 = request.form["value_1"]
    value_2 = request.form["value_2"]
    operations = str(request.form['operators'])
    
    # value_4 =  float(value_1) + float(value_2)
    #value_3 = "hellow rose"
    
    
    
    awensome = brainsolver(value_1, value_2, operations)

    # if operations == 'sum':

    # for z in  [ 'sum', 'rest', 'mod', 'divi', 'mult' ]:
    

    if value_1 == [0]:
        return render_template("index.html")
    elif value_2 == [0]:
        return render_template("index.html")
    #calculator
    # 
    #if operations == 'rails':
    #    return render_template("jumper.html", result=value_4)
    if  operations  == 'sum':
        return render_template("jumper.html", result=awensome)
    elif operations == 'rest':
        return  render_template("jumper.html", result=awensome)
    elif operations == 'multiply':

        return render_template("jumper.html", result=awensome)
    elif operations == 'divi':
        return render_template("jumper.html", result=awensome)
    
    elif  operations  == 'mod':
        return render_template("jumper.html", result=awensome)
    else:
        return render_template("index.html")

        
@app.route('/integrals', methods=["POST", "GET"])
def integrals():
    if request.method == 'POST':
        integral_one = request.form["integral_1"]
        check_comp = str(request.form['check_comp'])

        interlooper = intervaldor(integral_one)
        interlimit = limitation(integral_one)
        interderiv =  decliff(integral_one)
        kmatris = matrxxx(integral_one)
        # return render_template('jumper.html', integral_dump=integral_1)
        print(f'select time {check_comp}')
        # check_comp =  str(request.form['check_comp'])

        if check_comp == 'integral':
            return  render_template("jumper.html", dumpy=interlooper )
        elif check_comp == 'derivate':
            return  render_template("jumper.html", dumpy=interderiv)
        elif check_comp == 'limit':
            return  render_template("jumper.html", dumpy=interlimit)
        elif check_comp == 'matrix':
            return  render_template("jumper.html", dumpy=kmatris)
        else:
            return render_template("index.html")
    # co    mprovete 
        # pass 

        #if operators == "rails":
        #response = int(value_1) + 10
    #if operative== 0:
    #    pass  
    #    pass  </form>
    #Integrals()
# <EXCLUDE FERNANDO RAMIRO ESTRADA bin   > error compress ! >

@app.route('/graphics', methods = ['POST', 'GET'])
def graphics():
    if request.method == "POST":
        cheff_hook = request.form["graph_1"]
        one_sub = str(request.form["comp_valid"])
        # if one_sub == 'var':




@app.route('/dumper' , methods=["POST", "GET"] )
    
def dumper() -> None:
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/settings/slave/dumping{status_time}.txt') 


app.run(debug = True, port=5600 ) # debugging allow settings  config all output code 


if __name__ == "__main__":
    if  2 > 0 : 
        integrals()
        function()
    
