from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Replace with your Groq API Key
client = Groq(
    api_key="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"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI customer support assistant. Answer politely and clearly."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        reply = completion.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run(debug=True)