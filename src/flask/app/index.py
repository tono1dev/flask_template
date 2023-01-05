from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'PokemonDB'

mysql = MySQL()
mysql.init_app(app)

def sqltest():
    #本体
    sql = 'SELECT * FROM Techniques'
    try:
        cursor = mysql.connect().cursor() 
        cursor.execute(sql)
        rows = cursor.fetchall()

        app.logger.info('select結果')
        for t_rows in rows:
            app.logger.info(t_rows) 
    except Exception as e:
        app.logger.info('エラー')
        app.logger.info(e)

@app.route('/')
def main():
    sqltest()
    props = {'title': 'ポケモンDB', 'msg': 'ポケモンDB'}
    html = render_template('index.html', props=props)
    return html

@app.route('/hello')
def hello():
    props = {'title': 'flask_app - hello', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
  


