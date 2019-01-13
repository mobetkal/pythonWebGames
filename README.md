# PythonGames

PythonGames is a website, which uses Python language as a games code. Python uses Brython to display games on the screen.

Brython is a library, which replaces Python code into JavaScript. Frontend is made in Angular. Angular is a platform and framework for building client applications in HTML and TypeScript. It is written in TypeScript also. TypeScript is typed language, which is compiled to JavaScript directly. PostgreSQL is used as a object-relation database.

## Using

In our application we have the option to register an account. After doing that we can log in to service. You have a choice to play games, all of them are located in 'Games' tab on the navbar. After the end of each game, website sends a message to the database, which contains our score in the game.
The best scores of each game are located in "Statistics" tab.

This is a demo application, which can be extended by every developer.

## Installation

1. Install python 3.7.x
2. Install PostgreSQL 11
3. Make database entries by executing SQL files in /dbc
4. Run python server by executing backend/startup.sh or backend/startup.bat (regarding your OS)
5. Run frontend of the app by navigating to /frontend and running command "npm install" for instance in the Visual Studio Code app (with project loaded). Next run command "ng serve -o" and the app should open in your default web browser (or can be accessed by going to localhost:4200). Voila!
