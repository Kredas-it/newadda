from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Register Blueprint
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000,debug=True)
