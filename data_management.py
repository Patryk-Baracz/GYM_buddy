class User:

    def __init__(self, nick, weight, muscles_weight, fat_weight, metabolic_age, chest_circuit, biceps_circuit,
                 biceps_circuit_tight, buttock_circuit, thigh_circuit, waist_circuit, cald_circuit):
        self._id = -1
        self.nick = nick
        self.weight = weight
        self.muscles_weight = muscles_weight
        self. fat_weight = fat_weight
        self.metabolic_age = metabolic_age
        self. chest_circuit = chest_circuit
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
            values = (self.nick, self.weight, self.muscles_weight, self. fat_weight, self.metabolic_age,
                      self.chest_circuit, self.biceps_circuit, self.biceps_circuit_tight, self.buttock_circuit,
                      self.thigh_circuit, self.waist_circuit, self.cald_circuit)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
        else:
            sql = """UPDATE users SET user_nick, user_weight, user_muscles_weight, user_fat_weight, user_metabolic_age, 
                      user_chest_circuit, user_biceps_circuit, user_biceps_circuit_tight, user_buttock_circuit,
                      user_thigh_circuit, user_waist_circuit, user_cald_circuit
                           WHERE id=%s"""
            values = (self.nick, self.weight, self.muscles_weight, self. fat_weight, self.metabolic_age,
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
    def load_user_by_id(cursor, id_):
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
    def load_user_by_username(cursor, nick):
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