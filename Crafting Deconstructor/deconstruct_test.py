import math

recipes = {
    'bed': (
        ('wool', 3),
        ('plank', 3),
    ),
    'wool': (
        ('string', 4),
    ),
    'plank': (
        ('wood', 0.25),
    ),
    'wood': (),
    'string': (),

    'computer': (
        ('processor', 1),
        ('power supply', 1),
        ('aluminum', 6)
    ),
    'processor': (
        ('aluminum', 2),
        ('circuit', 2)
    ),
    'power supply': (
        ('copper wire', 3),
        ('circuit', 1),
        ('iron wire', 3)
    ),
    'circuit': (
        ('copper wire', 2),
        ('gold', 1)
    ),
    'aluminum': (),
    'copper wire': (),
    'iron wire': (),
    'gold': ()
}

def _resolve(thing, count=1):
    recipe = []

    if not recipes[thing]:
        recipe.append((thing, count))
    else:
        for comp, req in recipes[thing]:
            resolved = _resolve(comp, req*count)

            unmarked = True
            for i in resolved:
                for j in recipe:
                    if resolved[i] == recipe[j]:
                        recipe[j] = (recipe[j][0] + resolved[i][0], recipe[j][1] + resolved[i][1])
                        unmarked = False
            if unmarked:
                recipe.extend(resolved)

    return recipe


def resolve(thing):
    '''This is a convenience function that takes carea of rounding
    up fractional amounts to integer values (so if your recipe
    only takes 0.75 wood, this will transform that to 1 wood,
    because you can't use fractional amounts of things).'''
    return [(item, int(math.ceil(count)))
            for item, count in _resolve(thing, 1)]



def main():
    print(resolve('computer'))

if __name__ == '__main__':
    main()

    