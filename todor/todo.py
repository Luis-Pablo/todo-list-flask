from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix ='/todo')

@bp.route('/list')
def list():
    return "Lista de tareas"

@bp.route('/create')
def create():
    return "Crear un tarea"