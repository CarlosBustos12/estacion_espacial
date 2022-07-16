from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import base_de_datos as dbase
from naves_espa import Naves

db = dbase.dbConnection()
app = Flask(__name__)

@app.route('/')
def home():
    naves=db['naves']
    navesReceived=naves.find()
    
    return render_template('index.html', naves=navesReceived)

@app.route('/naves', methods=['POST'])
def agregar_nave():
    naves=db['naves']
    nombre=request.form['nombre']
    tipo_de_nave=request.form['tipo_de_nave']
    pais=request.form['pais']
    combustible=request.form['combustible']
    actividad=request.form['actividad']
    peso=request.form['peso']
    if nombre and tipo_de_nave and pais and combustible and actividad and peso:
        nave=Naves(nombre, tipo_de_nave, pais, combustible, actividad, peso)
        naves.insert_one(nave.datos())
        response = jsonify({
            'nombre':nombre,
            'tipo_de_nave':tipo_de_nave,
            'pais':pais,
            'combustible':combustible,
            'actividad':actividad,
            'peso':peso
        })
        return redirect(url_for('home'))
    else:
        return notFound()

@app.route('/agregar_consulta', methods=['POST'])
def agregar_consulta():
    naves=db['naves']
    nombre=request.form['nombre']
    
    
    if nombre:
         
        return naves.find_one({'nombre' : nombre}) and redirect(url_for('home'))
    else:
        return notFound()   

@app.route('/consulta/<string:product_name>')
def consulta(product_name):
    naves=db['naves']
    naves.find_one({'nombre' : product_name})
    return redirect(url_for('home'))

@app.route('/delete/<string:product_name>')
def delete(product_name):
    naves=db['naves']
    naves.delete_one({'nombre' : product_name})
    return redirect(url_for('home'))

@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    naves=db['naves']
    nombre=request.form['nombre']
    tipo_de_nave=request.form['tipo_de_nave']
    pais=request.form['pais']
    combustible=request.form['combustible']
    actividad=request.form['actividad']
    peso=request.form['peso']
    if nombre and tipo_de_nave and pais and combustible and actividad and peso:
        naves.update_one({'nombre' : product_name}, {'$set' : {'nombre' : nombre, 'tipo_de_nave' : tipo_de_nave, 'pais' : pais,'combustible':combustible,'actividad': actividad,'peso':peso}})
        
        return redirect(url_for('home'))
    else:
        return notFound()




@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


    
if __name__ == '__main__':
    app.run(debug=True, port=8000)