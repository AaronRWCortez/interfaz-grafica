from urllib import request
from flask import Flask
from flask import render_template,redirect,request
import modelo

app= Flask(__name__)

@app.route('/')
def index():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    
    return render_template('empleados/index.html',listado=listado)

@app.route('/ListarPorGenero')
def ListGenero():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    
    return render_template('empleados/index.html',listado=listado)

@app.route('/destroy/<int:cod_album>')
def destroy(cod_album):
    con = modelo.Conectar()
    con.BorrarAlbum(cod_album)
    return redirect('/')

@app.route('/create')
def create():
    i = modelo.Conectar()
    g = modelo.Conectar()
    d = modelo.Conectar()
    f = modelo.Conectar()
    interpretes = i.ListarInterprete()
    generos = g.ListarGenero()
    discograficas = d.ListarDiscografica()
    formatos = f.ListarFormato()
    return render_template('empleados/create.html', interpretes=interpretes, generos=generos, discograficas=discograficas, formatos=formatos)

@app.route('/save-new')
def saveNew():
    _txtCodAlbum=request.form['txtCodAlbum']
    _txtNombre=request.form['txtNombre']
    _IDInterprete=request.form['ID-Interprete']
    _IDGenero=request.form['ID-Genero']
    _txtCantTemas=request.form['txtCantTemas']
    _IDDiscografica=request.form['ID-Discografica']
    _txtFecha=request.form['txtFecha']
    _IDFormato=request.form['ID-Formato']
    _txtPrecio=request.form['txtPrecio']
    _txtPrecio=request.form['txtPrecio']
    _txtCantidad=request.form['txtCantidad']
    
    con = modelo.Conectar()
    album = modelo.Album(0,_txtCodAlbum,_txtNombre,_IDInterprete,_IDGenero,_txtCantTemas,_IDDiscografica,_txtFecha,_IDFormato,_txtPrecio,_txtCantidad,"")
    con.InsertarAlbum(album)

@app.route('/edit/<int:cod_album>')
def edit(cod_album):
    con = modelo.Conectar()
    album = con.ListarAlbum(cod_album)
    interpretes = con.ListarInterprete()
    generos = con.ListarGenero()
    discograficas = con.ListarDiscografica()
    formatos = con.ListarFormato()
    return render_template('empleados/edit.html',album=album, interpretes = interpretes, generos = generos, discograficas = discograficas, formatos = formatos)

if __name__ == '__main__':
    app.run(debug=True)