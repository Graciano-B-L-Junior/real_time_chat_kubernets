from flask import Flask,request,render_template,url_for,redirect

from db_aux import connect_to_mysql

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        conn = connect_to_mysql()
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE users.username = %s AND users.passphrase = %s",(username,password))
        myresult = cursor.fetchone()
        if myresult == None:
            conn.close()
            return render_template('index.html',error='username or password is wrong!')
        else:
            return redirect(url_for('chat_page'))

@app.route("/signin",methods=['GET', 'POST'])
def sign_in():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        conn = connect_to_mysql()
        username = request.form['username']
        password = request.form['password']
        password_2 = request.form['password_2']
        if password_2 != password:
            return render_template('signin.html',error='passwords are not match!')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, passphrase) VALUES (%s, %s)",(username,password))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

@app.route("/chat",methods=['GET',])
def chat_page():
    return render_template('chat_page.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)