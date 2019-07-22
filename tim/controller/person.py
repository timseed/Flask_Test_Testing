from flask import jsonify
from flask_restplus import Resource, reqparse

from tim.controller.app import API, NS_CONF
from tim.model import PERSON_MODEL


@API.marshal_with(PERSON_MODEL, envelope='resource')
@API.doc(params={'name': 'The B Package Name. This is a Fake data set.',
                 'number': 'Type Version',
                 'address': 'Architecture',
                 })
@NS_CONF.route('/person/<string:name>/number/<string:number>')
class Person(Resource):
    """
    Bpackage Versioning Flask Class
    """

    def get(self, name, number):
        """
        Call the underlying bpkg_dep call - to gather the project requirements.
        :param name: Compulsary  item.
        :param number: Compulsary item.
        :return: Json Data
        """

        # In the Model we have an optional param
        # Address  this is just like command arg parsing
        arg_parser = reqparse.RequestParser()
        arg_parser.add_argument("address", type=str, default="")
        args = arg_parser.parse_args()
        if args.address != "":
            return jsonify({'name': name, "number": number, "status": "Ok", "address": args.address})
        else:
            return jsonify({'name': name, "number": number, "status": "Ok"})
