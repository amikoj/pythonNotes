#!/usr/bin/env python
# -*-encoding:utf-8-*-

from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import os,sys
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

baseDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    u"""
    最常用的SQLAlchemy列类型
    Integer int 普通整数，一般是 32 位
    SmallInteger int 取值范围小的整数，一般是 16 位
    BigInteger int 或 long 不限制精度的整数
    Float float 浮点数
    Numeric decimal.Decimal 定点数
    String str 变长字符串
    Text str 变长字符串，对较长或不限长度的字符串做了优化
    Unicode unicode 变长 Unicode 字符串
    UnicodeText unicode 变长 Unicode 字符串，对较长或不限长度的字符串做了优化
    Boolean bool 布尔值
    Date datetime.date 日期
    Time datetime.time 时间
    DateTime datetime.datetime 日期和时间
    Interval datetime.timedelta 时间间隔
    Enum str 一组字符串
    PickleType 任何 Python 对象 自动使用 Pickle 序列化
    LargeBinary str 二进制文件


    db.Columen常用参数制定配置选项:
    primary_key 如果设为 True，这列就是表的主键
    unique 如果设为 True，这列不允许出现重复的值
    index 如果设为 True，为这列创建索引，提升查询效率
    nullable 如果设为 True，这列允许使用空值；如果设为 False，这列不允许使用空值
    default 为这列定义默认值


    常用的SQLAlchemy 关系选项
    backref 在关系的另一个模型中添加反向引用
    primaryjoin 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
    lazy 指定如何加载相关记录。可选值有 select（首次访问时按需加载）、immediate（源对象加载后就加载）、joined（加载记录，但使用联结）
                、subquery（立即加载，但使用子查询）， noload（永不加载）和 dynamic（不加载记录，但提供加载记录的查询）
    uselist 如果设为 Fales，不使用列表，而使用标量值
    order_by 指定关系中记录的排序方式
    secondary 指定多对多关系中关系表的名字
    secondaryjoin SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件
    """

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 设置users关联,第一个参数关联模型，若模型类没有定义可以使用字符串代替
    users = db.relationship("User", backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # 设置外键值
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


def connectSql(app):
    u"""
    数据库连接操作,常用sql连接Url结构.
    MySQL mysql://username:password@hostname/database
    Postgres postgresql://username:password@hostname/database
    SQLite（Unix） sqlite:////absolute/path/to/database
    SQLite（Windows） sqlite:///c:/absolute/path/to/database
    :return:
    """

    # 当前的路径
    #
    # print "baseDir:",baseDir






    # db.create_all()
    # admin_role = Role(name="admin")
    # mod_role = Role(name = "Moderator")
    # user_role = Role(name = 'User')
    # user_john = User(username = 'john',role = admin_role)
    # user_susan= User(username = "susan",role = user_role)
    # user_david = User(username = 'david',role = user_role)
    #
    # db.session.add(admin_role)
    # db.session.add(mod_role)
    # db.session.add(user_role)
    # db.session.add(user_john)
    # db.session.add(user_susan)
    # db.session.add(user_david)
    # db.session.commit()
    roles = Role.query.all()
    users = User.query.all()
    # User.query.filter_by(role=user_role).all()
    print str(User.query.filter_by(role = roles[2]))
    print roles[0].name
    print users[0].username
    print users[0].id
    # db.session.rollback() 数据库会话滚动




class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/form',methods = ['GET','POST'])
def formFunc():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data)
        if user:
            session['known'] = True
        else:
            user = User
            session['known'] = False
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name.')
        session['name' ] = form.name.data
        return redirect(url_for('formFunc'))
    return render_template('form.html',form=form,name=session.get('name'))


connectSql(app)
# app.run(debug=True)