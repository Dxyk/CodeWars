Position = {'high': 'h', 'low': 'l'}


class Warrior:
    def __init__(self, name):
        """
        :param name: name of the warrior
        :type name: str
        :return: a warrior
        :rtype: Warrior
        """
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default block is "", that is unguarded
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        """
        :param enemy: a enemy warrior
        :type enemy: Warrior
        :param position: the position of the attack
        :type position: str
        :return: None
        :rtype: None
        """
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        damage = 0
        if enemy.block != position:
            damage += 10 if position == Position['high'] else 5
            # and even more damage if the enemy is not blocking at all
            if enemy.block == "":
                damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        # health cannot have negative values
        self.health = max(0, new_health) if self.health > 0 else new_health
        # if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased = True
            self.zombie = False
        # he would be a zombie only if he was already dead
        if self.deceased and self.health < 0:
            self.zombie = True
