# Wards and Firewalls

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Database](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)

A two-player, card-based web application game designed to teach the relationships between cyber attacks and cyber defence methodologies through an engaging medieval-fantasy theme. This project was developed as part of an MSc Dissertation.

---

## Table of Contents

- [About The Game](#about-the-game)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Author](#author)

## About The Game

Traditional cybersecurity training often fails to engage non-technical audiences. "Wards and Firewalls" addresses this gap by transforming learning into a competitive, strategic and a partially luck-based game. Two players take on the roles of the **Guard** (the defender) and the **Thief** (the attacker).

- The **Guard** player draws and plays defensive cards to build up the castle's security, manage resources (Gold), and survive for 20 turns.
- The **Thief** player draws and plays attack cards to disrupt the Guard's defenses, steal Gold, and bankrupt the kingdom before the turn limit is reached.

By playing as both attacker and defender, players gain a practical understanding of core cybersecurity concepts and begin to develop **adversarial thinking**. The game abstracts complex topics (e.g., SQL Injection becomes "The Cipherbane") to make them accessible and engaging for beginners.

## Key Features

- **Two-Player Local Gameplay:** Two players can register accounts and play against each other on the same machine
- **Card-Based Mechanics:** A deck of 16 unique Guard cards and 13 unique Thief cards
- **Resource Management:** Both players must manage their "Gold" to play cards and execute actions
- **Integrated Learning:** In-game Multiple-Choice Questions (MCQs) reinforce the concepts behind each card played
- **Persistent Player Stats:** The game tracks user statistics, including win rates, games played, and MCQ accuracy
- **Leaderboard:** A global leaderboard to rank players based on various metrics
- **In-Game Tutorial & Glossary:** A comprehensive tutorial and a glossary of all cards and concepts
- **Thematic Audio & Visuals:** A full suite of medieval-themed graphics and non-copyright music to enhance immersion

## Technology Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript, Jinja2
- **Game Logic:** Pygame (for audio mixer)
- **Data Visualization:** Pandas & Altair (for the statistics page)
- **Database:** SQLite

## Getting Started

Follow these instructions to get a local copy of the project up and running for development and testing purposes.

### Prerequisites

You will need the following software installed on your system:
- [Python (version 3.10+ recommended)](https://www.python.org/downloads/)
- [pip (usually comes with Python)](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [your-repository-url]
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd wards-and-firewalls
    ```
3.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```
5.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
6.  **Run the application:**
    ```sh
    python app.py
    ```
    The application will start, and the database (`game.db`) will be created automatically in the `instance` folder. Open your web browser and navigate to `http://127.0.0.1:5000` to play.

## How to Play

1.  **Register Accounts:** Both players need to register a new account from the main menu.
2.  **Login:** Use the two-player login screen to log in as the Guard (Player 1) and the Thief (Player 2).
3.  **Play the Game:** Follow the on-screen instructions. The game alternates between the Guard's turn and the Thief's turn.
    - **Guard's Objective:** Survive for 20 turns without going bankrupt.
    - **Thief's Objective:** Bankrupt the Guard (reduce their Gold to less than 0) before Turn 20.
4.  **Check Stats:** After a game, visit the "Game Stats" page to see your updated win rates and performance.

## Project Structure

wards-and-firewalls/
├── app.py                  # Main Flask application <br>
├── Guards.py               # Guard card data and class
├── Thieves.py              # Thief card data and class
├── requirements.txt        # Python dependencies
├── instance/
│   └── game.db             # SQLite database file
├── static/
│   ├── css/
│   ├── images/
│   ├── audio/
│   └── fonts/
└── templates/
├── *.html              # All HTML templates
└── tutorial/
└── *.html          # Tutorial pages

## Author

- Sabari Girish Srinivasan