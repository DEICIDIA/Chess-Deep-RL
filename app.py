import chess
import sys
import random
import chess.svg
import train
import chess.pgn
import webbrowser
from flask import Flask, Response, request, render_template, jsonify

webbrowser.open('http://127.0.0.1:5000/', new=2)

app = Flask(__name__)

board = chess.Board()

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/move', methods = ['POST'])
def move():
	jsdata = request.form
	# print(jsdata, file=sys.stderr)
	print('\n')
	res = input(request.form['source'] + request.form['target'])
	move = chess.Move.from_uci(res)
	board.push(move)
	reponse = app.response_class(response = board.fen(), status=200)
	return reponse


app.run(debug=True)