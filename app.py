from flask import Flask, render_template, request
import openai

# Flask App তৈরি
app = Flask(__name__)

# এখানে তোমার OpenAI API Key বসাও
openai.api_key = "YOUR_API_KEY"

@app.route("/")
def home():
    return render_template("index.html", answer=None)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["question"]

    # OpenAI API Call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Mahmud's personal AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
