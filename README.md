# NumGame API

### Guess the number! 

This is a simple API-accessed number guessing game, built with python and FastAPI.

To play:
1. Start a new game at /newgame/\<your player name\> (optionally add a max range for the secret number, default is 100)
2. Make guesses at /\<your player name\>/\<your guess\>
3. Get the scores at /scores (see sort / order options below)

----

Request | Optional Params | Example Response | Description
|-------------------------|------------------------------------|-------------------------------------|-----------------------|
/newgame/`{{player}}`/ | max : int = 10 | `{"Player": "player", "Range": "1 - 100r", "Message": "New game created"}` | Start a new game
/`{{player}}`/`{{guess}}`/ | none | `{"Player": "player", "Correct": false, "Guesses": 2, "Message": "Too low"}` | Make a guess
/scores | sort_by : str = guesses, order : str = desc | *see below* | Fetch list of recorded scores
/open-games | sort_by : str = player, order : str = asc | *see below* | Fetch list of unfinished games

---

Sample /scores response:
```
[
    {
        "player": "matt",
        "correct": true,
        "total_guesses": 1,
        "guesses": [
            12
        ],
        "number": 12
    },
    {
        "player": "test",
        "correct": true,
        "total_guesses": 3,
        "guesses": [
            50,
            75,
            65
        ],
        "number": 65
    },
    {
        "player": "playername",
        "correct": true,
        "total_guesses": 3,
        "guesses": [
            50,
            50,
            5
        ],
        "number": 5
    }
]
```
