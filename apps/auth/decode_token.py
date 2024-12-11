import os

import jwt
from dotenv import load_dotenv
from decouple import config

load_dotenv()

def execute(key):
    jwt_decode = None
    print(os.getenv('SECRET_KEY'))

    try:
        jwt_decode = jwt.decode(key, config('SECRET_KEY'), algorithms=['HS256'])

        print(jwt_decode)
    except jwt.ExpiredSignatureError:
        print("Token expirado. Por favor, renueva el token.")
    except jwt.InvalidTokenError:
        print("Token inválido. Verifica la clave secreta o el formato del token.")

    return jwt_decode.get('user_id')
