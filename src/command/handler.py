import json
import sys
import random

actions = [
    'rotate-left',
    'rotate-right',
    'advance',
    'retreat',
    'shoot',
    'pass',
]

def pingu_in_sight(data):
    return False

# Check for nearby objects
def is_dangerous(data, action):
    return False

def get_random_action(data):
    # we don't want to do "pass"
    unicorns = set(actions) - set(['pass'])

    while True:
        action = random.choice(tuple(unicorns))

        if not is_dangerous(data, action):
            break

    return action

def shoot(data):
    return 'shoot'

# The function that decides the move..
def get_command(data):
    # Sjekk om fienden ser på oss og om vi ser på dem (og vi kan skyte)
    if pingu_in_sight(data):
        # funksjon som kalles dersom vi er på linje sammen med fiende
        return shoot(data)
    else:
        return get_random_action(data)

def handle(req):
    """
    {
      matchId: string, // unik kamp-ID
      mapWidth: int,
      mapHeight: int,
      suddenDeath: int, // antall runder til sudden death starter
      wallDamage: int, // hvor mye skade som pingvinen tar av å gå inn i veggen
      penguinDamage: int, // hvor mye skade pingvinen tar av å krasje med en annen pingvin -- også hvor mye skade pingvinen din gjør på veggen når den krasjer med den
      weaponDamage: int, // hvor mye skade pingvinen tar av å bli skutt
      visibility: int, // avstanden i felt du kan se på radaren
      weaponRange: int, // avstranden i felt pingvinens laser rekker
      you: PENGUIN, // informasjon om din pingvin -- se pingvinstrukturen nedenfor
      enemies: [PENGUIN], // array. fiendlige pingviner. se struktur nedenfor
      bonusTiles: [BONUS], array. felter som inneholder bonuser. se bonusstruktur nedenfor
      walls: [WALL], // array. synlige vegger. se vegg-struktur nedenfor
      fire: [FIELD] // array, synlige felt som brenner
    }
    """
    data = json.loads(req)

    return json.dumps({'command': get_command(data)})

if __name__ == '__main__':
    rawdata = sys.stdin.read()

    print(handle(rawdata))
