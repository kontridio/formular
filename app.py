from flask import Flask, render_template, request
from wtforms import Form, StringField, validators

app = Flask(__name__)

class HodnotaForm(Form):
    test = StringField('Hodnota', [validators.Length(min=4, max=25)])
    prijmeni = StringField('Prijmeni', [validators.Length(min=4, max=25)])


@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/hodnota/<int:id>/<int:data>')
def hodnota(id, data):
    return render_template('hodnota.html', id = id, data = data)

@app.route('/formular', methods=['GET','POST'])
def formular():
    form = HodnotaForm(request.form)
    if request.method == 'POST' and form.validate():
        return form.data["test"]
    return render_template('formular.html', form=form)

@app.route('/tabulka')
def tabulka():
    pole = ["prvek1", "prvek2"]
    dictpole = {"prvek":"1", "object": {"xxx","yyy"}}
    return render_template("tabulka.html", pole = pole, dictpole = dictpole)

if __name__ == '__main__':
    app.run()
