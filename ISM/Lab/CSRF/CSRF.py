from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user data (in a real application, this would be stored in a database)
users = {'example@example.com': 'password123'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Check if email exists in users dictionary and if the password matches
    if email in users and users[email] == password:
        # Successful login, redirect to a success page
        return 'Login successful!'
    else:
        # Failed login, render the login page again with the submitted data
        return render_template('login.html', email=email, password=password)

if __name__ == '__main__':
    app.run(debug=True)
