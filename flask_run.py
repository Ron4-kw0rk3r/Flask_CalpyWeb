#!/usr/bin/python3

# from pydoc import ErrorDuringImport


# from numbers import Integral


# rom re import I


try: 

    import flask
    from brainrsolver import  brainsolver
    from flask import Flask, render_template
    from flask import request
#    from flask import render_template # import function render_template using file
except  ErrorImportModule:
    import flask


########################### 


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
    return render_template("jumper.html", result=awensome)

    # if operations == 'sum':

    # for z in  [ 'sum', 'rest', 'mod', 'divi', 'mult' ]:
    
    #calculator
    # 
    #if operations == 'rails':
    #    return render_template("jumper.html", result=value_4)
    #if  operations  == 'sum':

    #elif operations == 'rest':
    #    return  render_template("jumper.html")
    #elif operations == 'multiply':
    #    return render_template("jumper.html", result=brainsolver(value_1, value_2, operations))
    #elif operations == 'divide':
    #    return render_template("jumper.html", result=brainsolver(value_1, value_2, operations))
        
    #elif  operations  == 'mod':
    #    return render_template("jumper.html", result=brainsolver(value_1, value_2, operations))
    #else:
    #    return render_template("index.html")

        
@app.route('/integrals', methods=["POST"])
def integrals():
    integral_1 = request.form["integral_1"]
    check_comp =  str(request.form['check_comp'])

    if check_comp == 'derivate':
        return  render_template("jumper.html", Integral=integral_1 )
    elif check_comp == 'integral':

        return  render_template("jumper.html", Integral=integral_1 )
    
    else:
        return render_template("index.html")
    # comprovete 
        # pass 

        #if operators == "rails":
        #response = int(value_1) + 10
    #if operative== 0:
    #    pass  
    #    pass  
    #Integrals()

    
    
app.run(debug = True ) # debugging allow settings  config all output code 


if __name__ == "__main__":
    if  2 > 0 : 
        integrals()
        function()
    
