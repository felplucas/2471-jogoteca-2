import os
from dotenv import load_dotenv

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario=os.getenv('DB_USER'),
        senha=os.getenv('DB_PASS'),
        servidor=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME')
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'