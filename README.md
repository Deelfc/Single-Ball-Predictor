# Hand Cricket - Single Ball Predictor

A simple Python script that simulates one ball of hand cricket.

## How It Works

You enter a number from 1 to 6, and the computer randomly generates its own number in the same range.

- If your number **matches** the computer's number → you're **OUT** 🏏
- If the numbers are **different** → your number counts as **runs scored** for that ball

## Running the Script

```bash
python main.py
```

You'll be prompted to enter a number (1-6), and the result will be printed immediately.

## Example

```
Enter a number (1-6): 4
You played: 4
Computer played: 2
Runs scored: 4
Result: 4

Enter a number (1-6): 3
You played: 3
Computer played: 3
OUT! 🏏
Result: out


## Tech Used
- Python 3
- Built-in `random` module

## About

This is a small practice project simulating a single turn of hand cricket, exploring conditional logic, functions, and randomness in Python.

Want me to put this together with your continuous-innings version too, or keep this README specific to just this single-ball script?

yes

Here's a combined README covering both the single-ball predictor and the continuous-innings version:

markdown
# Hand Cricket (Python)

A simple Python simulation of hand cricket, with two versions included.

## How It Works

You enter a number from 1 to 6, and the computer randomly generates its own number in the same range.

- If your number **matches** the computer's number → you're **OUT** 🏏
- If the numbers are **different** → your number counts as **runs scored** for that ball

## Versions

### 1. Single-Ball Predictor
Simulates just one ball. Enter a number, see the result immediately (runs scored or out).

```bash
python single_ball.py
```

**Example:**

Enter a number (1-6): 4
You played: 4
Computer played: 2
Runs scored: 4
Result: 4


### 2. Continuous Innings
Keeps playing ball after ball, tracking your total score, until you get out.

```bash
python innings.py
```

**Example:**

Enter a number (1-6): 5
You: 5 | Computer: 1
Runs scored: 5 | Total Score: 5

Enter a number (1-6): 3
You: 3 | Computer: 3
OUT! Final Score: 8


## Tech Used
- Python 3
- Built-in `random` module

## About

This is a small practice project exploring conditional logic, functions, loops, and randomness in Python through a simple hand cricket simulation.
