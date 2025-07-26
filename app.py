from flask import Flask, render_template, request, redirect, url_for, flash, session 
from functools import wraps
from flask_sqlalchemy import SQLAlchemy # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
import pygame
import ast
import random
import math
import os
import pandas as pd # type: ignore
import altair as alt # type: ignore
import Thieves as tf
import Guards as gd

app = Flask(__name__)

pygame.mixer.init()

kingdom_income_msg = ''
guild_income_msg = ''
guard_turn_counter = 1
thief_turn_counter = 1

# Initialising the Thief and Guard characters
guard = gd.Guard()
thief = tf.Thief()

app.config['SECRET_KEY'] = 'CauseImAPunkRockerYesIAm'
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'game.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)  

    stats = db.relationship('PlayerStats', backref='user', uselist=False)

class PlayerStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    total_games_played = db.Column(db.Integer, default=0)
    games_played_as_guard = db.Column(db.Integer, default=0)
    games_played_as_thief = db.Column(db.Integer, default=0)

    total_games_won = db.Column(db.Integer, default=0)
    total_games_won_as_guard = db.Column(db.Integer, default=0)
    total_games_won_as_thief = db.Column(db.Integer, default=0)

    total_win_rate = db.Column(db.Float, default=0.0)
    win_rate_as_guard = db.Column(db.Float, default=0.0)
    win_rate_as_thief = db.Column(db.Float, default=0.0)

    total_answer_accuracy = db.Column(db.Float, default=0.0)
    total_questions_attempted = db.Column(db.Integer, default=0)
    total_right_answers = db.Column(db.Integer, default=0)
    game_right_answers = db.Column(db.Integer, default=0)
    game_total_questions = db.Column(db.Integer, default=0)
    answer_accuracy_in_last_game = db.Column(db.Float, default=0.0)

class GameSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    guard_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thief_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    winning_role = db.Column(db.String(10)) 
    
    final_turn_number = db.Column(db.Integer) 

    guard_mcq_total_questions = db.Column(db.Integer)
    guard_mcq_right_answers = db.Column(db.Integer)
    guard_mcq_accuracy = db.Column(db.Float)

    thief_mcq_total_questions = db.Column(db.Integer)
    thief_mcq_right_answers = db.Column(db.Integer)
    thief_mcq_accuracy = db.Column(db.Float)

    timestamp = db.Column(db.DateTime, default=db.func.now())

    guard_player = db.relationship('User', foreign_keys=[guard_user_id], backref='guard_games')
    thief_player = db.relationship('User', foreign_keys=[thief_user_id], backref='thief_games')
    game_winner = db.relationship('User', foreign_keys=[winner_id], backref='won_games')

def players_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'player1_id' not in session or 'player2_id' not in session:
            flash('Both players must be logged in to play.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

#Card Array Length
guard_card_length = len(gd.guard_protection_header_real_life)
thief_card_length = len(tf.thief_attack_explanation_real_life)
thief_future = False
guard_future = False

guard_total_questions = 0
guard_right_answers = 0
thief_total_questions = 0
thief_right_answers = 0

def kingdom_income():
    income = [0, 5, 10, 15, 20, 25, 40, 60]
    i = random.randint(0, len(income)-1)
    if i == 0:
        kingdom_income_msg = 'The Empire is at war, no funds were sent. Make do with what you have'
    elif i == 1:
        kingdom_income_msg = 'A traitor was discovered! The Empire wants to be careful with funds for the time being'
    elif i == 2:
        kingdom_income_msg = 'It was a below average period of trade for the Empire, this is all they could provide'
    elif i == 3:
        kingdom_income_msg = 'Trade as usual, nothing to be concerned about'
    elif i == 4:
        kingdom_income_msg = 'A foreign trader invested some money into the Empire, luck is on your side'
    elif i == 5:
        kingdom_income_msg = 'What a period of flourishing trade! The Empire is pleased with your efforts'
    elif i == 6:
        kingdom_income_msg = 'It is the birthday of a member of the Emperor\'s family. They have showered you with gifts'
    else:
        kingdom_income_msg = 'The Empire has annexed a region and you were vital in this. Enjoy your rightfully earned reward'
    return [income[i],kingdom_income_msg]


def guild_income():
    income = [0, 2, 8, 10, 20, 25, 30]
    i = random.randint(0, len(income)-1)
    if i == 0:
        guild_income_msg = 'Cursed by the Gods for your crimes! Roam the streets. You couldn\'t even steal a bronze coin'
    elif i == 1:
        guild_income_msg = 'You were mistaken to be a pauper. Some nobleman gave you some spare change'
    elif i == 2:
        guild_income_msg = 'A merchant\'s carriage fell over. You swooped in to pick some coin for yourself'
    elif i == 3:
        guild_income_msg = 'An average day at a cutthroat\'s line of work'
    elif i == 4:
        guild_income_msg = 'Luck seems to favour you. Pity it did not favour the moneylender'
    elif i == 5:
        guild_income_msg = 'Your guild leader broke into the neighbouring kingdom\'s royal vault! ' \
        'He gives you a small cut for your help'
    else:
        guild_income_msg = 'Those rich foreign merchants never saw you coming!'
    return [income[i],guild_income_msg]

def min_cost_return(card_choice):
    min_cost = 0
    if guard.card_headers_medieval[card_choice] == 'Guild of Watchful Scribes':
        #GoWS buy/maintenance is same
        min_cost = guard.card_cost[card_choice] * guard.cost_multiplier

    elif guard.card_headers_medieval[card_choice] == 'Twin Seal Protocol':
        if guard.has_mfa == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier

    elif guard.card_headers_medieval[card_choice] == 'The Whispering Gargoyles':
        if guard.has_ids == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier 

    elif guard.card_headers_medieval[card_choice] == 'The Flaming Battlements':
        if guard.has_firewalls == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier

    elif guard.card_headers_medieval[card_choice] == 'The Town Crier':
        if guard.has_rate_limiting == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier   

    elif guard.card_headers_medieval[card_choice] == 'The Royal Cipher':
        if guard.has_e2ee == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier   

    elif guard.card_headers_medieval[card_choice] == 'The Sewer Tunnels':
        if guard.has_vpn == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier   

    elif guard.card_headers_medieval[card_choice] == 'Iron Gate Lockdown':
        if guard.has_acc_lockout == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier  

    elif guard.card_headers_medieval[card_choice] == 'Code of The Squire':
        if guard.has_lpa == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier   

    elif guard.card_headers_medieval[card_choice] == 'The Sylvan Oracle Snare':
        if guard.has_param_queries == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier  

    elif guard.card_headers_medieval[card_choice] == 'Ink Purification Ritual':
        if guard.has_input_sanitisation == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier   

    elif guard.card_headers_medieval[card_choice] == 'The Walled Districts':
        if guard.has_net_segmentation == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier        

    elif guard.card_headers_medieval[card_choice] == 'The Silver Vanguard':
        if guard.has_https == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier 

    elif guard.card_headers_medieval[card_choice] == 'The Ironbound Doctrine':
        if guard.has_zta == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier  

    elif guard.card_headers_medieval[card_choice] == 'The Hidden Borough':
        if guard.has_offshore_backup == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier    

    elif guard.card_headers_medieval[card_choice] == 'The Dwarven Bastion':
        if guard.has_waf == 0:
            min_cost = guard.card_cost[card_choice] * guard.cost_multiplier
        else:
            min_cost = guard.maintenance_cost[card_choice] * guard.cost_multiplier

    return min_cost    

def reset_game_state():
    global guard, thief, guard_turn_counter, thief_turn_counter
    
    guard = gd.Guard()
    thief = tf.Thief()
    guard_turn_counter = 1
    thief_turn_counter = 1

guard_total_answers = 0
guard_right_answers = 0
thief_total_answers = 0
thief_right_answers = 0

def update_game_stats(guard_id, thief_id, winner_role):
    
    global guard_total_answers, guard_right_answers, thief_total_answers, thief_right_answers
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()
    thief_stats = PlayerStats.query.filter_by(user_id=thief_id).first()

    if not guard_stats or not thief_stats:
        print("Error: Could not find player stats for one or both players.")
        return

    guard_stats.total_games_played += 1
    guard_stats.games_played_as_guard += 1
    thief_stats.total_games_played += 1
    thief_stats.games_played_as_thief += 1

    if winner_role == 'guard':
        guard_stats.total_games_won += 1
        guard_stats.total_games_won_as_guard += 1
    elif winner_role == 'thief':
        thief_stats.total_games_won += 1
        thief_stats.total_games_won_as_thief += 1

    guard_stats.total_questions_attempted += guard_stats.game_total_questions
    guard_stats.total_right_answers += guard_stats.game_right_answers
    if guard_stats.game_total_questions > 0:
        guard_stats.answer_accuracy_in_last_game = round((guard_stats.game_right_answers / guard_stats.game_total_questions) * 100)
    else:
        guard_stats.answer_accuracy_in_last_game = 0

    thief_stats.total_questions_attempted += thief_stats.game_total_questions
    thief_stats.total_right_answers += thief_stats.game_right_answers
    if thief_stats.game_total_questions > 0:
        thief_stats.answer_accuracy_in_last_game = round((thief_stats.game_right_answers / thief_stats.game_total_questions) * 100)
    else:
        thief_stats.answer_accuracy_in_last_game = 0

    new_game_session = GameSession(
        guard_user_id = guard_id,
        thief_user_id = thief_id,
        winner_id = guard_id if winner_role == 'guard' else (thief_id if winner_role == 'thief'else None),
        winning_role = winner_role,
        final_turn_number=guard_turn_counter,
        guard_mcq_total_questions = guard_stats.game_total_questions,
        guard_mcq_right_answers=guard_stats.game_right_answers,
        guard_mcq_accuracy = guard_stats.answer_accuracy_in_last_game,
        thief_mcq_total_questions = thief_stats.game_total_questions,
        thief_mcq_right_answers = thief_stats.game_right_answers,
        thief_mcq_accuracy = thief_stats.answer_accuracy_in_last_game
    )

    db.session.add(new_game_session)

    guard_total_answers = guard_stats.game_total_questions
    guard_right_answers = guard_stats.game_right_answers
    thief_total_answers = thief_stats.game_total_questions
    thief_right_answers = thief_stats.game_right_answers
    
    guard_stats.game_total_questions = 0
    guard_stats.game_right_answers = 0
    thief_stats.game_total_questions = 0
    thief_stats.game_right_answers = 0    

    if guard_stats.total_games_played > 0:
        guard_stats.total_win_rate = round((guard_stats.total_games_won / guard_stats.total_games_played) * 100)
    if guard_stats.games_played_as_guard > 0:
        guard_stats.win_rate_as_guard = round((guard_stats.total_games_won_as_guard / guard_stats.games_played_as_guard) * 100)
    if guard_stats.total_questions_attempted > 0:
        guard_stats.total_answer_accuracy = round((guard_stats.total_right_answers / guard_stats.total_questions_attempted) * 100)

    if thief_stats.total_games_played > 0:
        thief_stats.total_win_rate = round((thief_stats.total_games_won / thief_stats.total_games_played) * 100)
    if thief_stats.games_played_as_thief > 0:
        thief_stats.win_rate_as_thief = round((thief_stats.total_games_won_as_thief / thief_stats.games_played_as_thief) * 100)
    if thief_stats.total_questions_attempted > 0:
        thief_stats.total_answer_accuracy = round((thief_stats.total_right_answers / thief_stats.total_questions_attempted) * 100)

    db.session.commit()

def create_mcq_accuracy_chart(player_name, game_sessions, role_type):
    
    data = []
    for i, game in enumerate(reversed(game_sessions)):
        accuracy = 0.0
        total_questions = 0
        if role_type == 'guard':
            accuracy = game.guard_mcq_accuracy
            total_questions = game.guard_mcq_total_questions
        else: 
            accuracy = game.thief_mcq_accuracy
            total_questions = game.thief_mcq_total_questions
        
        if total_questions is not None and total_questions > 0:
            data.append({'Game Number': i + 1, 'Accuracy': accuracy})
    
    df = pd.DataFrame(data)
    
    if df.empty:
        return None 

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Game Number:O', axis=alt.Axis(title='Game (1 = Most Recent)')),
        y=alt.Y('Accuracy:Q', axis=alt.Axis(title='MCQ Accuracy (%)', format='.1f', tickCount=5), scale=alt.Scale(domain=[0, 100])),
        tooltip=['Game Number', alt.Tooltip('Accuracy', format='.1f')]
    ).properties(
        title=f'{player_name} MCQ Accuracy in Last {len(df)} Games'
    ).interactive()

    return chart.to_json()

def create_game_outcome_chart(player_name, player_user_id, game_sessions, role_type):
    
    outcomes = []
    for game in game_sessions:
        if game.winner_id is None: 
            outcomes.append('Draw')
        elif game.winner_id == player_user_id:
            outcomes.append('Win')
        else:
            outcomes.append('Loss')
    
    if not outcomes:
        return None 

    outcome_counts = pd.Series(outcomes).value_counts().reset_index()
    outcome_counts.columns = ['Outcome', 'Count']

    outcome_order = ['Win', 'Loss', 'Draw'] 

    chart = alt.Chart(outcome_counts).mark_bar().encode(
        x=alt.X('Outcome:N', sort=outcome_order, axis=alt.Axis(title='Game Outcome')),
        y=alt.Y('Count:Q', axis=alt.Axis(title='Number of Games')),
        tooltip=['Outcome', 'Count'],
        color=alt.Color('Outcome:N', scale=alt.Scale(domain=['Win', 'Loss', 'Draw'], range=['green', 'red', 'gray']))
    ).properties(
        title=f'{player_name} Outcomes in Last {len(game_sessions)} Games'
    )

    return chart.to_json()

@app.route("/")
def home():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("static/audio/BreakingTheSiege.mp3")
    pygame.mixer.music.play(-1)
    return render_template("index.html") 

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        knight_username = request.form.get('knight_username')
        knight_password = request.form.get('knight_password')
        rogue_username = request.form.get('rogue_username')
        rogue_password = request.form.get('rogue_password')

        user1 = User.query.filter_by(username=knight_username).first()
        user2 = User.query.filter_by(username=rogue_username).first()

        incorrect_one = False
        incorrect_two = False 

        if not user1 or not check_password_hash(user1.password_hash, knight_password):
            incorrect_one = True

        if not user2 or not check_password_hash(user2.password_hash, rogue_password):
            incorrect_two = True
        
        if incorrect_one and incorrect_two:
            flash('Both credentials are incorrect')
            return redirect(url_for('login'))
        elif incorrect_two:
            flash('Player 2 (Thief) credentials are incorrect')
            return redirect(url_for('login'))
        elif incorrect_one:
            flash('Player 1 (Guard) credentials are incorrect')
            return redirect(url_for('login'))

        session['player1_id'] = user1.id
        session['player2_id'] = user2.id

        return render_template("login_success.html", player1=knight_username, player2=rogue_username)

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose another.')
            return redirect(url_for('register'))

        new_user = User(
            username=username,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256')
        )
        db.session.add(new_user)
        new_stats = PlayerStats(user_id=new_user.id)
        db.session.add(new_stats)
        new_user.stats = new_stats
        db.session.commit()

        return render_template('register_success.html')

    return render_template('register.html')

@app.route("/instructions") 
def instructions():
    return render_template("instructions.html")

@app.route("/instructions2") 
def instructions2():
    return render_template("instructions_2.html")

@app.route("/instructions3") 
def instructions3():
    return render_template("instructions_3.html")

@app.route("/guard_turn")
@players_required
def guard_turn():
    

    if 'player1_id' in session and 'player2_id' in session:

        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/VillageConsort.mp3")
        pygame.mixer.music.play(-1)

        if guard.kingdom_gold < 0:
            
            guard_id = session.get('player1_id')
            thief_id = session.get('player2_id')
            
            update_game_stats(guard_id, thief_id, 'thief')
            
            pygame.mixer.music.stop()
            pygame.mixer.music.load("static/audio/DragonCastle.mp3")
            pygame.mixer.music.play(start=9.0)

            reset_game_state()
            return render_template("guard_game_over.html")
        
        elif guard_turn_counter > 20:
            
            guard_id = session.get('player1_id')
            thief_id = session.get('player2_id')

            update_game_stats(guard_id, thief_id, 'guard')
            
            pygame.mixer.music.stop()
            pygame.mixer.music.load("static/audio/ForTomorrow.mp3")
            pygame.mixer.music.play(start=38.0)   
            
            reset_game_state() 
            return render_template("thief_game_over.html")
    
        else:
            kingdom_turn_income,kingdom_income_msg = kingdom_income()
            guard.kingdom_gold += math.floor(kingdom_turn_income * guard.income_multiplier)
            old_val = guard.income_multiplier
            guard.income_multiplier = 1

            return render_template("guard_menu.html", kingdom_income_msg=kingdom_income_msg,
                                kingdom_turn_income=math.floor(kingdom_turn_income * old_val), guard_turn_counter=guard_turn_counter,
                                total_gold=guard.kingdom_gold, logged_in=True)
    return redirect(url_for('login'))

@app.route("/guard_draws")
def guard_draws():
    global guard_turn_counter
    global guard_future
    
    if guard_future == True:
        guard_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/VillageConsort.mp3")
        pygame.mixer.music.play(-1)
    
    deteriorated = guard.deteriorate()
    guard_turn_counter += 1

    card_choice = random.randint(0, guard_card_length-1)

    guard.card_headers_medieval.append(gd.guard_protection_header_medieval[card_choice])
    guard.card_explanations_medieval.append(gd.guard_protection_explanation_medieval[card_choice])
    guard.card_headers_real_life.append(gd.guard_protection_header_real_life[card_choice])
    guard.card_explanations_real_life.append(gd.guard_protection_explanation_real_life[card_choice])
    guard.card_image.append(gd.guard_image_list[card_choice])
    guard.rl_card_image.append(gd.guard_rl_image_list[card_choice])
    guard.card_cost.append(gd.guard_defence_cost[card_choice])
    guard.maintenance_cost.append(gd.guard_maintenance_cost[card_choice])
                

    return render_template("guard_draws.html", medieval_header=gd.guard_protection_header_medieval[card_choice],
                           medieval_explanation=gd.guard_protection_explanation_medieval[card_choice].replace("\n", "<br>"),
                           img_link=gd.guard_image_list[card_choice], deteriorated=deteriorated)

@app.route("/guard_plays")
def guard_plays():
    global guard_future
    
    if guard_future == True:
        guard_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/VillageConsort.mp3")
        pygame.mixer.music.play(-1)

    card_explanation = [card.replace('\n', '<br>') for card in guard.card_explanations_medieval]
    card_number = list(range(len(card_explanation)))
    zipped_data = list(zip(guard.card_headers_medieval, card_explanation, guard.card_image, card_number))
    
    return render_template("guard_plays.html", data=zipped_data)

@app.route("/guard_play_training", methods=["POST"])
@players_required
def guard_play_training():
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer'] 
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Scribe Training successfully Completed!'
        final_msg = 'Excellent!\nThe Royal Scribe and his assistants have educated the noblemen and guards about thieves all around the Kingdom\nThese guards notice all suspicious townsfolk and alert the guards'
        guard.cost_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()
        
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.scribe_training()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Noblemen and guards were too complacent with their training\nThey remember nothing'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_mfa", methods=["POST"])
@players_required
def guard_play_mfa():
    

    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()
    
    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Twin Seal Protocol successfully Established!'
        final_msg = 'Excellent!\nThe Commander of the Castle has initiated a secret second seal protocol\n All guards and noblemen are let in only on presenting both seals'
        guard.cost_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.twin_sigils()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'There were budgeting issues with the seal production\nThe iron was used to forge weapons instead'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_ids", methods=["POST"])
@players_required
def guard_play_ids():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Gargoyles Activated Successfully!!'
        final_msg = 'Excellent!\nThe King has magically activated the magical Gargoyle statues\nThese statues notice all suspicious townsfolk and alert the guards'
        guard.exfiltration_multiplier = 1
        guard.cost_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.gargoyles()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The King failed to magically activate the magical Gargoyle statues\nHe must remember the Royal Mage\'s training'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_firewall", methods=["POST"])
@players_required
def guard_play_firewall():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Flaming Battlements successfully Activated!'
        final_msg = 'Excellent!\nYou have brought in a Seer to create magical walls of flame that protect the Castle from unwanted threats'
        guard.cost_multiplier = 1
        guard.exfiltration_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.battlements()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Seer has scammed you\nHe created a dummy wall that cannot bother blocking a small chicken'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_rate_limiting", methods=["POST"])
@players_required
def guard_play_rate_limiting():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Town Crier is successfully Hired!'
        final_msg = 'Excellent!\nYou have sought the help of the Town Crier to aid the Castle Guards\n People and Salesmen will now form a proper line and await their turn to enter the Castle'
        guard.cost_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.crier()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Crier has refused to help the gate guards\nHe is swarmed by work for the Kingdom'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_e2ee", methods=["POST"])
@players_required
def guard_play_e2ee():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()
    
    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Royal Cipher Established Successfully!'
        final_msg = 'Excellent!\nYour messages to the neighbouring Fiefdoms are now safe\n Even your messengers won\'t be able to decipher them'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.cipher()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Scribes have failed to come up with a strong Royal Cipher\nYour messages are still written in basic English'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark,heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_vpn", methods=["POST"])
@players_required
def guard_play_vpn():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Sewer Tunnels are Established Successfully!'
        final_msg = 'Excellent!\nYou have dug a secret path through the sewers for messengers and spies to reach the Castle\n The bathhouses won\'t be too happy about this, but the Castle is now safer to approach'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.sewer()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Sewer Tunnels are occupied by Poisonous Cockatrices\nThey remain unfit to be used as a secret passage'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_acc_lockout", methods=["POST"])
@players_required
def guard_play_acc_lockout():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Iron Gate has been successfully Activated!'
        final_msg = 'Excellent!\nYou have installed an iron gate that shields the Castle Walls\n Now, miscreants won\'t be able to bombard the gate and enter the castle'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.iron_gate()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Kingdom\'s Blacksmiths doubt your prowess in handling such a large amount of Iron'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_lpa", methods=["POST"])
@players_required
def guard_play_lpa():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Code of The Squire has been successfully Established!'
        final_msg = 'Excellent!\nYou have established a code that ensures that a person cannot access places that they do not need access to'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.squire()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Council could not agree on a uniform code\nThere were too many discrepancies'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_param_queries", methods=["POST"])
@players_required
def guard_play_param_queries():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Sylvan Oracle Snare has been successfully Activated!'
        final_msg = 'Excellent!The Wood Elves decided to help you protect the Oracle\n Their Sylvan magic protects the Oracle from malicious spells'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.snare()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Elves could not gather their magic near the polluted Oracle'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_input_sanitisation", methods=["POST"])
@players_required
def guard_play_input_sanitisation():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'Ink Purification Ritual has been successfully Established!'
        final_msg = 'Excellent!The Scribes conduct a ritual cleansing the Royal Scrolls\n Malicious spells are now next to useless when applied on these scrolls'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.ink()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Scribes could not purify the ink\nThe ritual has failed'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_net_segmentation", methods=["POST"])
@players_required
def guard_play_net_segmentation():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Walled Districts have been successfully Established!'
        final_msg = 'Excellent!\nThe Town and Castle are now separated into smaller Districts with their own Bailiffs for better governance'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.walls()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'There was not enough stone to build the walls\nNeither could the architects come up with an efficient method to segregate the Town and Castle'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_https", methods=["POST"])
@players_required
def guard_play_https():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Silver Vanguard has been successfully Established!'
        final_msg = 'Excellent!\nThe Messengers are now protected by The Silver Vanguard\n No harm may befall the messengers'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.vanguard()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Silver Vanguard have refused to work\nThey demand more payment for their services'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_zta", methods=["POST"])
@players_required
def guard_play_zta():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Ironbound Doctrine has been successfully Established!'
        final_msg = 'Excellent!\nEveryone is the same before the law!\nNobles, Commonfolk and Guards will be made to prove their identities at random intervals'
        guard.doctrine()
        guard.cost_multiplier = 1
        guard.exfiltration_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.doctrine()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Ironbound Doctrine could not be established\nThe nobles and scribes raised too many concerns\n'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>') 
        heading = False       

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_offshore_backup", methods=["POST"])
@players_required
def guard_play_offshore_backup():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Hidden Borough has been successfully Established!'
        final_msg = 'Excellent!\nThere is now a secret borough hidden in the woods\n It has grains, weapons and medicine to keep the Castle afloat during a crisis\n'
        guard.cost_multiplier = 1
        
        guard_stats.game_right_answers += 1
        db.session.commit()

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.borough()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'There was a forest fire\nMost of the borough and the vital rations were burned down'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_waf", methods=["POST"])
@players_required
def guard_play_waf():
    
    
    guard_id = session.get('player1_id')
    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()    
    guard_stats.game_total_questions += 1
    db.session.commit()

    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    dead = request.form.getlist('deteriorated')
    cleaned_dead = dead[0]
    parsed_dead = ast.literal_eval(cleaned_dead)
    parsed_dead = [item.replace('\n','<br>') for item in parsed_dead]
    print(parsed_dead)
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True

    if right_answer == user_answer:
        usr_msg = 'The Dwarven Bastion have been successfully Established!'
        final_msg = 'Excellent!\nThe strength of the Earth and the strength of the Dwarves are yours\n The inner Castle is now safer against internal threats'
        guard.cost_multiplier = 1

        guard_stats.game_right_answers += 1
        db.session.commit()

        if guard.exfiltration_multiplier == 1.5:
            guard.exfiltration_multiplier == 1.25

        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        guard.bastion()
    else:
        usr_msg = 'Too bad....'
        final_msg = 'The Dwarven Bastion was not awakened\nThe  Dwarves were unable to complete their ritual'
        final_msg = final_msg.replace('\n', '<br>')
        msg_list = final_msg.split('<br>')
        heading = False

    return render_template('guard_play_result.html',usr_msg=usr_msg, final_msg=msg_list,
                            right_answer=right_answer,
                            remark=remark, heading=heading, deteriorated=parsed_dead)

@app.route("/guard_play_result", methods=["POST"])
def guard_play_result():

    global guard_turn_counter
    global guard_future
    
    if guard_future == True:
        guard_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/VillageConsort.mp3")
        pygame.mixer.music.play(-1)

    card_choice = int(request.form['number'])
    upgrade_cost = min_cost_return(card_choice)                                                                                             
    success_msg = ''

    if guard.kingdom_gold < upgrade_cost:
        return render_template("guard_play_flop.html")
    
    else: 

        guard_turn_counter +=  1
        deteriorated = guard.deteriorate()
        card_title = guard.card_headers_medieval[card_choice]
        guard.kingdom_gold -= upgrade_cost

        del guard.card_headers_medieval[card_choice]
        del guard.card_explanations_medieval[card_choice]
        del guard.card_headers_real_life[card_choice]
        del guard.card_explanations_real_life[card_choice]
        del guard.card_cost[card_choice]
        del guard.maintenance_cost[card_choice]
        del guard.card_image[card_choice]
        del guard.rl_card_image[card_choice]

        if card_title == 'Guild of Watchful Scribes':

            path = '/guard_play_training'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.training_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.training_answers[question], right_answer=gd.training_answers[question][gd.training_answer_key[question]],
                                   remark=gd.training_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

        elif card_title == 'Twin Seal Protocol':
            
            path = '/guard_play_mfa'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.mfa_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.mfa_answers[question], right_answer=gd.mfa_answers[question][gd.mfa_answer_key[question]],
                                   remark=gd.mfa_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

        elif card_title == 'The Whispering Gargoyles':
            
            path = '/guard_play_ids'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.ids_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.ids_answers[question], right_answer=gd.ids_answers[question][gd.ids_answer_key[question]],
                                   remark=gd.ids_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)
            

        elif card_title == 'The Flaming Battlements':

            path = '/guard_play_firewall'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.firewall_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.firewall_answers[question], right_answer=gd.firewall_answers[question][gd.firewall_answer_key[question]],
                                   remark=gd.firewall_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

        elif card_title == 'The Town Crier':
            
            path = '/guard_play_rate_limiting'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.rate_limiting_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.rate_limiting_answers[question], right_answer=gd.rate_limiting_answers[question][gd.rate_limiting_answer_key[question]],
                                   remark=gd.rate_limiting_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)         

        elif card_title == 'The Royal Cipher':
            
            path = '/guard_play_e2ee'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.e2ee_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.e2ee_answers[question], right_answer=gd.e2ee_answers[question][gd.e2ee_answer_key[question]],
                                   remark=gd.e2ee_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated) 

        elif card_title == 'The Sewer Tunnels':
            
            path = '/guard_play_vpn'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.vpn_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.vpn_answers[question], right_answer=gd.vpn_answers[question][gd.vpn_answer_key[question]],
                                   remark=gd.vpn_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)    

        elif card_title == 'Iron Gate Lockdown':

            path = '/guard_play_acc_lockout'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.acc_lockout_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.acc_lockout_answers[question], right_answer=gd.acc_lockout_answers[question][gd.acc_lockout_answer_key[question]],
                                   remark=gd.acc_lockout_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)   

        elif card_title == 'Code of The Squire':
            
            path = '/guard_play_lpa'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.lpa_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.lpa_answers[question], right_answer=gd.lpa_answers[question][gd.lpa_answer_key[question]],
                                   remark=gd.lpa_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)  

        elif card_title == 'The Sylvan Oracle Snare':

            path = '/guard_play_param_queries'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.param_queries_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.param_queries_answers[question], right_answer=gd.param_queries_answers[question][gd.param_queries_answer_key[question]],
                                   remark=gd.param_queries_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated) 

        elif card_title == 'Ink Purification Ritual':
            
            path = '/guard_play_input_sanitisation'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.input_sanitisation_questions[question].replace('\n', '<br>'), 
                                   list_of_answers=gd.input_sanitisation_answers[question], right_answer=gd.input_sanitisation_answers[question][gd.input_sanitisation_answer_key[question]],
                                   remark=gd.input_sanitisation_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)    

        elif card_title == 'The Walled Districts':
            
            path = '/guard_play_net_segmentation'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.net_segmentation_questions[question].replace('\n', '<br>'),
                                   list_of_answers=gd.net_segmentation_answers[question], right_answer=gd.net_segmentation_answers[question][gd.net_segmentation_answer_key[question]],
                                   remark=gd.net_segmentation_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)       

        elif card_title == 'The Silver Vanguard':
            
            path = '/guard_play_https'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.https_questions[question].replace('\n', '<br>'),
                                   list_of_answers=gd.https_answers[question], right_answer=gd.https_answers[question][gd.https_answer_key[question]],
                                   remark=gd.https_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

        elif card_title == 'The Ironbound Doctrine':
            
            path = '/guard_play_zta'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.zta_questions[question].replace('\n', '<br>'),
                                   list_of_answers=gd.zta_answers[question], right_answer=gd.zta_answers[question][gd.zta_answer_key[question]],
                                   remark=gd.zta_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

        elif card_title == 'The Hidden Borough':
            
            path = '/guard_play_offshore_backup'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.offshore_backup_questions[question].replace('\n', '<br>'),
                                   list_of_answers=gd.offshore_backup_answers[question], right_answer=gd.offshore_backup_answers[question][gd.offshore_backup_answer_key[question]],
                                   remark=gd.offshore_backup_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)
                

        elif card_title == 'The Dwarven Bastion':

            path = '/guard_play_waf'
            question = random.randint(0, 5)
            return render_template('guard_plays_mcq.html',card_title = card_title, question=gd.waf_questions[question].replace('\n', '<br>'),
                                   list_of_answers=gd.waf_answers[question], right_answer=gd.waf_answers[question][gd.waf_answer_key[question]],
                                   remark=gd.waf_q_response[question].replace('\n', '<br>'), path=path, deteriorated=deteriorated)

@app.route("/guard_card_explanation")
def guard_card_explanation():

    global guard_future
    
    guard_future = True
    empty = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load("static/audio/WhiteHole.mp3")
    pygame.mixer.music.play(-1)

    if len(guard.card_headers_medieval) == 0:
        empty = True

    real_life_explanation = [exp.replace('\n', '<br>') for exp in guard.card_explanations_real_life]
    zipped_data = list(zip(guard.card_headers_medieval, guard.card_headers_real_life, 
                      real_life_explanation, guard.rl_card_image))
    return render_template("guard_card_explanation.html", data=zipped_data, empty=empty)

@app.route("/guard_countdown")
def guard_countdown():

    global guard_future

    if guard_future == True:
        guard_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/VillageConsort.mp3")
        pygame.mixer.music.play(-1)

    titles_and_attrs = [
        ("Guild of Watchful Scribes", "has_training"),
        ("Twin Seal Protocol", "has_mfa"),
        ("The Whispering Gargoyles", "has_ids"),
        ("The Flaming Battlements", "has_firewalls"),
        ("The Town Crier", "has_rate_limiting"),
        ("The Royal Cipher", "has_e2ee"),
        ("The Sewer Tunnels", "has_vpn"),
        ("Iron Gate Lockdown", "has_acc_lockout"),
        ("Code of The Squire", "has_lpa"),
        ("Sylvan Oracle Snare", "has_param_queries"),
        ("Ink Purification Ritual", "has_input_sanitisation"),
        ("The Walled Districts", "has_net_segmentation"),
        ("The Silver Vanguard", "has_https"),
        ("The Ironbound Doctrine", "has_zta"),
        ("The Hidden Borough", "has_offshore_backup"),
        ("The Dwarven Bastion", "has_waf")
    ]
    
    active_cards = []
    countdown = []
    empty_message = ''

    for title, attr in titles_and_attrs:
        value = getattr(guard, attr, 0)
        if value > 0:
            active_cards.append(title)
            countdown.append(value)
    
    if len(active_cards) == 0:
        empty_message = "No upgrades are active yet, the castle is vulnerable!!"

    zipped_data = zip(active_cards, countdown)
    return render_template("guard_countdown.html",data=zipped_data, empty_message=empty_message,
                           cost=guard.cost_multiplier, exfil=guard.exfiltration_multiplier)

@app.route("/thief_turn")
def thief_turn():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("static/audio/BattleOfTheCreek.mp3")
    pygame.mixer.music.play(start=60.0)
    pygame.mixer.music.play(-1)

    if thief.extreme_wounds > 0:
        global thief_turn_counter

        thief.deteriorate()
        thief_turn_counter += 1
        
        thief.extreme_wounds -= 1
        guild_turn_income,guild_income_msg = guild_income()
        thief.guild_gold += guild_turn_income
        return render_template("thief_turn_skip.html", extreme_wounds=thief.extreme_wounds)
    
    else:
        guild_turn_income,guild_income_msg = guild_income()
        thief.guild_gold += guild_turn_income

        return render_template("thief_menu.html", guild_income_msg=guild_income_msg,
                            guild_turn_income=guild_turn_income, thief_turn_counter=thief_turn_counter,
                            total_gold=thief.guild_gold)

@app.route("/thief_draws")
def thief_draws():

    global thief_future
    if thief_future == True:
        thief_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/BattleOfTheCreek.mp3")
        pygame.mixer.music.play(start=60.0)
        pygame.mixer.music.play(-1)

    global thief_turn_counter

    thief.deteriorate()
    thief_turn_counter += 1

    card_choice = random.randint(0, thief_card_length-1)

    thief.card_headers_medieval.append(tf.thief_attack_header_medieval[card_choice])
    thief.card_explanations_medieval.append(tf.thief_attack_explanation_medieval[card_choice])
    thief.card_headers_real_life.append(tf.thief_attack_header_real_life[card_choice])
    thief.card_explanations_real_life.append(tf.thief_attack_explanation_real_life[card_choice])
    thief.card_img.append(tf.thief_image_list[card_choice])
    thief.rl_card_img.append(tf.thief_rl_image_list[card_choice])
    thief.card_cost.append(tf.thief_attack_cost[card_choice])

    return render_template("thief_draws.html", medieval_header=tf.thief_attack_header_medieval[card_choice],
                           medieval_explanation=tf.thief_attack_explanation_medieval[card_choice].replace("\n", "<br>"),
                           img_link=tf.thief_image_list[card_choice])

@app.route("/thief_plays")
def thief_plays():

    global thief_future
    if thief_future == True:
        thief_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/BattleOfTheCreek.mp3")
        pygame.mixer.music.play(start=60.0)
        pygame.mixer.music.play(-1)

    card_explanation = [card.replace('\n', '<br>') for card in thief.card_explanations_medieval]
    card_number = list(range(len(card_explanation)))
    zipped_data = list(zip(thief.card_headers_medieval, card_explanation, thief.card_img, card_number))
    return render_template("thief_plays.html", data=zipped_data)

@app.route("/thief_play_result", methods=["POST"])
def thief_play_result():
    
    global thief_turn_counter
    card_choice = int(request.form['number'])
    upgrade_cost = thief.card_cost[card_choice]                                                                                            
    guards_defenses = []
    min_roll = 1    

    if thief.guild_gold < upgrade_cost:
        return render_template("thief_play_flop.html")
    
    else:
        thief_turn_counter += 1
        if thief.card_headers_medieval[card_choice] == 'Snake Oil Salesman':
            thief.guild_gold -= 5
            if guard.has_training > 0 and guard.has_mfa > 0:
                min_roll = 20
                guards_defenses.append('Guild of Watchful Scribes')
                guards_defenses.append('Twin Seal Protocol')
            elif guard.has_training: 
                min_roll = 17
                guards_defenses.append('Guild of Watchful Scribes')   
            else:
                min_roll = 11    

        elif thief.card_headers_medieval[card_choice] == 'Alehouse Swindler':
            thief.guild_gold -= 8 
            if guard.has_training > 0 and guard.has_mfa > 0:
                min_roll = 20
                guards_defenses.append('Guild of Watchful Scribes')
                guards_defenses.append('Twin Seal Protocol')
            elif guard.has_training: 
                min_roll = 17
                guards_defenses.append('Guild of Watchful Scribes')   
            else:
                min_roll = 6  

        elif thief.card_headers_medieval[card_choice] == 'Loosened Castle Walls':
            thief.guild_gold -= 10 
            has_one = False
            
            if guard.has_ids > 0:
                min_roll = 12
                has_one = True
                guards_defenses.append('The Whispering Gargoyles')
            
            if guard.has_firewalls > 0:
                min_roll = 12
                has_one = True
                guards_defenses.append('The Flaming Battlements')
            
            if guard.has_zta > 0:
                min_roll = 12
                has_one = True
                guards_defenses.append('The Ironbound Doctrine')         
            
            if not has_one:
                min_roll = 7         

        elif thief.card_headers_medieval[card_choice] == 'Clatter of Brats':
            thief.guild_gold -= 12
            max_up = False

            if guard.has_rate_limiting > 0:
                min_roll = 20
                max_up = True
                guards_defenses.append('The Town Crier')
            else:   
                if guard.has_firewalls > 0:
                    if not max_up:
                        min_roll = 12
                        max_up = True
                    guards_defenses.append('The Flaming Battlements')
                if guard.has_waf > 0:
                    if not max_up:
                        min_roll = 12
                        max_up = True
                    guards_defenses.append('The Dwarven Bastion')
                if guard.has_net_segmentation > 0:
                    if not max_up:
                        min_roll = 12
                        max_up = True
                    guards_defenses.append('The Walled Districts')
                if guard.has_ids > 0:
                    if not max_up:
                        min_roll = 8
                        max_up = True
                    guards_defenses.append('The Whispering Gargoyles')
                if guard.has_zta > 0:
                    if not max_up:
                        min_roll = 8
                        max_up = True
                    guards_defenses.append('The Ironbound Doctrine')                

        elif thief.card_headers_medieval[card_choice] == 'The Ratcaller of Elwood':
            thief.guild_gold -= 20
            
            if guard.has_training > 0:
                min_roll = 8
                guards_defenses.append('Guild of Watchful Scribes')
            if guard.has_ids > 0:
                min_roll = 12
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_zta > 0:
                min_roll = 12
                guards_defenses.append('The Ironbound Doctrine')   
            if guard.has_firewalls > 0:
                min_roll = 12
                guards_defenses.append('The Flaming Battlements')
            if guard.has_lpa > 0:
                min_roll = 12
                guards_defenses.append('Code of the Squire')   
            if guard.has_net_segmentation > 0:
                min_roll = 16
                guards_defenses.append('The Walled Districts')   
            if guard.has_offshore_backup > 0:
                min_roll = 20
                guards_defenses.append('The Hidden Borough')                 
        
        elif thief.card_headers_medieval[card_choice] == 'Whispering Knaves':
            thief.guild_gold -= 22
            min_roll = 8

            if guard.has_https > 0:
                min_roll = 20
                guards_defenses.append('The Silver Vanguard')
            if guard.has_e2ee > 0:
                min_roll = 20
                guards_defenses.append('The Royal Cipher')
            if guard.has_vpn > 0:
                min_roll = 20
                guards_defenses.append('The Sewer Tunnels')        
        
        elif thief.card_headers_medieval[card_choice] == 'Brigands and Bandits':
            thief.guild_gold -= 20
            
            if thief.has_access:
                min_roll = 8
            else:
                min_roll = 12

            if guard.has_mfa > 0:
                min_roll = 16
                guards_defenses.append('Twin Seal Protocol')
            if guard.has_rate_limiting > 0:
                min_roll = 16
                guards_defenses.append('The Town Crier')
            if guard.has_ids > 0:
                min_roll = 16
                guards_defenses.append('The Whispering Gargoyles')
            if guard.has_zta > 0:
                min_roll = 16
                guards_defenses.append('The Ironbound Doctrine')
            if guard.has_firewalls > 0:
                min_roll = 16
                guards_defenses.append('The Flaming Battlements')
            if guard.has_acc_lockout > 0:
                min_roll = 20
                guards_defenses.append('Iron Gate Lockdown')                     

        elif thief.card_headers_medieval[card_choice] == 'Rags to Riches':
            thief.guild_gold -= 25
            min_roll = 8

            if guard.has_ids > 0:
                min_roll = 16
                guards_defenses.append('The Whispering Gargoyles')
            if guard.has_mfa > 0:
                min_roll = 16
                guards_defenses.append('Twin Seal Protocol')
            if guard.has_firewalls > 0:
                min_roll = 16
                guards_defenses.append('The Flaming Battlements')
            if guard.has_zta > 0:
                min_roll = 19
                guards_defenses.append('The Ironbound Doctrine') 
            if guard.has_lpa > 0:
                min_roll = 19
                guards_defenses.append('Code of The Squire')
            if guard.has_net_segmentation > 0:
                min_roll = 19
                guards_defenses.append('The Walled Districts')           

        elif thief.card_headers_medieval[card_choice] == 'The Cipherbane':
            thief.guild_gold -= 30

            if guard.has_input_sanitisation > 0:
                min_roll = 14
                guards_defenses.append('Ink Purification Ritual')
            if guard.has_waf > 0:
                min_roll = 14
                guards_defenses.append('The Dwarven Bastion')
            if guard.has_ids > 0:
                min_roll = 14
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_zta > 0:
                min_roll = 14
                guards_defenses.append('The Ironbound Doctrine')  
            if guard.has_param_queries > 0:
                min_roll = 20
                guards_defenses.append('The Sylvan Oracle Snare') 

        elif thief.card_headers_medieval[card_choice] == 'Poisoned Scroll':
            thief.guild_gold -= 35 
            min_roll = 8

            if guard.has_ids > 0:
                min_roll = 14
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_zta > 0:
                min_roll = 14
                guards_defenses.append('The Ironbound Doctrine')
            if guard.has_waf > 0:
                min_roll = 14
                guards_defenses.append('The Dwarven Bastion')
            if guard.has_input_sanitisation > 0:
                min_roll = 19
                guards_defenses.append('Ink Purification Ritual')        

        elif thief.card_headers_medieval[card_choice] == 'Blade of the Doppelganger':
            thief.guild_gold -= 40  

            if guard.has_ids > 0:
                min_roll = 13
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_zta > 0:
                min_roll = 13
                guards_defenses.append('The Ironbound Doctrine')  
            if guard.has_mfa > 0:
                min_roll = 13
                guards_defenses.append('Twin Seal Protocol') 
            if guard.has_vpn > 0:
                min_roll = 13
                guards_defenses.append('The Sewer Tunnels')
            if guard.has_training:
                min_roll = 17
                guards_defenses.append('Guild of Watchful Scribes')
            if guard.has_https:
                min_roll = 20
                guards_defenses.append('The Silver Vanguard')  

        elif thief.card_headers_medieval[card_choice] == 'Grains of Malice': 
            thief.guild_gold -= 45
            min_roll = 7

            if guard.has_firewalls > 0:
                min_roll = 13
                guards_defenses.append('The Flaming Battlements') 
            if guard.has_waf > 0:
                min_roll = 13
                guards_defenses.append('The Dwarven Bastion')
            if guard.has_ids > 0:
                min_roll = 17
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_net_segmentation > 0:
                min_roll = 17
                guards_defenses.append('The Walled Districts')     
            if guard.has_zta > 0:
                min_roll = 20
                guards_defenses.append('The Ironbound Doctrine')

        elif thief.card_headers_medieval[card_choice] == 'The Mourning Blightweaver': 
            thief.guild_gold -= 50

            if guard.has_waf > 0:
                min_roll = 13
                guards_defenses.append('The Dwarven Bastion') 
            if guard.has_training > 0:
                min_roll = 13
                guards_defenses.append('Guild of Watchful Scribes')
            if guard.has_firewalls > 0:
                min_roll = 17
                guards_defenses.append('The Flaming Battlements')    
            if guard.has_ids > 0:
                min_roll = 17
                guards_defenses.append('The Whispering Gargoyles') 
            if guard.has_zta > 0:
                min_roll = 17
                guards_defenses.append('The Ironbound Doctrine') 
            if guard.has_net_segmentation > 0:
                min_roll = 20
                guards_defenses.append('The Walled Districts')       
                           



        card_name = thief.card_headers_medieval[card_choice]

        del thief.card_headers_medieval[card_choice]
        del thief.card_explanations_medieval[card_choice]
        del thief.card_headers_real_life[card_choice]
        del thief.card_explanations_real_life[card_choice]
        del thief.card_cost[card_choice]
        del thief.card_img[card_choice]
        del thief.rl_card_img[card_choice]

        return render_template("thief_play_result.html",defenses=guards_defenses,min_roll=min_roll,
                               card_name=card_name)
    
@app.route("/roll_d20", methods=["POST"])  
def roll_d20():
    min_roll = int(request.form.get('min_roll'))
    card_name = request.form.get('card_name')
    roll = random.randint(1, 20)
    res_msg = ''
    attack_success = False
    idiot = False

    if card_name == 'Snake Oil Salesman':

        if thief.phishing_countdown > 0:
            res_msg = 'Welp...didn\'t I warn you before?\nYour salesman ran away again and you can\'t use him or the drunkard for 2 MORE turns'
            thief.phishing_countdown += 2
            idiot = True
        elif roll < min_roll:
            res_msg = 'Darn it! Your salesman was caught!\nLuckily, he got away but the guards and noblemen are far more wary now...\nYou can\'t use him or the drunkard for 2 turns'
            thief.phishing_countdown += 2
        else:
            res_msg = 'Success!!! That scallywag managed to trick some fool!\n You now have access to the castle!'
            attack_success = True

    elif card_name == 'Alehouse Swindler':

        if thief.phishing_countdown > 0:
            res_msg = 'Welp...didn\'t I warn you before?\nYour drunkard ran away again and you can\'t use him or the drunkard for 2 MORE turns'
            thief.phishing_countdown += 2
            idiot = True
        elif roll < min_roll:
            res_msg = 'Darn it! Your drunkard was caught!\nLuckily, he got away but the guards and noblemen are far more wary now...\nYou can\'t use him or the drunkard for 2 turns'
            thief.phishing_countdown += 2
        else:
            res_msg = 'Success!!! That drunkard managed to trick some fool!\n You now have access to the castle!'
            attack_success = True        

    elif card_name == 'Loosened Castle Walls':

        if not thief.has_access:
             res_msg = 'You do not have access to the Castle!\nYou caused a lot of noise from outside the castle\n You can\'t play this card for 5 turns'
             thief.walls_countdown += 5
        else:
            if thief.walls_countdown > 0:
                res_msg = 'The loosened rocks worsen! You cannot use this card for 5 MORE turns'
                thief.walls_countdown += 5
                idiot = True
            elif roll <  min_roll:
                res_msg = 'Oof, you tried too hard and caused a LOT of noise! The guards have noticed this \nYou can\'t play this card for 5 turns'
                thief.walls_countdown += 5
            else:
                res_msg = 'Success!!!\n You managed to break a few rocks in a decrepit castle wall.\nYou now have access to the castle!\nYou now steal 50% more Gold'  
                attack_success = True
    
    elif card_name == 'Clatter of Brats':
        if roll < min_roll:
            res_msg = 'Nope! The children scattered away and scammed you instead!\nWell well well, how the tables turn...'
        else:
            res_msg = "Success!! Those little brats annoyed the guards and the travelling salesmen!\nThe Kingdom earns only 20% of the intended Gold in the next turn!"
            attack_success = True    

    elif card_name == 'The Ratcaller of Elwood':
        if thief.ratcaller_countdown > 0:
            res_msg = 'Well?? What else did you expect from the wounded Ratcaller? \nHe is now in recovery, and can\'t be called for 5 MORE turns...'
            idiot = True
            thief.ratcaller_countdown += 5
        elif roll < min_roll:
            res_msg = 'You bottled it! The Ratcaller was spotted and beaten up by those annoying Guards!\nHe is now in recovery, and can\'t be called for 5 turns...'    
            thief.ratcaller_countdown += 5
        else:
            res_msg = f'Success!! The Ratcaller of Elwood managed to ransack the Castle\'s granary!\nThe Kingdom loses {200 * guard.exfiltration_multiplier} Gold to your ransom!\nThe Kingdom earns only 25% of its intended Gold in the next turn!'
            attack_success = True    

    elif card_name == 'Whispering Knaves':
        if thief.knaves_countdown > 0:
            res_msg = 'Well?? What else did you expect from the wounded Knave? \nThey are still in recovery, and can\'t be called for 5 MORE turns...'
            idiot = True
            thief.knaves_countdown += 5
        elif roll < min_roll:
            res_msg = 'You bottled it! Your Knaves were spotted and beaten up by those annoying Guards!\nThey are now hiding in the dense forest, and can\'t be called for 5 turns...'  
            thief.knaves_countdown += 5
        else:
            res_msg = f'Success!! The Knaves managed to decipher and rephrase the Castle\'s message! \nThe Knaves additionally stole {20 * guard.exfiltration_multiplier} Gold from the Messenger! \nThe Kingdom earns 60% of its intended Gold in the next turn!'
            attack_success = True    

    elif card_name == 'Brigands and Bandits':
        if thief.bnb_countdown > 0:
            res_msg = 'They did NOT forget the last incident \nThe Brigands and Bandits steal ALL of your Gold once again and wound you\nYou are seriously wounded and you lose 2 turns \nBrigands and Bandits may not be played for 15 MORE turns'
            thief.bnb_countdown += 15
            thief.guild_gold = 0
            thief.extreme_wounds += 2
            idiot = True
        elif thief.weaknesses_found == 0:
            res_msg = 'What did you expect when you go there with no information?\nThe Brigands and Bandits steal ALL of your Gold once again and wound you\nYou are seriously wounded and you lose 2 turns \nBrigands and Bandits may not be played for 15 MORE turns'
            thief.bnb_countdown += 15
            thief.guild_gold = 0
            thief.extreme_wounds += 2 
        elif roll < min_roll:
            res_msg = 'Fresh meat is in the House, and YOU are the entree!\nThe Brigands and Bandits are humiliated by the Guards\nIn retaliation, they wound you and steal ALL of your Gold \nYour wounds are severe and cannot move for 2 turns \nYou are now wanted by the Brigands and Bandits and the card may not be played for 15 turns'
            thief.bnb_countdown += 15
            thief.guild_gold = 0
            thief.extreme_wounds += 2
        else:
            if thief.weaknesses_found == 1:
                thief.guild_gold += 5
            elif thief.weaknesses_found <= 3:
                thief.guild_gold += 15
            else:
                thief.guild_gold += 30

            thief.weaknesses_found = 0
            res_msg = 'Success!! The Brigands and Bandits have successfully stormed the Castle! \nThey offered you some Gold for the information \nhe Kingdom loses 70% of its Gold and the next upgrade costs 6 times the usual price!'
            guard.cost_multiplier = 6
            guard.kingdom_gold = math.floor(guard.kingdom_gold * 0.3)
            attack_success = True 

    elif card_name == 'Rags to Riches':
        if not thief.has_access:
            res_msg = 'You bottled it! You didn\'t have access to the Castle\nThe guards discovered you with minimal effort\nYou were caught and put in the pillory! Do not forget this humiliation!!\nYou lose 2 turns'
            thief.extreme_wounds += 2
        else:
            if roll < min_roll:
                res_msg = 'You bottled it! That annoying brute of a Guard spotted you!!\nYou were caught and put in the pillory! Do not forget this humiliation!!\nYou lose 2 turns and access to the Castle'  
                thief.extreme_wounds += 2 
                thief.has_access = False
            else:
                res_msg = f'Success!! Your silver tongue never fails! \nYou managed to steal {math.floor(50 * guard.exfiltration_multiplier)} Gold from the Royal Vault in the limited time!'
                attack_success = True   
    
    elif card_name == 'The Cipherbane':
        if roll < min_roll:
            res_msg = 'Do you need a Sylvan dictionary? The Oracle just looked at you like a child\nYou could not extract any information from the Oracle, and quickly escaped\n'
        else:
            res_msg = f'Success!! Your Sylvan tongue skills remain polished! \nYou managed to steal {math.floor(30 * guard.exfiltration_multiplier)} Gold from the Royal Vault! \nThe Kingdom is forced to pay {60 * guard.exfiltration_multiplier} Gold as a fine to the Empire!'
            guard.kingdom_gold -= (math.floor(90 * guard.exfiltration_multiplier))
            thief.guild_gold += (math.floor(30 * guard.exfiltration_multiplier)) 
            thief.weaknesses_found += 1
            attack_success = True   
    
    elif card_name == 'Poisoned Scroll':
        if roll < min_roll:
            res_msg = 'Looks like you need to work on your spell endurance and were caught by the Royal Scribe\'s assistant \nYou could not extract any information from the Oracle, and quickly escaped'
        else:
            res_msg = f'Success!! Your impersonation of the Royal Scribe prevailed!\nThe Kingdom is in Chaos\nYou managed to steal {math.floor(50 * guard.exfiltration_multiplier)} Gold from the Royal Vault! \nThe Kingdom earns 50% of the intended Gold in the next turn!'
            attack_success = True    
    
    elif card_name == 'Blade of the Doppelganger':
        if thief.blade_countdown > 0:
            res_msg = 'Well?? What else did you expect from the wounded Seer? \nHe is now in recovery, and can\'t be called for 5 MORE turns...'
            thief.blade_countdown += 5
            idiot = True
        elif roll < min_roll:
            res_msg = 'Sorlin the Seer bottled it! He was spotted and beaten up by the nobleman and his annoying Guards!\nHe is now in recovery, and can\'t be called for 5 turns...'
            thief.blade_countdown += 5
        else:
            res_msg = f'Success!! Sorlin the Seer delivers in style! \nHe stole {math.floor(35 * guard.exfiltration_multiplier)} Gold from the Castle and loosened a few stones on the Castle wall, giving you easier access to the Castle! \nThe Kingdom is forced to pay {math.floor(30 * guard.exfiltration_multiplier)} Gold as a fine to the Empire! '
            attack_success = True        

    elif card_name == 'Grains of Malice':
        if thief.grain_countdown > 0:
            res_msg = 'Waste of time...waste of money...and a waste of energy \nThe guards are now vigilant of these grains for 5 MORE turns...'
            thief.grain_countdown +=5
            idiot = True
        elif roll < min_roll:
            res_msg = 'The grains were caught! Those pesky guards and their keen eyes....\nTime to recuperate, it is unwise to use this method for the next 5 turns...'
            thief.grain_countdown +=5
        else:
            res_msg = f'Success!! The poisoned grains reached the Kingdom\'s rations \nThe King is forced to spend {math.floor(70 * guard.exfiltration_multiplier)} Gold to hire healers and cleanse the Kingdom! \nThe Kingdom earns 15% of the intended Gold in the next turn! \nThe neighbouring King offers you 40 Gold as a token of his appreciation for harming the Kingdom \n'
            attack_success = True   

    elif card_name == 'The Mourning Blightweaver':
        if thief.pestilence_countdown > 0:
            res_msg = 'Why?? Just why?? You foolishly sauntered towards the necromancer and he repeated what he did to you last time \n You are stuck healing for 3 MORE turns and you still cannot use The Mourning Blightweaver...'
            thief.extreme_wounds += 3
            thief.pestilence_countdown += 10000
            thief.guild_gold = 0
            idiot = True  
        elif roll < min_roll:
            res_msg = 'Oh no... The wounded necromancer diverts his rage towards you and destroys all of your Gold!\nNot satisfied with that, he calls upon the undead to poison and wound you thus forcing you to spend time healing for the next 3 turns \nYou may NEVER use The Mourning Blightweaver for the rest of the game'               
            thief.extreme_wounds += 3
            thief.pestilence_countdown += 10000
            thief.guild_gold = 0
        else:
            res_msg = f'Success!! The rats have wrecked havoc in the Kingdom! \nIn the chaos, you manage to steal {math.floor(55 * guard.exfiltration_multiplier)} Gold from the Castle \nAdditionally, the King is forced to pay {math.floor(80 * guard.exfiltration_multiplier)} Gold to hire mages and exterminators to cleanse the town off these rats \nThe Kingdom earns 10% of the intended Gold in the next turn!'
            attack_success = True
             
    res_msg = res_msg.split('\n')  
    thief.deteriorate()

    return render_template("roll_d20.html", roll=roll, res_msg=res_msg, attack_success=attack_success, 
                           idiot=idiot, card_name=card_name)

@app.route("/answer_mcq", methods=["GET","POST"])
def answer_mcq():
    card_name = request.form['card_name']

    if card_name == 'Snake Oil Salesman':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.phishing_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.phishing_answers[question],right_answer=tf.phishing_answers[question][tf.phishing_answer_key[question]],
                               remark=tf.phishing_q_response[question].replace('\n', '<br>')) 

    elif card_name == 'Alehouse Swindler':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.phishing_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.phishing_answers[question],right_answer=tf.phishing_answers[question][tf.phishing_answer_key[question]],
                               remark=tf.phishing_q_response[question].replace('\n', '<br>')) 
    
    elif card_name == 'Loosened Castle Walls':

        question = random.randint(0, 5)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.backdoor_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.backdoor_answers[question],right_answer=tf.backdoor_answers[question][tf.backdoor_answer_key[question]],
                               remark=tf.backdoor_q_response[question].replace('\n', '<br>')) 
    
    elif card_name == 'Clatter of Brats':

        question = random.randint(0, 5)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.dos_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.dos_answers[question],right_answer=tf.dos_answers[question][tf.dos_answer_key[question]],
                               remark=tf.dos_q_response[question].replace('\n', '<br>')) 
    
    elif card_name == 'The Ratcaller of Elwood':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.ransomware_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.ransomware_answers[question],right_answer=tf.ransomware_answers[question][tf.ransomware_answer_key[question]],
                               remark=tf.ransomware_q_response[question].replace('\n', '<br>')) 
    
    elif card_name == 'Whispering Knaves':

        question = random.randint(0, 8)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.mitm_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.mitm_answers[question],right_answer=tf.mitm_answers[question][tf.mitm_answer_key[question]],
                               remark=tf.mitm_q_response[question].replace('\n', '<br>')) 
    
    elif card_name == 'Brigands and Bandits':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.brute_force_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.brute_force_answers[question],right_answer=tf.brute_force_answers[question][tf.brute_force_answer_key[question]],
                               remark=tf.brute_force_q_response[question].replace('\n', '<br>'))
    
    elif card_name == 'Rags to Riches':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.priv_esc_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.priv_esc_answers[question],right_answer=tf.priv_esc_answers[question][tf.priv_esc_answer_key[question]],
                               remark=tf.priv_esc_q_response[question].replace('\n', '<br>'))
    
    elif card_name == 'The Cipherbane':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.sql_injection_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.sql_injection_answers[question],right_answer=tf.sql_injection_answers[question][tf.sql_injection_answer_key[question]],
                               remark=tf.sql_injection_q_response[question].replace('\n', '<br>'))

    elif card_name == 'Poisoned Scroll':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.xss_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.xss_answers[question],right_answer=tf.xss_answers[question][tf.xss_answer_key[question]],
                               remark=tf.xss_q_response[question].replace('\n', '<br>')) 

    elif card_name == 'Blade of the Doppelganger':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.session_hijack_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.session_hijack_answers[question],right_answer=tf.session_hijack_answers[question][tf.session_hijack_answer_key[question]],
                               remark=tf.session_hijack_q_response[question].replace('\n', '<br>')) 

    elif card_name == 'Grains of Malice':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.supply_chain_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.supply_chain_answers[question],right_answer=tf.supply_chain_answers[question][tf.supply_chain_answer_key[question]],
                               remark=tf.supply_chain_q_response[question].replace('\n', '<br>'))  

    elif card_name == 'The Mourning Blightweaver':

        question = random.randint(0, 9)                          
        return render_template("thief_plays_mcq.html", card_title=card_name, question=tf.worm_questions[question].replace('\n', '<br>'),
                               list_of_answers=tf.worm_answers[question],right_answer=tf.worm_answers[question][tf.worm_answer_key[question]],
                               remark=tf.worm_q_response[question].replace('\n', '<br>'))                            


@app.route("/thief_mcq_result", methods=["POST"])
@players_required
def thief_mcq_result():
    heading = True
    right_answer = request.form['right_answer']
    remark = request.form['remark']
    user_answer = request.form['answer']
    card_name = request.form['card_name']
    usr_msg = ''
    final_msg = ''
    msg_list = []
    heading = True
    
    thief_id = session.get('player2_id')
    thief_stats = PlayerStats.query.filter_by(user_id=thief_id).first()    
    thief_stats.game_total_questions += 1
    db.session.commit()

    

    if right_answer == user_answer:

        thief_stats.game_right_answers += 1
        db.session.commit()

        if card_name == 'Snake Oil Salesman':
            usr_msg = 'The Salesman has Succeeded!'
            final_msg = 'Success!!!\n That scallywag managed to trick some fool!\n You now have access to the castle!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.has_access = True
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list) 

        elif card_name == 'Alehouse Swindler':
            usr_msg = 'The Swindler has Succeeded!'
            final_msg = 'Success!!!\n That drunkard managed to trick some fool!\n You now have access to the castle!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.has_access = True
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)    

        elif card_name == 'Loosened Castle Walls':
            usr_msg = 'The Walls have been Loosened!'
            final_msg = 'Success!!!\n You managed to break a few rocks in a decrepit castle wall.\nYou now have access to the castle!\nYou now steal 50% more Gold'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')

            guard.kingdom_gold -= math.floor(25 * guard.exfiltration_multiplier)
            thief.guild_gold += math.floor(25 * guard.exfiltration_multiplier)          
            guard.exfiltration_multiplier = 1.5 
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)

        elif card_name == 'Clatter of Brats':
            usr_msg = 'The Brats have Cluttered the Gates!'
            final_msg = 'Success!! Those little brats annoyed the guards and the travelling salesmen!\nThe Kingdom loses 10% of its Gold and earns only 10% of the intended Gold in the next turn!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')

            guard.income_multiplier = 0.1
            guard.kingdom_gold = math.floor(guard.kingdom_gold * 0.9)
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list) 
        
        elif card_name == 'The Ratcaller of Elwood':
            usr_msg = 'The Ratcaller has Seized the Grains!'
            final_msg = f'Success!!\nThe Ratcaller of Elwood managed to ransack the Castle\'s granary!\nThe Kingdom loses {200 * guard.exfiltration_multiplier} Gold to your ransom!\nThe Kingdom earns only 25% of its intended Gold in the next turn!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.guild_gold += (200 * guard.exfiltration_multiplier)
            guard.kingdom_gold -= (200 * guard.exfiltration_multiplier)
            guard.income_multiplier = 0.25
            thief.weaknesses_found += 1
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Whispering Knaves':
            usr_msg = 'The Knaves have Rewritten the Message!'
            final_msg = f'Success!! The Knaves managed to decipher and rephrase the Castle\'s message! \nThe Knaves additionally stole {20 * guard.exfiltration_multiplier} Gold from the Messenger! \nThe Kingdom earns 60% of its intended Gold in the next turn!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.income_multiplier = 0.6
            guard.kingdom_gold -= (20 * guard.exfiltration_multiplier)  
            thief.weaknesses_found += 1
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Brigands and Bandits':
            usr_msg = 'Chaos Galore!!!!'
            final_msg = 'Success!!\n The Brigands and Bandits have successfully stormed the Castle! \nThey offered you some Gold for the information \nThe Kingdom loses 70% of its Gold and the next upgrade costs 6 times the usual price!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')

            if thief.weaknesses_found == 1:
                thief.guild_gold += 5
            elif thief.weaknesses_found <= 3:
                thief.guild_gold += 15
            else:
                thief.guild_gold += 30

            thief.weaknesses_found = 0
            thief.has_access = True
            guard.cost_multiplier = 6
            guard.kingdom_gold = math.floor(guard.kingdom_gold * 0.3)

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)

        elif card_name == 'Rags to Riches':
            usr_msg = 'You are now a Noble! For now....'
            final_msg = f'Success!! Your silver tongue never fails! \nYou managed to steal {math.floor(50 * guard.exfiltration_multiplier)} Gold from the Royal Vault in the limited time!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.kingdom_gold -= math.floor(50 * guard.exfiltration_multiplier) 
            thief.guild_gold += math.floor(50 * guard.exfiltration_multiplier) 
            thief.weaknesses_found += 1
                
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'The Cipherbane':
            usr_msg = 'You have Cheated the Oracle!'
            final_msg = f'Success!! Your Sylvan tongue skills remain polished! \nYou managed to steal {math.floor(30 * guard.exfiltration_multiplier)} Gold from the Royal Vault! \nThe Kingdom is forced to pay {60 * guard.exfiltration_multiplier} Gold as a fine to the Empire!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.kingdom_gold -= (math.floor(90 * guard.exfiltration_multiplier))
            thief.guild_gold += (math.floor(30 * guard.exfiltration_multiplier)) 
            thief.weaknesses_found += 1      
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Poisoned Scroll':
            usr_msg = 'The Scroll now bends to YOUR Will!'
            final_msg = f'Success!! Your impersonation of the Royal Scribe prevailed!\nThe Kingdom is in Chaos\nYou managed to steal {math.floor(50 * guard.exfiltration_multiplier)} Gold from the Royal Vault! \nThe Kingdom earns 50% of the intended Gold in the next turn!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.income_multiplier = 0.5
            guard.kingdom_gold -= math.floor(50 * guard.exfiltration_multiplier)
            thief.guild_gold += math.floor(50 * guard.exfiltration_multiplier)
            thief.weaknesses_found += 1 

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Blade of the Doppelganger':
            usr_msg = 'Sorlin the Seer is Unstoppable!!'
            final_msg = f'Success!! Sorlin the Seer delivers in style! \nHe stole {math.floor(35 * guard.exfiltration_multiplier)} Gold from the Castle and loosened a few stones on the Castle wall, giving you easier access to the Castle! \nThe Kingdom is forced to pay {math.floor(30 * guard.exfiltration_multiplier)} Gold as a fine to the Empire!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.exfiltration_multiplier = 1.5
            guard.kingdom_gold -= math.floor(65 * guard.exfiltration_multiplier)
            thief.guild_gold += math.floor(35 * guard.exfiltration_multiplier)
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Grains of Malice':
            usr_msg = 'Is it Food or Poison??!!'
            final_msg = f'Success!!\n The poisoned grains reached the Kingdom\'s rations \nThe King is forced to spend {math.floor(70 * guard.exfiltration_multiplier)} Gold to hire healers and cleanse the Kingdom! \nThe Kingdom earns 15% of the intended Gold in the next turn! \nThe neighbouring King offers you 40 Gold as a token of his appreciation for harming the Kingdom'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.income_multiplier = 0.15
            guard.kingdom_gold -= (math.floor(70 * guard.exfiltration_multiplier))
            thief.guild_gold += 40
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'The Mourning Blightweaver':
            usr_msg = 'Plagued by the Undead!!'
            final_msg = f'Success!! The rats have wrecked havoc in the Kingdom! \nIn the chaos, you manage to steal {math.floor(55 * guard.exfiltration_multiplier)} Gold from the Castle \nAdditionally, the King is forced to pay {math.floor(80 * guard.exfiltration_multiplier)} Gold to hire mages and exterminators to cleanse the town off these rats \nThe Kingdom earns 10% of the intended Gold in the next turn!'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            guard.income_multiplier = 0.1
            guard.kingdom_gold -= math.floor(135 * guard.exfiltration_multiplier)
            thief.guild_gold += math.floor(55 * guard.exfiltration_multiplier)  
            thief.weaknesses_found += 1

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        
    else:
        heading = False

        if card_name == 'Snake Oil Salesman':
            usr_msg = 'The Salesman has Failed!'
            final_msg = 'Darn it!\n Your salesman was caught!\nLuckily, he got away but the guards and noblemen are far more wary now...\nYou can\'t use him or the drunkard for 2 turns'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.phishing_countdown += 2
            

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)   
        
        elif card_name == 'Alehouse Swindler':
            usr_msg = 'The Swindler has Failed!'
            final_msg = 'Darn it!\n Your drunkard was caught!\nLuckily, he got away but the guards and noblemen are far more wary now...\nYou can\'t use him or the drunkard for 2 turns'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.phishing_countdown += 2

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Loosened Castle Walls':
            usr_msg = 'The Guards have Noticed the Attempt!!'
            final_msg = 'Oof, you tried too hard and caused a LOT of noise!\n The guards have noticed this \nYou can\'t play this card for 5 turns'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.walls_countdown += 5

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Clatter of Brats':
            usr_msg = 'The Brats have Run Away!!'
            final_msg = 'The children scattered away and scammed you instead!\nWell well well, how the tables turn...'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'The Ratcaller of Elwood':
            usr_msg = 'The Ratcaller has Failed!!'
            final_msg = 'He bottled it!\n The Ratcaller was spotted and beaten up by those annoying Guards!\nHe is now in recovery, and can\'t be called for 5 turns...'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.ratcaller_countdown += 5

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Whispering Knaves':
            usr_msg = 'The Knaves have Failed!!'
            final_msg = 'You bottled it! Your Knaves were spotted and beaten up by those annoying Guards!\nThey are now hiding in the dense forest, and can\'t be called for 5 turns...'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.knaves_countdown += 5

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Brigands and Bandits':
            usr_msg = 'You have been Betrayed!!!!'
            final_msg = 'Fresh meat is in the House, and YOU are the entree!\nThe Brigands and Bandits are humiliated by the Guards\nIn retaliation, they wound you and steal ALL of your Gold \nYour wounds are severe and cannot move for 2 turns \nYou are now wanted by the Brigands and Bandits and the card may not be played for 15 turns'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.bnb_countdown += 15
            thief.guild_gold = 0
            thief.extreme_wounds += 2

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Rags to Riches':
            usr_msg = 'You have Bottled it!!!!'
            final_msg = 'That annoying brute of a Guard spotted you!!\nYou were caught and put in the pillory! Do not forget this humiliation!!\nYou lose 2 turns and access to the Castle'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.extreme_wounds += 2  
            thief.has_access = False

            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'The Cipherbane':
            usr_msg = 'Sylvan Flop!!'
            final_msg = 'Do you need a Sylvan dictionary?\n The Oracle just looked at you like a child\nYou could not extract any information from the Oracle, and quickly escaped'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Poisoned Scroll':
            usr_msg = 'Butter Fingers!!'
            final_msg = 'Looks like you need to work on your spell endurance\n You were caught by the Royal Scribe\'s assistant \nYou could not poison the Scrolls, and quickly escaped'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Blade of the Doppelgangers':
            usr_msg = 'Caught by Weary Eyes!!'
            final_msg = 'Sorlin the Seer bottled it!\n He was spotted and beaten up by the nobleman and his annoying Guards!\nHe is now in recovery, and can\'t be called for 5 turns...'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.blade_countdown += 5
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'Grains of Malice':

            usr_msg = 'Caught by Weary Eyes!!'
            final_msg = 'The grains were caught! Those pesky guards and their keen eyes....\nTime to recuperate, it is unwise to use this method for the next 5 turns...'
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.grain_countdown +=5    

            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
        
        elif card_name == 'The Mourning Blightweaver':

            usr_msg = 'The Necromancer meets his Match!!'
            final_msg = 'Oh no...\nThe wounded necromancer diverts his rage towards you and destroys all of your Gold!\nNot satisfied with that, he calls upon the undead to poison and wound you thus forcing you to spend time healing for the next 3 turns \nYou may NEVER use The Mourning Blightweaver for the rest of the game'               
            final_msg = final_msg.replace('\n', '<br>')
            msg_list = final_msg.split('<br>')
            thief.extreme_wounds += 3
            thief.pestilence_countdown += 10000
            thief.guild_gold = 0    
            
            return render_template("thief_mcq_result.html", heading=heading, usr_msg=usr_msg,
                                   right_answer=right_answer, remark=remark, final_msg=msg_list)
         

@app.route("/thief_card_explanation")
def thief_card_explanation():

    global thief_future
    thief_future = True
    empty = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load("static/audio/WhiteHole.mp3")
    pygame.mixer.music.play(-1)

    if len(thief.card_headers_medieval) == 0:
        empty = True
    
    real_life_explanation = [exp.replace('\n', '<br>') for exp in thief.card_explanations_real_life]
    zipped_data = zip(thief.card_headers_medieval, thief.card_headers_real_life,
                      real_life_explanation, thief.rl_card_img)
    return render_template("thief_card_explanation.html", data=zipped_data, empty=empty)

@app.route("/thief_countdown")
def thief_countdown():

    global thief_future

    if thief_future == True:
        thief_future = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("static/audio/BattleOfTheCreek.mp3")
        pygame.mixer.music.play(start=60.0)
        pygame.mixer.music.play(-1)

    titles_and_attrs = [
        ("Snake Oil Salesman and Alehouse Swindler", "phishing_countdown"),
        ("Loosened Castle Walls", "walls_countdown"),
        ("The Ratcaller of Elwood", "ratcaller_countdown"),
        ("The Whispering Knaves", "knaves_countdown"),
        ("Brigands and Bandits", "bnb_countdown"),
        ("Blade of the Doppelganger", "blade_countdown"),
        ("Grains of Malice", "grain_countdown"),
        ("The Mourning Blightweaver", "pestilence_countdown")
    ]

    active_cards = []
    countdown = []
    empty_message = ''

    for title, attr in titles_and_attrs:
        value = getattr(thief, attr, 0)
        if value > 0:
            active_cards.append(title)
            countdown.append(value)

    if len(active_cards) == 0:
        empty_message = "No attacks are on cooldown, you are good to go!!\nUnleash Hell!!"

    zipped_data = zip(active_cards, countdown)
    return render_template("thief_countdown.html", data=zipped_data, empty_message=empty_message,
                           weaknesses=thief.weaknesses_found, access=thief.has_access)    

@app.route("/glossary")
def glossary():
    guard_medieval_cards_data_zip = []
    for medieval_title, img_url in zip(gd.guard_protection_header_medieval, gd.guard_image_list):
        guard_medieval_cards_data_zip.append((medieval_title, img_url))

    guard_real_life_cards_data_zip = []
    guard_expl = []
    for explanation in gd.guard_protection_explanation_real_life:
        guard_expl.append(explanation.replace('\n','<br>'))
    for real_title, medieval_title, card_expl, img_url in zip(gd.guard_protection_header_real_life, gd.guard_protection_header_medieval, guard_expl, gd.guard_rl_image_list):
        guard_real_life_cards_data_zip.append((real_title, medieval_title, card_expl, img_url))  

    thief_medieval_cards_data_zip = []
    for medieval_title, img_url in zip(tf.thief_attack_header_medieval, tf.thief_image_list):
        thief_medieval_cards_data_zip.append((medieval_title, img_url))

    thief_real_life_cards_data_zip = []
    thief_expl = []
    for explanation in tf.thief_attack_explanation_real_life:
        thief_expl.append(explanation.replace('\n','<br>'))
    for real_title, medieval_title, card_expl, img_url in zip(tf.thief_attack_header_real_life, tf.thief_attack_header_medieval, thief_expl, tf.thief_rl_image_list):
        thief_real_life_cards_data_zip.append((real_title, medieval_title, card_expl, img_url))              
    
    return render_template("glossary.html", guard_medieval_card=guard_medieval_cards_data_zip,
        guard_real_card=guard_real_life_cards_data_zip, thief_medieval_card=thief_medieval_cards_data_zip,
        thief_real_card=thief_real_life_cards_data_zip)

@app.route("/tutorial")
def tutorial():
    return render_template("/tutorial/page1.html")

@app.route("/page/<int:page_num>", methods=["GET", "POST"])
def tutorial_page(page_num):
    if 2 <= page_num <= 50:
        return render_template(f"tutorial/page{page_num}.html")
    else:
        return "Page not found",  404

@app.route('/game_stats')
@players_required
def game_stats():
    global guard_total_answers, guard_right_answers, thief_total_answers, thief_right_answers

    guard_id = session.get('player1_id')
    thief_id = session.get('player2_id')    

    guard_stats = PlayerStats.query.filter_by(user_id=guard_id).first()
    thief_stats = PlayerStats.query.filter_by(user_id=thief_id).first()

    if not guard_stats or not thief_stats:
        flash("Error: Player stats not found for current session.")
        return redirect(url_for('login'))
    
    guard_last_10_games_as_guard = GameSession.query.filter_by(guard_user_id=guard_id)\
                                     .order_by(GameSession.timestamp.desc())\
                                     .limit(10)\
                                     .all()

    thief_last_10_games_as_thief = GameSession.query.filter_by(thief_user_id=thief_id)\
                                     .order_by(GameSession.timestamp.desc())\
                                     .limit(10)\
                                     .all()

    guard_mcq_chart_json = create_mcq_accuracy_chart("Guard", guard_last_10_games_as_guard, 'guard')
    thief_mcq_chart_json = create_mcq_accuracy_chart("Thief", thief_last_10_games_as_thief, 'thief')
    
    guard_outcome_chart_json = create_game_outcome_chart("Guard", guard_id, guard_last_10_games_as_guard, 'guard')
    thief_outcome_chart_json = create_game_outcome_chart("Thief", thief_id, thief_last_10_games_as_thief, 'thief')

    
    print("\n--- Guard MCQ Chart JSON (from app.py) ---")
    print(guard_mcq_chart_json)
    print("\n--- Thief MCQ Chart JSON (from app.py) ---")
    print(thief_mcq_chart_json)
    print("\n--- Guard Outcome Chart JSON (from app.py) ---")
    print(guard_outcome_chart_json)
    print("\n--- Thief Outcome Chart JSON (from app.py) ---")
    print(thief_outcome_chart_json)
    print("\n--------------------------------------------\n")

    return render_template('game_stats.html', 
                           guard_stats=guard_stats, 
                           thief_stats=thief_stats,
                           guard_total_questions=guard_total_answers, 
                           guard_right_answers=guard_right_answers,
                           thief_total_questions=thief_total_answers, 
                           thief_right_answers=thief_right_answers,
                           guard_mcq_chart=guard_mcq_chart_json,
                           thief_mcq_chart=thief_mcq_chart_json,
                           guard_outcome_chart=guard_outcome_chart_json,
                           thief_outcome_chart=thief_outcome_chart_json)

@app.route('/leaderboard')
def leaderboard():
    sort_by = request.args.get('sort_by', 'total_win_rate')

    sort_options = {
        'games_played': PlayerStats.total_games_played,
        'total_win_rate': PlayerStats.total_win_rate,
        'win_rate_as_guard': PlayerStats.win_rate_as_guard,
        'win_rate_as_thief': PlayerStats.win_rate_as_thief,
        'mcq_accuracy': PlayerStats.total_answer_accuracy
    }

    sort_column = sort_options.get(sort_by, PlayerStats.total_win_rate)

    leaderboard_data = db.session.query(PlayerStats, User)\
        .join(User, PlayerStats.user_id == User.id)\
        .order_by(sort_column.desc())\
        .limit(20)\
        .all()

    return render_template('leaderboard.html',
                           leaderboard_data=leaderboard_data,
                           current_sort=sort_by)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
