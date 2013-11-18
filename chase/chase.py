import rg

class Robot:
    def act(self, game):
        closestEnemy = self.findClosestEnemy(game)
        if rg.dist(self.location, closestEnemy) < 1:
            if self.hp < 11:
                return ['suicide']
            else:
            	return ['attack', loc]
        else:
            return ['move', rg.toward(self.location, closestEnemy)]

    def findClosestEnemy(self, game):
        closestDistance = 1000
        closestLoc = (0, 0)
        for loc, robot in game['robots'].items():
            if robot.player_id != self.player_id:
                distance = rg.dist(self.location, loc)
                if distance < closestDistance:
                    closestDistance = distance
                    closestLoc = loc
        return closestLoc
