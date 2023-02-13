from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def prompt():
    prompt = request.form.get("prompt")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

    if __name__ == "__main__":
        app.run()
