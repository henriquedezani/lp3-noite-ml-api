from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# @app.route('/<name>')
# def home(name):
#     return render_template('hello.html', name=name)

@app.route('/')
def home():
    return render_template('hello.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['search']
    # TODO: Usar o modelo de ML já treinado para predizer a resposta.
    # modelo.predict(query)
    return jsonify({
        "query": query,
        "result": "positivo"
    })


if __name__ == '__main__':
    app.run(debug=True)
