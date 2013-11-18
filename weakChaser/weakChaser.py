import rg

class Robot:
    def act(self, game):
        # if there are enemies around, attack them
        for loc, bot in game.get('robots').items():
            if bot.get('player_id') != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    if self.hp < 10:
                        return ['suicide']
                    else:
                        return ['attack', loc]

        # otherwise, move toward the weakest enemy robot
        return ['move', rg.toward(self.location, self.weakestEnemy(game))]
    
    def weakestEnemy(self, game):
        weakestEnemy = (0, 0)
        weakestEnemyHp = 1000

        for loc, bot in game.get('robots').items():
            if bot.get('player_id') != self.player_id:
                if bot.get('hp') <= weakestEnemyHp:
                    weakestEnemyHp = bot.get('hp')
                    weakestEnemy = loc

        return weakestEnemy
