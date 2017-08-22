enemies = hero.findEnemies()
enemy = findMostHealth(enemies)
if enemy:
    while enemy.health > 0:
        if hero.isReady("cleave") and numInRange(enemies, 7) > 3:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
