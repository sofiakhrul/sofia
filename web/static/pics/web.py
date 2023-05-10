import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

def verdict(num):
        try:
            a = int(num)
        except ValueError:
            return 'Введите год!!!'
        if a <=2023:
            return 'Я же просила будущий год!!!'
        b = 0
        for i in range(2, int(a ** 0.5) + 1):
            if (a % i == 0):
                b = b + 1
        if (b <= 0):
            return('Этот год будет простым! :) ')
        else:
            return('Этот год будет непростым.. но вы не расстраивайтесь и не сдавайтесь!')

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/cat')
def cat():
    return flask.render_template(
        'cat.html'
    )


@app.route('/number', methods=['POST', 'GET'])
def number():
    if request.method == 'POST':
        num = request.form.get('number')
        ver = verdict(num)
    else:
        ver = ''

    return flask.render_template(
        'number.html',
        conclusion = ver
    )

'''
@app.route('/anon_game', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param is None:
        name_param="Ошибка"

    return flask.render_template(
        'nubber.html',
        name=name_param,
        method=request.method
    )
'''

if __name__ == '__main__':
   app.run(debug = True)
