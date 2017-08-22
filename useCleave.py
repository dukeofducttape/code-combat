def useCleave(enemies, range, minEnemies):
    enemy = hero.findNearest(enemies)
    if enemy and hero.isReady("cleave") and numInRange(enemies, range) >= minEnemies:
        hero.cleave(enemy)
