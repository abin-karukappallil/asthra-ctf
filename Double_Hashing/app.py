from flask import Flask, request, jsonify, render_template
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def create_hashed_password(password):
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    md5_hash = hashlib.md5(sha256_hash.encode()).hexdigest()
    return md5_hash

with open('hashed_password.txt', 'r') as file:
    hashed_password = file.read().strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        user_password = request.form.get('password', '')
        if not user_password:
            return jsonify({
                "message": "Password cannot be empty",
                "status": "error"
            }), 400
        
        user_hashed = create_hashed_password(user_password)
        
        if user_hashed == hashed_password:
            return jsonify({
                "message": "Correct password! Here's the flag: asthra{you_broke_the_hashing_chain}",
                "status": "success"
            })
        else:
            return jsonify({
                "message": "Incorrect password. Try again.",
                "status": "error"
            })
    
    except Exception as e:
        return jsonify({
            "message": "An error occurred while processing your request",
            "status": "error"
        }), 500

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    if not os.path.exists('hashed_password.txt'):
        print("Warning: hashed_password.txt not found. Creating with default password 'admin'")
        default_password = create_hashed_password('admin')
        with open('hashed_password.txt', 'w') as f:
            f.write(default_password)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
#Message: KZ9tA8sFJt