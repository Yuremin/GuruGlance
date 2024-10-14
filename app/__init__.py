from flask import Flask

def create_app():
    app = Flask(__name__)

    # 注册路由
    from .routes import main
    app.register_blueprint(main)

    return app
