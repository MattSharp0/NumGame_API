from fastapi import FastAPI
from game import Game, load_game, get_game_data


app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello World"}


@app.get('/newgame/{playername}/')
def newgame(playername: str, max: int = 100):
    g = Game(playername=playername, max=max)
    g.save_game()
    return {'Player': playername, 'Range': f'1 - {max}', 'Message': 'New game created'}


@app.get('/{playername}/{guess}/')
def game(playername: str, guess: int):
    save = load_game(playername)
    g = Game(save)
    message = g.check_guess(guess)
    g.save_game()
    return {'Player': playername, 'Correct': g.correct, 'Guesses': len(g.guesses), 'Message': message}


@app.get('/scores')
def sort_scores(sort_by: str = 'guesses', order: str = 'desc'):
    scores = get_game_data()

    if order == 'desc':
        rev = True
    elif order == 'asc':
        rev = False
    if sort_by == 'guesses':
        sort_key = 'total_guesses'
        rev = not rev
    if sort_by == 'player':
        sort_key = 'player'

    return sorted(scores, key=lambda k: k[sort_key], reverse=rev)


@app.get('/open_games')
def get_open_games(sort_by: str = 'player', order: str = 'desc'):
    open_games = get_game_data(completed=False)

    if order == 'desc':
        rev = True
    elif order == 'asc':
        rev = False
    if sort_by == 'guesses':
        sort_key = 'total_guesses'
        rev = not rev
    if sort_by == 'player':
        sort_key = 'player'

    return sorted(open_games, key=lambda k: k[sort_key], reverse=rev)
