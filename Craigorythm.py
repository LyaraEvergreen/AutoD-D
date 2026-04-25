from random import randint
def d6(): return(randint(1,6))
def d8(): return(randint(1,8))
def d10(): return(randint(1,10))
def d12(): return(randint(1,12))
def d20(): return(randint(1,20))

rageDMG, profBonus, strMod, barbLvl = 2, 3, 4, 6
toHit = profBonus + strMod
reckless, rage = 0, 0
crit = 0
combatRound = 1
weaponModifier, smite, cleave, topple, graze, sap, heavy = 0, False, False, False, False, False, 0
useCharge, spearCharges = 0, 6
weapon = ""
adv = 1
actionSurge = True
damageType = ""

def rageTemp():
    temp = 0
    for i in range(rageDMG):
        temp += d6()
    return temp

def rollD20(): 
    rollOne = d20()
    if (reckless or adv): rollTwo = d20() 
    else: rollTwo = 0
    print("[{0}] [{1}]".format(rollOne,rollTwo))
    roll = max(rollOne, rollTwo)
    #print(roll)
    return(roll)

def damageDice():
    match(weapon):
        case "l":
            return max(d10(),3)
        case "h":
            return max(d10(),3)
        case "g":
            return max(d6(),3) + max(d6(),3)
        case "s":
            return max(d8(), 3) + (useCharge * max(d8(), 3))
        case "a":
            return max(d12(), 3)

def makeAttacks():
    global crit
    # Attack One
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 1st attack.\t| Damage: {0} {1}".format(2*damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier, damageType))
        crit += 1
        if topple:
            print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
        if sap:
            print("If you hit an opponent, they have disadvatage on their next attack.")
        if weapon == "a":
            print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
    else:
        print("Rolled {0} for the first attack\t| Damage: {1} {2}".format(roll + toHit + weaponModifier, damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier, damageType))
        if graze:
            print("If you missed, deal {0} {1} damage.".format(strMod, damageType))
        if topple:
            print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
        if sap:
            print("If you hit an opponent, they have disadvatage on their next attack.")
        if weapon == "a":
            print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))

    # Attack Two
    roll = rollD20()
    if(roll == 20):
        print("Nat 20 on the 2nd attack.\t| Damage: {0} {1}".format(2*damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier, damageType))
        crit += 1
        if topple:
            print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
        if sap:
            print("If you hit an opponent, they have disadvatage on their next attack.")
        if weapon == "a":
            print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
    else:
        print("Rolled {0} for the second attack\t| Damage: {1} {2}".format(roll + toHit + weaponModifier, damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier, damageType))
        if graze:
            print("If you missed, deal {0} {1} damage.".format(strMod, damageType))
        if topple:
            print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
        if sap:
            print("If you hit an opponent, they have disadvatage on their next attack.")
        if weapon == "a":
            print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
    
def hew():
    global crit
    # Hew
    if(crit > 0): 
        print("You crit an opponent so you get Hew")
        hew = True
        crit = 0
    else: 
        hew = (input("Did you reduce an opponent to 0 HP this turn? ").lower().strip()  in ["yes","y"])
    if(hew and (input("Would you like to use your bonus action to use Hew? ").lower().strip() in ["y","yes"])):
        roll = rollD20()
        if(roll == 20):
            print("Hew Crits\t| Damage: {0} {1}".format(2*damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier, damageType))
            if topple:
                print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
            if sap:
                print("If you hit an opponent, they have disadvatage on their next attack.")
            if weapon == "a":
                print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
        else:
            print("Hew rolled {0}\t| Damage: {1}".format(roll + toHit + weaponModifier, damageDice() + strMod + (heavy * profBonus) + (rageDMG * rage) + weaponModifier))
            if graze:
                print("If you missed, deal {0} {1} damage".format(strMod, damageType))
            if topple:
                print("If you hit, impose a DC{0} Con save, on a fail, they are prone".format(8 + strMod + profBonus))
            if sap:
                print("If you hit an opponent, they have disadvatage on their next attack.")
            if weapon == "a":
                print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
        

inCombat = (input("In Fight? ").lower().strip()  in ["yes","y"])
while inCombat:
    print("Round {0}".format(combatRound))
    if (rage == 1):
        if (input("Still Peeved? ").lower().strip() in ["yes","y"]):
            print("You are raged, that means more stuff, be nice and give someone {0} temp HP".format(rageTemp()))
        else:
            rage = 0
    else:
        if (input("Are you becoming peeved? ").lower().strip()  in ["yes","y"]):
            rage = 1
            print("You are raged, that means more stuff.\n{0} temp HP please\nNow be nice and give someone {1} temp HP".format(barbLvl, rageTemp()))
    if(input("Do you have advantage? ").lower().strip()  in ["yes","y"]):
        adv = 1
    else:
        if(input("Reckless attack? ").lower().strip()  in ["yes","y"]): 
            reckless = 1
            print("Enemies have advantage on attacks against you until the start of your next turn.")
    match(input("Which weapon are you choosing? (H)alberd, (L)ance, (S)pear, (A)xe or (G)reatsword? ").lower().strip()[0]):
        case "h": 
            weaponModifier = 1
            cleave = True
            weapon = "h"
            damageType = "Slashing"
            heavy = 1
        case "l":
            topple = True
            weapon = "l"
            damageType = "Pierceing"
            heavy = 1
        case "g":
            graze = True
            weapon = "g"
            damageType = "Slashing"
            heavy = 1
        case "s":
            if spearCharges > 0:    
                if input("Is you opponent scaly, squamous, or wearing scale mail or splint armour? ").lower().strip() in ["yes","y"]:
                    if input("Would you like to use a charge to add an extra damage dice (You have " + str(spearCharges) + " charges remaining)? ").lower().strip() in ["yes","y"]:
                        useCharge = 1
                        adv = 1
                        spearCharges -= 1
            weaponModifier = 1
            sap = True
            weapon = "s"
            damageType = "Piercing"
            heavy = 0
        case "a":
            cleave = True
            weapon = "a"
            damageType = "Slashing"

    
    makeAttacks()

    if (actionSurge):
        if (input("Would you like to Action Surge? ").lower().strip() in ["y","yes"]):
            makeAttacks()
            actionSurge = False
    
    if cleave:
        if (input("Do you cleave into another enemy? ").lower().strip() in ["y", "yes"]):
            roll = rollD20()
            if(roll == 20):
                print("Nat 20 on Cleave\t| Damage: {0} {1}".format(2*damageDice() + (rageDMG * rage) + profBonus + weaponModifier, damageType))
                crit += 1
                if weapon == "a":
                    print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
            else:
                print("Rolled {0} for the cleave\t| Damage: {1} {2}".format(roll + toHit + weaponModifier, damageDice() + (rageDMG * rage) + profBonus + weaponModifier, damageType))
                if weapon == "a":
                    print("Do and extra {0} damage and gain that much temp HP".format(d6()+d6()))
        
    if (smite):
        smite = input("Is your opponent still smited? ").lower().strip() in ["y","yes"]
    
    if (weapon == "h" and (not smite)):
        if (input("Would you like to use your bonus action to smite? ").lower().strip() in ["y","yes"]):
            if (input("Do they fail a DC" + str(8 + strMod + profBonus) + " Con Save? ").lower().strip() in ["y","yes"]):
                smite = True
                print("Your Smite deals {0} Fire Damage".format(d6()))
    
    if not smite:
        hew()

    reckless = 0
    weaponModifier, smite, cleave, topple, graze, sap = 0, False, False, False, False, False
    useCharge, adv = 0, 0
    combatRound += 1
    if (smite): print("Remember to make your opponent take {0} Fire damage at the start of their turn and roll a DC{1} Con Save".format(d6(), 8 + strMod + profBonus))
    inCombat = (input("Still fighting? ").lower().strip() in ["yes","y"])