#nơi tạo lớp đối tượng - entity class
#lớp entity đại diện cho 1 bảng trên database
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from chatserver import db, app
from flask_login import UserMixin
from sqlalchemy.orm import relationship
#enum là giá trị liệt kê
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    #user thường đăng kí
    #user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib

        # u = User(name='Admin', username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)

        u1 = User(name='Thuy', username='thuyho2411',
                  password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()))
                  # user_role=UserRoleEnum.ADMIN)
        db.session.add(u1)
        db.session.commit()

