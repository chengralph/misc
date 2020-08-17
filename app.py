from flask import Flask, render_template, url_for, jsonify
from class_deck import deck


random_deck = deck()
random_deck.load_deck()

app = Flask(__name__)

@app.route("/game/play", methods=['GET'])
def play_game():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    index = f'{current_index}/{last_index}'
    return render_template("play.html", card_value=card, index=index)

@app.route("/game/shuffle", methods=['POST'])
def shuffle_deck():
    random_deck.shuffle()
    card, current_index, last_index = random_deck.draw()
    index = f'{current_index}/{last_index}'
    return jsonify({"status":"Shuffled", "value": card, "index": index})

@app.route("/game/draw", methods=["POST"])
def draw_deck():
    card, current_index, last_index = random_deck.draw()
    index = f'{current_index}/{last_index}'
    return jsonify({"status":"Drew", "value": card, "index": index})

@app.route("/game/reverse", methods=["POST"])
def reverse_draw():
    card, current_index, last_index = random_deck.reverse_draw()
    index = f'{current_index}/{last_index}'
    return jsonify({"status":"Reversed", "value": card, "index": index})

if __name__ == "__main__":
    app.run(debug=True)
