from flask import Flask

from blueprints.v1 import blueprint as blueprint_api_v1
from configurations.logger import factory_logger

logger = factory_logger()


def init_api():
    app = Flask(__name__)

    app.config['RESTPLUS_MASK_SWAGGER'] = False

    app.register_blueprint(blueprint_api_v1)
    return app


def main():
    app = init_api()
    app.run(host='0.0.0.0', port=9007)


if __name__ == "__main__":
    main()
