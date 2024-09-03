from app import api
from flask_restx import Resource
from app.schemas.roles_schemas import RolesRequestSchema

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modelo de Roles',
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)


@role_ns.route('')
class Roles(Resource):
    def get(self):
        """ Listar todos los roles """
        pass

    @role_ns.expect(request_schema.create(), validate=True)
    def post(self):
        """ Creacion del Rol """
        pass


@role_ns.route('/roles/<int:id>')
class RolesById(Resource):
    def get(self, id):
        """ Obtener un rol por el ID  """
        return {'message': f'Role -> {id}'}

    def put(self, id):
        """ Actualizar un rol por el ID """
        pass

    def delete(self, id):
        """ inhabilitar un rol por el ID """
        pass
