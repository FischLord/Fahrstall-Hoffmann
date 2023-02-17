from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hochzeitskutsche')
def hochzeitskutsche():
    return render_template('hochzeitskutsche.html')

@app.route('/ueberUns')
def ueberUns():
    return render_template('ueberUns.html')

@app.route('/termine2023')
def termine2023():
    return render_template('termine2023.html')

@app.route('/kutschfahrten')
def kutschfahrten():
    return render_template('kutschfahrten.html')

@app.route('/fahrsport')
def fahrsport():
    return render_template('fahrsport.html')



if __name__ == '__main__':
    app.run(debug=True)
