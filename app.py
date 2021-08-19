from flask import Flask
from flask_restx import Api
import py_eureka_client.eureka_client as eureka_client
from flask_cors import CORS
import config

eureka_client.init(eureka_server=config.EUREKA_SERVER,
                   app_name=config.SERVICE_NAME,
                   instance_host=config.SERVICE_HOST,
                   instance_port=config.SERVICE_PORT)

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['JSON_AS_ASCII'] = False  # 한글 사용을 위한 옵션

api = Api(app, title='Yongjun\'s Python Apis', doc='/')

CORS(app)

if __name__ == "__main__":
    app.run(host=config.SERVICE_HOST, port=config.SERVICE_PORT, debug=True)