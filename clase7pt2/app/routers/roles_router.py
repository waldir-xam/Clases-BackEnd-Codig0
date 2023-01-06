from app import api
from flask_restx import Resource

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modelo de Roles',
    path='/roles'
)


@role_ns.route('')
class Roles(Resource):
    def get(self):
        '''Listar todos los archivos'''
        pass

    def post(self):
      '''Creacion del Rol'''
      pass

@role_ns.route('/<int:id>')
class RolesById(Resource):
  def get(self,id):
    '''Obtener un rol por el ID'''
    return {'mesage':f'Role->{id}'}

  def put(self,id):
    '''Actualizar un rol por el ID'''
    pass

  def delete(self,id):
    '''Inhabilitar un rol por el ID'''
    pass



@api.route('/roles/<int:id>')
class RolesById(Resource):
    def get(self, id):
        return {'message': f'Role->{id}'}
