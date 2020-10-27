import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def __init__(self):
    ''

def initFirebase():
    cred = credentials.Certificate('./module/phat-authen.json')
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://admin-page-6c6c8.firebaseio.com/'})
    return db

if __name__ == '__main__':
    db_ = initFirebase()
    ref = db_.reference('nhanvien')
    ref.set('test2')