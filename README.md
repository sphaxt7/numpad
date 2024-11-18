# Numpad Games

#### Video Demo: https://www.youtube.com/watch?v=PPSZz9bxRjA

#### Description:
Numpad Games.

A project i made for the CS50 final project assignment.

Numpad Games is a terminal based game that combines 3 classic games, TicTacToe, MineSweeper, and Schulte.
It's played using a numpad on a 3x3 grid that appears on the terminal. 

This project was my first ever attempt at making a game, it took almost 2 weeks to complete but it was really fun and a great learning experience. 

I split the project into 2 separate files, a main file "project.py" for the main functions, for the starting menus and to choose the settings for each game, And a second file "numpad.py" which contains 3 classes, 1 for each game, it's where i wrote the game logic for each of the 3 games. i felt like using classes would be alot cleaner and better for functionality.

I started by making a simple 20 lines of code for the MineSweeper game, then i kept adding new ideas like a grid instead of using a simple list and removing the numbers from it like i was doing at first. Each time i added something new it opened a rabbit hole that kept me motivated to learn. I wanted to add another game that is similar to MineSweeper in that it can also be played using the numpad since i liked the simplicity of it, which is how i decided on TicTacToe, coming up with the Computer's AI was very challenging at first and looked alot more cryptic than it does now, but the more i learned the shorter it became.
As for the third game, i simply felt like 3 games would be better than 2 so i asked around the discord community and someone suggested Schulte, i learned how it works and created a simpler version on a 3x3 grid that fit in perfectly with the rest of the games.

The project relied on the input() function at first, but i changed it to using the blessed library to capture single key presses. The library also allowed me to use colors and clear the terminal to create a clean board.


Overall, i'm happy with the outcome for my first ever project of this size, and i will continue making games in the future. Thank you to the CS50 staff and community, and to the official Python discord community for all the help and words of encouragement.

