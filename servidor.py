from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/registro', methods=['POST'])
def registrar():
    datos = request.json
    usuario = datos.get('usuario')
    contraseña = generate_password_hash(datos.get('contraseña'))
    nuevo_usuario = Usuario(usuario=usuario, contraseña=contraseña)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201

@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    usuario = Usuario.query.filter_by(usuario=datos.get('usuario')).first()
    if usuario and check_password_hash(usuario.contraseña, datos.get('contraseña')):
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    return jsonify({'mensaje': 'Credenciales incorrectas'}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    return render_template('bienvenida.html')

if __name__ == '__main__':
    app.run(debug=True)