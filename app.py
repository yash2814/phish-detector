from flask import Flask, render_template, request

app = Flask(__name__)

# Simple demo phishing detector logic
def detect_phishing(email_text):
    email_text = email_text.lower()
    phishing_keywords = ["bank", "password", "verify", "login", "click here", "urgent", "account"]
    score = sum(keyword in email_text for keyword in phishing_keywords)
    
    if score >= 2:
        return "⚠️ This email looks like a Phishing Email!"
    else:
        return "✅ This email looks Legitimate."

# Main route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        email_text = request.form.get("email_text")
        result = detect_phishing(email_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    # Run on localhost, port 80 or default 5000
    app.run(host="0.0.0.0", port=80, debug=True)
