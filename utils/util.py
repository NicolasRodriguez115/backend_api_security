from datetime import datetime, timedelta, timezone
import jwt
from flask import jsonify, request 
from functools import wraps 

SECRET_KEY = "super_secret_secrets"

def encode_token(user_id, role):

    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0, hours=1),
        'iat':datetime.now(timezone.utc),
        'sub': user_id,
        'role': role
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"messages":"Token has expired"}),401
            except jwt.InvalidTokenError:
                return jsonify({"messages":"Invalid Token"}),401
            return func(*args, **kwargs)
        else:
            return jsonify({"message":"Token Authorization Required"}), 401
    return wrapper


def user_token_wrapper(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"messages":"Token has expired"}),401
            except jwt.InvalidTokenError:
                return jsonify({"messages":"Invalid Token"}),401
            return func(token_id=payload['sub'],*args, **kwargs) 
        else:
            return jsonify({"message":"Token Authorization Required"}), 401
    return wrapper


def admin_required(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"messages":"Token has expired"}),401
            except jwt.InvalidTokenError:
                return jsonify({"messages":"Invalid Token"}),401
            if payload['role'] == 'Admin':
                return func(*args, **kwargs)
            else:
                return jsonify({"messages":"Admin role required"}), 401
        else:
            return jsonify({"message":"Token Authorization Required"}), 401
    return wrapper