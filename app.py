from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

appointments = []

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/book-form')
def book_form():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    age = request.form['age']
    date = request.form['date']
    time = request.form['time']
    reason = request.form['reason']

    if not name or not age or not date or not time or not reason:
        flash('All fields are required!')
        return redirect(url_for('book_form'))

    appointment = {
        'name': name,
        'age': age,
        'date': date,
        'time': time,
        'reason': reason
    }
    appointments.append(appointment)
    flash('Appointment booked successfully!')
    return redirect(url_for('appointments_view'))

@app.route('/appointments')
def appointments_view():
    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
