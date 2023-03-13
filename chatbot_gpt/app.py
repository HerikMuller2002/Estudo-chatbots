from flask import Flask

app = Flask("app")

@app.route('/command', methods = ['POST'])
def command():
    return "Testando 1 2 3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)