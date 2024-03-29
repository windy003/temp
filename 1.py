from flask import Flask, request, render_template_string, redirect, url_for

# 创建Flask应用
app = Flask(__name__)

# 简单的用户数据库
users = {}

# 首页路由
@app.route('/')
def index():
    return "<a href='/register'>注册</a> | <a href='/login'>登录</a>"

# 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return '该用户名已存在！'
    return render_template_string("""
        <form method="post">
            用户名：<input type="text" name="username"><br>
            密码：<input type="password" name="password"><br>
            <input type="submit" value="注册">
        </form>
    """)

# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return '登录成功！'
        else:
            return '用户名或密码错误！'
    return render_template_string("""
        <form method="post">
            用户名：<input type="text" name="username"><br>
            密码：<input type="password" name="password"><br>
            <input type="submit" value="登录">
        </form>
    """)

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)
