from chatserver.models import User
import hashlib
def get_user_by_id(user_id):
    return User.query.get(user_id) #câu truy vấn có nghĩa là: SELECT * FROM USER WHERE ID = 'user_id'
def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()