from flask import Flask
from blueprints.v1 import blueprint as distance_teste

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False


app.register_blueprint(distance_teste)

if __name__ == "__main__":
    app.run()
