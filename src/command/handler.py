import json
import sys
from makeMove import makeMove

def walk(data):
    pass

def get_command(data):
    print(data)
    doer = makeMove(
        mypos    = [data['you']['x'], data['you']['y']],
        mydir    = data['you']['direction'],
        myhp     = data['you']['strength'],
        myrange  = data['you']['weaponRange'],
        mydamage = data['you']['weaponDamage'],
    )

    action = doer.doSomething(
        enemydata = [
            data['enemies'][0]['x'], data['enemies'][0]['y'],
            data['enemies'][0]['strength'],
            data['enemies'][0]['direction'],
            data['enemies'][0]['ammo'],
            data['enemies'][0]['weaponRange'],
            data['enemies'][0]['weaponDamage'],
        ],
        bonusdata = True,
        walls     = True,
        fire      = True,
    )

    return action

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
