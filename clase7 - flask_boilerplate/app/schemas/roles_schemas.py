from flask_restx import fields


class RolesRequestSchema:
    def __init__(self,  namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, max_lenght=80)
        })
