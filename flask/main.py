from flask import Flask, render_template


app = Flask(import_name=__name__, static_url_path='/',
            static_folder='static', template_folder='templates')


# 添加html访问路由
@app.route('/')
def blog():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()  # 默认设置host:0.0.0.0 port:5000
