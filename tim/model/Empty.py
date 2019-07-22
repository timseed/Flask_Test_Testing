"""
These Models are used by the Flask Interface to
   1: Limit which fields are to be sent back to the User
   2: Enforce the datatype
   3: Help building the Swagger Api
   4: Used by the Database Module to verify that the field exists in the Database.
You can have less fields in a model than in the
corresponding database table, but You can not have more.
This is shown in the Model...
NOT in the Route.
"""
from flask_restplus import fields
from tim.controller import app

# To use this on a route - the route needs to use this.
# In the route code use this
#     @API.marshal_with(BPKG_MODEL, envelope='resource')
# If the Route has Compulsory params then make the route like this
#     @NS_CONF.route('/ROUTE/<string:name>/phone/<string:phone>')
# Opt arguments (Address) need to be arg parsed.
#     arg_parser = reqparse.RequestParser()
#     arg_parser.add_argument("address", type=str, default="")
#     args = arg_parser.parse_args()

EMPTY_MODEL = app.API.model('empty_model',{})
