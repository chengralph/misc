from flask import Flask, render_template, url_for, jsonify
from class_deck import deck
import time

random_deck = deck()
random_deck.load_deck()

app = Flask(__name__)

@app.route("/game/play", methods=['GET'])
def play_game():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    return render_template("play.html", card_value=card, current_index=current_index, last_index=last_index)

@app.route("/game/shuffle", methods=['POST'])
def shuffle_deck():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    return jsonify({"status":"Shuffled", "value": card, "index": current_index})

@app.route("/game/draw", methods=["POST"])
def draw_deck():
    card, current_index, last_index = random_deck.draw()
    return jsonify({"status":"Drew", "value": card, "index": current_index})

@app.route("/game/reverse", methods=["POST"])
def reverse_draw():
    card, current_index, last_index = random_deck.reverse_draw()
    return jsonify({"status":"Reversed", "value": card, "index": current_index})

@app.route("/game/nicole", methods=['GET'])
def play_game1():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    return render_template("nicole.html", card_value=card, current_index=current_index, last_index=last_index)

@app.route("/game/test", methods=['GET'])
def play_test():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    return render_template("test.html", card_value=card, current_index=current_index, last_index=last_index)

if __name__ == "__main__":
    app.run(debug=True)
