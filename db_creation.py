from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

CREATE_DB = "CREATE DATABASE GYM_buddy;"

CREATE_TRAININGS_TABLE = """CREATE TABLE trainings(
    id serial PRIMARY KEY, 
    training_name varchar(255) UNIQUE
    )"""

CREATE_EXERCISES_TABLE = """CREATE TABLE exercises(
    id SERIAL PRIMARY KEY, 
    exercise_name varchar(255) UNIQUE,
    trainings_id INTEGER REFERENCES trainings(id) ON DELETE CASCADE )"""

CREATE_USERS_TABLE = """CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    user_nick varchar(255) UNIQUE,
    user_weight DECIMAL(4,1),
    user_muscles_weight DECIMAL(4,1),
    user_fat_weight DECIMAL(4,1),
    user_metabolic_age INTEGER,
    user_chest_circuit DECIMAL(4,1),
    user_biceps_circuit DECIMAL(4,1),
    user_biceps_circuit_tight DECIMAL(4,1),
    user_buttock_circuit DECIMAL(4,1),
    user_thigh_circuit DECIMAL(4,1),
    user_waist_circuit DECIMAL(4,1),
    user_cald_circuit DECIMAL(4,1)
    )"""

CREATE_USERS_HISTORY_TABLE = """CREATE TABLE users_history(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    user_nick varchar(255) UNIQUE,
    user_weight DECIMAL(5,2),
    user_muscles_weight DECIMAL(5,2),
    user_fat_weight DECIMAL(5,2),
    user_metabolic_age INTEGER,
    user_chest_circuit DECIMAL(4,1),
    user_biceps_circuit DECIMAL(4,1),
    user_biceps_circuit_tight DECIMAL(4,1),
    user_buttock_circuit DECIMAL(4,1),
    user_thigh_circuit DECIMAL(4,1),
    user_waist_circuit DECIMAL(4,1),
    user_cald_circuit DECIMAL(4,1),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

CREATE_EXERCISES_HISTORY_TABLE = """CREATE TABLE exercises_history(
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    exercise_reps INTEGER,
    weight_add DECIMAL(4,1) DEFAULT 0,
    total_weight DECIMAL(4,1),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)

try:
    cnx = connect(database="gym_buddy", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("Table users created")
    except errors.DuplicateTable as e:
        print("Table exists ", e)
    try:
        cursor.execute(CREATE_TRAININGS_TABLE)
        print("Table trainings created")
    except errors.DuplicateTable as e:
        print("Table exists ", e)
    try:
        cursor.execute(CREATE_USERS_HISTORY_TABLE)
        print("Table users_history created")
    except errors.DuplicateTable as e:
        print("Table exists ", e)
    try:
        cursor.execute(CREATE_EXERCISES_TABLE)
        print("Table exercises created")
    except errors.DuplicateTable as e:
        print("Table exists ", e)
    try:
        cursor.execute(CREATE_EXERCISES_HISTORY_TABLE)
        print("Table exercises_history created")
    except errors.DuplicateTable as e:
        print("Table exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)