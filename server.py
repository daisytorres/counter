from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "the_key"



@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template("index.html")



@app.route('/add_two')
def add_two():
    session['count'] += 1 
    return redirect('/')
if __name__ == "__main__":
    app.run(debug = True)



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

