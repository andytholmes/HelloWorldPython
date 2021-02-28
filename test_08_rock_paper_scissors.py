import pytest


def rock_paper_scissors(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        return "player 1"
    if player1 == "scissors" and player2 == "rock":
        return "player 2"
    if player1 == "scissors" and player2 == "paper":
        return "player 1"
    if player1 == "paper" and player2 == "scissors":
        return "player 2"
    if player1 == "paper" and player2 == "rock":
        return "player 1"
    if player1 == "rock" and player2 == "paper":
        return "player 2"
    else:
        return "draw"


@pytest.mark.parametrize('player1, player2, expected', [
    ("rock", "scissors", "player 1"),
    ("scissors", "rock", "player 2"),
    ("scissors", "paper", "player 1"),
    ("paper", "scissors", "player 2"),
    ("rock", "paper", "player 2"),
    ("paper", "scissors", "player 2"),
    ("paper", "rock", "player 1"),
    ("rock", "rock", "draw"),
    ("paper", "paper", "draw"),
    ("scissors", "scissors", "draw")
])
def test_rock_paper_scissors(player1, player2, expected):
    # When
    winner = rock_paper_scissors(player1, player2)

    # Then
    assert winner == expected
