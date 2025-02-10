from flask import Flask, request

app = Flask(__name__)

FLAG = "asthra{hey rizzler its skibidi ceaser cipher}"

@app.route("/", methods=["GET", "POST"])
def challenge():
    message = "dvwkur{khb ulccohu lwv vnelgl fhduhu flskhu}"
    
    if request.method == "POST":
        user_input = request.form.get("flag")
        if user_input == FLAG:
            return "✅ Correct! You solved the challenge."
        else:
            return "❌ Wrong flag! Try again."
    
    return f"""
    <h2>Encrypted Message: {message}</h2>
    <form method='post'>
        Enter Flag: <input type='text' name='flag'>
        <input type='submit' value='Submit'>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)