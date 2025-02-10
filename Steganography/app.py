from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

correct_flag = "asthra{hidden_in_the_pixels}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_flag = request.form['flag']
    
    if user_flag == correct_flag:
        return jsonify({
            "message": "Correct! Congratulations! You've successfully extracted the flag: " + correct_flag
        })
    else:
        return jsonify({
            "message": "Incorrect flag. Keep analyzing the image and try again!"
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)