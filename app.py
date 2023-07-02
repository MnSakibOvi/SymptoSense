
from flask import Flask, render_template, request
import openai


app = Flask(__name__)


openai.api_key = "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"

messages = [{"role": "system",
             "content": "You are an medical asisstent you will give disease name by user syndromes,you can ask question for insure the disease."}]


@app.route("/")
def home():
    return render_template("index.html")


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    ans = CustomChatGPT(userText)
    return ans


if __name__ == "__main__":
    app.run()
