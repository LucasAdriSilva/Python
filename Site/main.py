from flask import Flask, render_template
 
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def we():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)