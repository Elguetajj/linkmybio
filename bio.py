from flask import Flask, render_template, url_for
import yaml

app = Flask(__name__)

with open('links.yml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)