from flask import Flask, request, jsonify, render_template
import hashlib
import os

app = Flask(__name__)

# Store password hash - in a real app, this would be in a secure config
password_hash = hashlib.sha256(b"secretpassword").hexdigest()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == password_hash:
        return jsonify({
            "success": True,
            "message": "Correct password!",
            "flag": "CTF{congratulations_you_found_the_flag}"
        })
    else:
        return jsonify({
            "success": False,
            "message": "Incorrect password, try again."
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)