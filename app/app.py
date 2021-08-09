import redis
from sys import stderr
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
Contador = 0

@app.route('/success/<name>/<email>/<passw>')
def success(name, email, passw):
    return 'welcome %s - %s - %s ' % (name, email, passw)

@app.route('/sql', methods=['GET', 'POST'])
def insert_sql():
    if request.method == 'POST':
        connection = mysql.connector.connect(option_files='./connectors.cnf', option_groups='mysqld-8.0.26')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (username, email, pass) VALUES (\"%s\", \"%s\", \"%s\");'
        %(request.form['name'], request.form['email'], request.form['pass']))
        cursor.close()
        connection.commit()
        connection.close()
        return redirect(url_for('hello_world'))
    return redirect(url_for('hello_world'))

@app.route('/redis', methods=['GET', 'POST'])
def insert_redis():
    global Contador
    Contador+=1
    if request.method == 'POST':
        cache.hmset('user:%d'%(Contador),{
            'name': request.form['name'],
            'email': request.form['email'],
            'password': request.form['pass']
        })
        return redirect(url_for('hello_world'))
    return redirect(url_for('hello_world'))

@app.route('/', methods=['GET'])
def hello_world():
    tamanioredis = 0
    tamaniomysql = []
    connection = mysql.connector.connect(option_files='./connectors.cnf', option_groups='mysqld-8.0.26')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM users')
    tamaniomysql = cursor.fetchone()
    cursor.close()
    connection.close()
    tamanioredis = cache.dbsize()
    return render_template('formulario.html', ssql= int(tamaniomysql[0]), scache= int(tamanioredis))