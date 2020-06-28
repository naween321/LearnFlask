from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'

db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __str__(self):
        return f'user is {self.name}'


@app.route('/')
@app.route('/home/', methods=['GET', 'POST', ])
def home():
    if request.method == 'POST':
        name = request.form.get('your_name')
        email = request.form.get('email')
        message = request.form.get('message')
        contact = Contact(name=name, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contact_list'))
    return render_template('form.html')


@app.route('/contact-list/')
def contact_list():
    contacts = Contact.query.all()
    return render_template('contact_list.html', contacts=contacts)


if __name__ == '__main__':
    app.run()
