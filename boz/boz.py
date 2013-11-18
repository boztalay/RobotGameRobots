import rg

congregationPoints = [rg.CENTER_POINT]

class Robot:
    def act(self, game):
	closestPoint = self.closestCongregationPoint(game)
        # if we're at the closest congregation point, stay put
        if self.location == closestPoint:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.get('robots').items():
            if bot.get('player_id') != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    if self.hp < 10:
                        return ['suicide']
                    else:
                        return ['attack', loc]

        # move toward the closest congregation point
        return ['move', rg.toward(self.location, closestPoint)]
    
    def closestCongregationPoint(self, game):
        closestPoint = (0, 0)
        closestDistance = 1000
        for pointToTest in congregationPoints:
            distance = rg.dist(self.location, pointToTest)
            if distance < closestDistance:
                closestPoint = pointToTest
                closestDistance = distance
        return closestPoint
