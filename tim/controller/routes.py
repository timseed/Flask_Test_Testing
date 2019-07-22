from flask_restplus import Resource

from tim.controller.app import API, NS_CONF
from tim.model.Empty import EMPTY_MODEL

print("Loading routes")


@API.marshal_with(EMPTY_MODEL, envelope='resource')
@NS_CONF.route('/top/')
class RouteTop(Resource):
    """
    Bpackage Versioning Flask Class
    """

    def get(self):
        """

        :return: Running
        """
        return 'Running'


@API.marshal_with(EMPTY_MODEL, envelope='resource')
@NS_CONF.route('/hello/')
class RouteHello(Resource):
    """
    A static Route that will return same expression.
    """
    def get(self):
        """
        :return: 'Hello, World!'
        """
        return 'Hello, World!'
