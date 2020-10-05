# TODO Corregir fallos
ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
         "Elite", "Conqueror", "Champion", "Master", "Greatest"]


class Warrior():
    # Next level every 100 increase, max level 100
    level = 1
    # At every 10 levels new rank tier
    # 1-9 Pushover, 80-89 Champion
    rank = "Pushover"
    # Cumulative
    experience = 100
    achievements = []

    def training(self, train_battle):
        if self.level >= train_battle[2] and train_battle[2] != 0:
            self.experience += train_battle[1]
            self.achievements.append(train_battle[0])
            self.actualize_warrior()
            return train_battle[0]
        else:
            return "Not strong enough"

    def actualize_warrior(self):
        if self.experience > 10000:
            self.level = 100
            self.rank = ranks[9]
        else:
            self.level = self.experience//100
            self.rank = ranks[self.experience//1000]

    def battle(self, battle_level):
        if battle_level < 1 or battle_level > 100:
            return "Invalid level"
        else:
            if battle_level == self.level:
                self.experience += 10
            elif battle_level == self.level - 1:
                self.experience += 5
            elif battle_level <= self.level - 2:
                # Simbólico, después quitar
                self.experience += 0
            elif battle_level > self.level:
                diff = battle_level - self.level
                self.experience += 20 * diff * diff
            if battle_level - self.level >= 5:
                self.actualize_warrior()
                return "You've been defeated"
            elif self.level - battle_level >= 2:
                self.actualize_warrior()
                return "Easy fight"
            elif self.level - battle_level <= 1:
                self.actualize_warrior()
                return "A good fight"
            elif self.level < battle_level:
                self.actualize_warrior()
                return "An intense fight"
