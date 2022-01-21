from flask_restful import Resource
from flask import make_response, render_template


class GetHome(Resource):
    """To be used by Flask.add_resource."""
    def get(self):
        """Handle method get of endpoint / """
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)
