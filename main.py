from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot(
    "Chatterbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not understand',
            'maximum_similarity_threshold': 0.90
        }
    ]
)
trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")


@app.route("/")
def index():
    return render_template("index.html")  # to send context to html


@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return str(english_bot.get_response(user_text))


if __name__ == "__main__":
    app.run(debug=True)



# while True:
#     try:
#         bot_input = english_bot.get_response(input(">> "))
#         print("Bot: ", bot_input)
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break

