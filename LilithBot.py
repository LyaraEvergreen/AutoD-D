from random import randint
def d8(): return(randint(1,8))
def d10(): return(randint(1,10))
def d20(): return(randint(1,20))

profBonus, dexMod= 4, 5
weaponMod = 0
toHit = profBonus + dexMod + weaponMod
crit, atRange = 0, 2
hitLastAtk, advantage = 0, 0
combatRound = 1
actionSurge, surging = True, False
dancing = False
hitLastAtk = 0
usingFire = False

def hitDice():
    if usingFire: return d10
    else: return d8

def damageType():
    if usingFire: return "fire" 
    else: return "slashing"

def rollD20(): 
    roll = max(d20(), d20() * max(hitLastAtk, advantage))
    return(roll)

def makeAttacks():
    # Attack One
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 1st attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange),damageType()))
        hitLastAtk = 1
    else:
        print("Rolled {0} for the first attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
        if input("Hit? ").lower().strip()  in ["yes","y"]:
            hitLastAtk = 1
        else: hitLastAtk = 0

    # Attack Two
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 2nd attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange), damageType()))
    else:
        print("Rolled {0} for the second attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
    hitLastAtk = 0

    if not surging:
        # Attack Three
        roll = rollD20()
        if(roll == 20):
            print("Nat 20 on the 3rd attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange),damageType()))
            hitLastAtk = 1
        else:
            print("Rolled {0} for the third attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
            if input("Hit? ").lower().strip()  in ["yes","y"]:
                hitLastAtk = 1
            else: hitLastAtk = 0

        if dancing:
            # Attack four
            roll = rollD20()
            if(roll == 20):
                print("Nat 20 on the 4th attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange),damageType()))
            else:
                print("Rolled {0} for the fourth attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
            hitLastAtk = 0

def makeBonusAttacks(dancing):
    # Attack One
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 1st bonus attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange),damageType()))
        hitLastAtk = 1
    else:
        print("Rolled {0} for the first bonus attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
        if input("Hit? ").lower().strip()  in ["yes","y"]:
            hitLastAtk = 1
        else: hitLastAtk = 0
    
    if ((dancing) and input("End your dance to make another attack? ").lower().strip() in ["y","yes"]):
        # Attack Two
        roll = rollD20()
        if(roll == 20):
            print("Nat 20 on the 2nd bonus attack.\t| Damage: {0} {1}".format(2*hitDice()() + dexMod + weaponMod + (2 * atRange),damageType()))
        else:
            print("Rolled {0} for the second bonus attack\t| Damage: {1} {2}".format(roll + toHit, hitDice()() + dexMod + weaponMod + (2*atRange),damageType()))
        hitLastAtk = 0
        dancing = 0

inCombat = (input("In Fight? ").lower().strip()  in ["yes","y"])
while inCombat:
    print("Round {0}".format(combatRound))
    usingFire = input("Ignite fans? ").lower().strip() in ["y","yes"]
    if (dancing):
        if (input("Still Dancing? ").lower().strip() in ["yes","y"]):
            next
        else:
            dancing = False
        started = False
    else:
        if (input("Start Dancing? ").lower().strip()  in ["yes","y"]):
            dancing = True
            started = True
        else: started = False
    if(input("Attacking with advantage? ").lower().strip()  in ["yes","y"]): 
        advantage = 1
    
    makeAttacks()

    if(not started):
        if (input("Make a bonus action attack? ").lower().strip() in ["y","yes"]):
            makeBonusAttacks(dancing)

    if (actionSurge):
        if (input("Would you like to Action Surge? ").lower().strip() in ["y","yes"]):
            surging = True
            makeAttacks()
            actionSurge, surging = False, False
    
    advantage = 0
    combatRound += 1
    inCombat = (input("Still fighting? ").lower().strip() in ["yes","y"])