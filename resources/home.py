from flask_restful import Resource
from flask import make_response, render_template
from models.event import Event


class GetHome(Resource):
    """To be used by Flask.add_resource."""
    def get(self):
        """Handle method get of endpoint / """
        event = Event()
        result = [(ev.id, ev.event_name) for ev in event.get_all_events()]

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html',
                                             all_events=result,
                                             len_all_events=len(result)), 200, headers)
