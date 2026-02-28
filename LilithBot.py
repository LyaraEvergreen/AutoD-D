from random import randint
def d8(): return(randint(1,8))
def d20(): return(randint(1,20))

profBonus, dexMod= 3, 5
toHit = profBonus + dexMod
crit, atRange = 0, 2
hitLastAtk, advantage = 0, 0
combatRound = 1
actionSurge, surging = True, False
dancing = False

def rollD20(): 
    roll = max(d20(), d20() * max(hitLastAtk, advantage))
    return(roll)

def makeAttacks():
    # Attack One
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 1st attack.\t| Damage: {0} slashing".format(2*d8() + toHit + (2 * atRange)))
        hitLastAtk = 1
    else:
        print("Rolled {0} for the first attack\t| Damage: {1} slashing".format(roll + toHit, d8() + toHit + (2*atRange)))
        if input("Hit? ").lower().strip()  in ["yes","y"]:
            hitLastAtk = 1
        else: hitLastAtk = 0

    # Attack Two
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 2nd attack.\t| Damage: {0} slashing".format(2*d8() + toHit + (2 * atRange)))
    else:
        print("Rolled {0} for the second attack\t| Damage: {1} slashing".format(roll + toHit, d8() + toHit + (2*atRange)))
    hitLastAtk = 0

    if not surging:
        # Attack Three
        roll = rollD20()
        if(roll == 20):
            print("Nat 20 on the 3rd attack.\t| Damage: {0} slashing".format(2*d8() + toHit + (2 * atRange)))
            hitLastAtk = 1
        else:
            print("Rolled {0} for the third attack\t| Damage: {1} slashing".format(roll + toHit, d8() + toHit + (2*atRange)))
            if input("Hit? ").lower().strip()  in ["yes","y"]:
                hitLastAtk = 1
            else: hitLastAtk = 0

        if dancing:
            # Attack four
            roll = rollD20()
            if(roll == 20):
                print("Nat 20 on the 4th attack.\t| Damage: {0} slashing".format(2*d8() + toHit + (2 * atRange)))
            else:
                print("Rolled {0} for the fourth attack\t| Damage: {1} slashing".format(roll + toHit, d8() + toHit + (2*atRange)))
            hitLastAtk = 0

inCombat = (input("In Fight? ").lower().strip()  in ["yes","y"])
while inCombat:
    print("Round {0}".format(combatRound))
    if (dancing):
        if (input("Still Dancing? ").lower().strip() in ["yes","y"]):
            next
        else:
            dancing = False
    else:
        if (input("Start Dancing? ").lower().strip()  in ["yes","y"]):
            dancing = True
    if(input("Attacking with advantage? ").lower().strip()  in ["yes","y"]): 
        advantage = 1
    
    makeAttacks()

    if (actionSurge):
        if (input("Would you like to Action Surge? ").lower().strip() in ["y","yes"]):
            surging = True
            makeAttacks()
            actionSurge, surging = False, False
    
    advantage = 0
    combatRound += 1
    inCombat = (input("Still fighting? ").lower().strip() in ["yes","y"])