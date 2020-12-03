from connection import connect

connection = connect()
cursor = connection.cursor()


class User:

    def __init__(self, nick, weight, muscles_weight, fat_weight, metabolic_age, chest_circuit, biceps_circuit,
                 biceps_circuit_tight, buttock_circuit, thigh_circuit, waist_circuit, cald_circuit):
        self._id = -1
        self.nick = nick
        self.weight = weight
        self.muscles_weight = muscles_weight
        self.fat_weight = fat_weight
        self.metabolic_age = metabolic_age
        self.chest_circuit = chest_circuit
        self.biceps_circuit = biceps_circuit
        self.biceps_circuit_tight = biceps_circuit_tight
        self.buttock_circuit = buttock_circuit
        self.thigh_circuit = thigh_circuit
        self.waist_circuit = waist_circuit
        self.cald_circuit = cald_circuit

    @property
    def id_(self):
        return self._id

    def save_to_db(self, cursor):
        if self.id_ == -1:
            sql = """INSERT INTO users(user.nick, user.weight, user.muscles_weight, user. fat_weight, user.metabolic_age, 
                      user.chest_circuit, user.biceps_circuit, user.biceps_circuit_tight, user.buttock_circuit,
                      user.thigh_circuit, user.waist_circuit, user.cald_circuit)
                            VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s) RETURNING id"""
            values = (self.nick, self.weight, self.muscles_weight, self.fat_weight, self.metabolic_age,
                      self.chest_circuit, self.biceps_circuit, self.biceps_circuit_tight, self.buttock_circuit,
                      self.thigh_circuit, self.waist_circuit, self.cald_circuit)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
        else:
            sql = """UPDATE users SET user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age, 
                      user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
                      user_thigh_circuit, user_waist_circuit, user_cald_circuit
                           WHERE id=%s"""
            values = (self.nick, self.weight, self.muscles_weight, self.fat_weight, self.metabolic_age,
                      self.chest_circuit, self.biceps_circuit, self.biceps_circuit_tight, self.buttock_circuit,
                      self.thigh_circuit, self.waist_circuit, self.cald_circuit, self._id)
            cursor.execute(sql, values)
        sql = """INSERT INTO users_history(user_id, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age, 
                      user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
                      user_thigh_circuit, user_waist_circuit, user_cald_circuit)
                                    VALUES(%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s) RETURNING id"""
        values = (self._id, self.nick, self.weight, self.muscles_weight, self.fat_weight, self.metabolic_age,
                  self.chest_circuit, self.biceps_circuit, self.biceps_circuit_tight, self.buttock_circuit,
                  self.thigh_circuit, self.waist_circuit, self.cald_circuit)
        cursor.execute(sql, values)
        return True

    @staticmethod
    def load_user_by_id(id_, cursor):
        sql = """SELECT id, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age, 
                      user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
                      user_thigh_circuit, user_waist_circuit, user_cald_circuit FROM users WHERE id=%s"""
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            (id_, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age,
             user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
             user_thigh_circuit, user_waist_circuit, user_cald_circuit) = data
            loaded_user = User(user_nick)
            loaded_user._id = id_
            loaded_user.nick = user_nick
            loaded_user.weight = user_weight
            loaded_user.muscles_weight = user_muscles_weight
            loaded_user.fat_weight = user_fat_weight
            loaded_user.metabolic_age = user_metabolic_age
            loaded_user.chest_circuit = user_chest_circuit
            loaded_user.biceps_circuit = user_biceps_circuit
            loaded_user.biceps_circuit_tight = user_biceps_circuit_tight
            loaded_user.buttock_circuit = user_buttock_circuit
            loaded_user.thigh_circuit = user_thigh_circuit
            loaded_user.waist_circuit = user_waist_circuit
            loaded_user.cald_circuit = user_cald_circuit
            return loaded_user

    @staticmethod
    def load_user_by_username(nick, cursor):
        sql = """SELECT id, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age, 
                      user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
                      user_thigh_circuit, user_waist_circuit, user_cald_circuit FROM users WHERE username=%s"""
        cursor.execute(sql, (nick,))
        data = cursor.fetchone()
        if data:
            (id_, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age,
             user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
             user_thigh_circuit, user_waist_circuit, user_cald_circuit) = data
            loaded_user = User(user_nick)
            loaded_user._id = id_
            loaded_user.nick = user_nick
            loaded_user.weight = user_weight
            loaded_user.muscles_weight = user_muscles_weight
            loaded_user.fat_weight = user_fat_weight
            loaded_user.metabolic_age = user_metabolic_age
            loaded_user.chest_circuit = user_chest_circuit
            loaded_user.biceps_circuit = user_biceps_circuit
            loaded_user.biceps_circuit_tight = user_biceps_circuit_tight
            loaded_user.buttock_circuit = user_buttock_circuit
            loaded_user.thigh_circuit = user_thigh_circuit
            loaded_user.waist_circuit = user_waist_circuit
            loaded_user.cald_circuit = user_cald_circuit
            return loaded_user

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, hashed_password FROM Users"
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            (id_, user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age,
             user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
             user_thigh_circuit, user_waist_circuit, user_cald_circuit) = row
            loaded_user = User(user_nick)
            loaded_user._id = id_
            loaded_user.nick = user_nick
            loaded_user.weight = user_weight
            loaded_user.muscles_weight = user_muscles_weight
            loaded_user.fat_weight = user_fat_weight
            loaded_user.metabolic_age = user_metabolic_age
            loaded_user.chest_circuit = user_chest_circuit
            loaded_user.biceps_circuit = user_biceps_circuit
            loaded_user.biceps_circuit_tight = user_biceps_circuit_tight
            loaded_user.buttock_circuit = user_buttock_circuit
            loaded_user.thigh_circuit = user_thigh_circuit
            loaded_user.waist_circuit = user_waist_circuit
            loaded_user.cald_circuit = user_cald_circuit
        return users

    def delete(self, cursor):
        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, (self.id_,))
        self._id = -1
        return True


class Exercise:

    def __init__(self, exercise_name, training_id):
        self._id = -1
        self.exercise_name = exercise_name
        self.training_id = training_id

    @property
    def id_(self):
        return self._id

    def save_to_db(self, cursor):
        if self.id_ == -1:
            sql = """INSERT INTO exercises(exercise_name, training_id)
                            VALUES(%s, %s) RETURNING id"""
            values = (self.exercise_name, self.training_id)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE exercises SET exercise_name=%s, training_id=%s
                           WHERE id=%s"""
            values = (self.exercise_name, self.training_id, self.id_)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_exercise_by_id(id_, cursor):
        sql = "SELECT id, exercise_name, training_id FROM exercises WHERE id=%s"
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            id_, exercise_name, training_id = data
            loaded_exercise = User(exercise_name)
            loaded_exercise._id = id_
            loaded_exercise.exercise_name = exercise_name
            loaded_exercise.training_id = training_id
            return loaded_exercise

    @staticmethod
    def load_exercise_by_name(exercise_name, cursor):
        sql = "SELECT id, exercise_name, training_id FROM exercises WHERE exercise_name=%s"
        cursor.execute(sql, (exercise_name,))
        data = cursor.fetchone()
        if data:
            id_, exercise_name, training_id = data
            loaded_exercise = Exercise(exercise_name)
            loaded_exercise._id = id_
            loaded_exercise.exercise_name = exercise_name
            loaded_exercise.training_id = training_id
            return loaded_exercise

    @staticmethod
    def load_all_exercises(cursor):
        sql = "SELECT id, exercise_name, training_id FROM exercises"
        exercises = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, exercise_name, training_id = row
            loaded_exercise = Exercise(exercise_name)
            loaded_exercise._id = id_
            loaded_exercise.exercise_name = exercise_name
            loaded_exercise.training_id = training_id
            exercises.append(loaded_exercise)
        return exercises

    @staticmethod
    def load_exercises_by_training_id(training_id, cursor):
        sql = "SELECT id, exercise_name, training_id FROM exercises WHERE training_id=%s"
        cursor.execute(sql, (training_id,))
        exercises = []
        for row in cursor.fetchall():
            id_, exercise_name, training_id = row
            loaded_exercise = Exercise(exercise_name)
            loaded_exercise._id = id_
            loaded_exercise.exercise_name = exercise_name
            loaded_exercise.training_id = training_id
            exercises.append(loaded_exercise)
        return exercises

    def delete(self, cursor):
        sql = "DELETE FROM Exercises WHERE id=%s"
        cursor.execute(sql, (self.id_,))
        self._id = -1
        return True


class Training:
    def __init__(self, training_name):
        self._id = -1
        self.training_name = training_name

    @property
    def id_(self):
        return self._id

    def save_to_db(self, cursor):
        if self.id_ == -1:
            sql = """INSERT INTO trainings(training_name)
                            VALUES(%s) RETURNING id"""
            values = (self.training_name)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE trainings SET training_name=%s
                           WHERE id=%s"""
            values = (self.training_name, self.id_)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_training_by_id(id_, cursor):
        sql = "SELECT id, training_name FROM trainings WHERE id=%s"
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            id_, training_name = data
            loaded_training = Training(training_name)
            loaded_training._id = id_
            return loaded_training

    @staticmethod
    def load_training_by_name(training_name, cursor):
        sql = "SELECT id, training_name FROM trainings WHERE training_name=%s"
        cursor.execute(sql, (training_name,))
        data = cursor.fetchone()
        if data:
            id_, training_name = data
            loaded_training = Training(training_name)
            loaded_training._id = id_
            return loaded_training

    @staticmethod
    def load_all_trainings(cursor):
        sql = "SELECT id, training_name FROM trainings"
        trainings = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, training_name = row
            loaded_training = Training()
            loaded_training._id = id_
            loaded_training.training_name = training_name
            trainings.append(loaded_training)
        return trainings

    def delete(self, cursor):
        sql = "DELETE FROM trainings WHERE id=%s"
        cursor.execute(sql, (self.id_,))
        self._id = -1
        return True


def exercise_history_save_to_db(exercise_id, user_id, exercise_reps, weight_add):
    total_weight = weight_add + User.load_user_by_id(user_id, cursor).weight
    sql = """INSERT INTO exercises_history(exercise_id, user_id, exercise_reps, weight_add, total_weight)
                                        VALUES(%s, %s, %s,%s, %s) RETURNING id"""
    values = (exercise_id, user_id, exercise_reps, weight_add, total_weight)
    cursor.execute(sql, values)
    return True
