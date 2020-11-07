import chess
import sys
import random
import chess.svg
import train
import chess.pgn
import webbrowser
from flask import Flask, Response, request, render_template

#webbrowser.open('http://127.0.0.1:5000/', new=2)
pgn = open("data/db_1.pgn")
first_game = chess.pgn.read_game(pgn)
board = first_game.board()
img = chess.svg.board(board, size=800)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    








app.run(debug=True)