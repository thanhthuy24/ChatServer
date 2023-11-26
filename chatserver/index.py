from flask import render_template, request, redirect #chuyển giữa các man hình khác nhau
from chatserver import app, login
import dao
from flask_login import login_user

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
        return render_template('/layout/chat.html')

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    from chatserver import admin
    app.run(debug=True)