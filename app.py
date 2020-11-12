import chess
import sys
import random
import chess.svg
import train
import chess.pgn
import webbrowser
from flask import Flask, Response, request, render_template, jsonify

#webbrowser.open('http://127.0.0.1:5000/', new=2)

app = Flask(__name__)

board = chess.Board()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move')
def move():

  target = int(request.args.get('to', default=''))
  source = int(request.args.get('from', default=''))  
  move = chess.Move(source, target)

  if move in board.legal_moves:
    board.push(move)
    board.push(random.choice(list(board.legal_moves)))

  print(board)
  reponse = app.response_class(response = board.fen(), status = 200)
  return reponse

@app.route("/newgame")
def newgame():
  board.reset()
  response = app.response_class(
    response = board.fen(),
    status=200
  )
  return response

app.run(debug=True)