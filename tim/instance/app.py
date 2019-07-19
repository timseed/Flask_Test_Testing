from tim.instance import create_app
app = create_app()
# Now add the routes
from tim.route import routes
print("In app.py")