from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user, get_user_profile
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/',methods=['GET'])
def default():
    return 'the app running'
# REGISTER
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = register_user(data.get('name'), data.get('password'))
    return jsonify(response), 201


# LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = login_user(data.get('name'), data.get('password'))

    if isinstance(user, tuple):
        return jsonify(user[0]), user[1]

    token = create_access_token(identity=user['UserName'])

    return jsonify({
        "message": "Login successful",
        "token": token
    })


# PROFILE (Protected)
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()

    user = get_user_profile(current_user)

    return jsonify({"user": user})
