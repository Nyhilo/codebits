#Imports
from random import randint

class Player(object):
    """docstring for Player"""

    # Stats Setters
    def setStrength(self, value): self.strength = value 
    def setDexterity(self, value): self.dexterity = value 
    def setVitality(self, value): self.vitality = value 
    def setEndurance(self, value): self.endurance = value 
    def setResistance(self, value): self.resistance = value 
    def setWisdom(self, value): self.wisdom = value 
    def setCharisma(self, value): self.charisma = value 
    def setIntimidation(self, value): self.intimidation = value 
    def setKnowledge(self, value): self.knowledge = value 
    def setFaith(self, value): self.faith = value 
    def setAttractiveness(self, value): self.attractiveness = value 
    def setWillpower(self, value): self.willpower = value 
    def setCuriosity(self, value): self.curiosity = value 
    def setInstinct(self, value): self.instinct = value 
    def setFriendliness(self, value): self.friendliness = value 
    def setDestiny(self, value): self.destiny = value 

    # Combined Stats Setters
    def setAwareness(self): self.awareness = self.wisdom*.6 + self.curiosity*.2 + self.instinct*.2
    def setReflexes(self): self.reflexes = self.awareness*.3 + self.dexterity*.6 + self.instinct*.1
    def setDeceit(self): self.deceit = self.charisma*.5 + self.friendliness*.2 + self.instinct*.1 + self.attractiveness*.2
    def setFocus(self): self.focus = self.wisdom*.6 + self.willpower*.4 + self.instinct*.2 - self.curiosity*.2
    def setDefense(self): self.defense = self.resistance*.6 + self.vitality*.3 + self.willpower*.1
    def setIntelligence(self): self.intelligence = self.knowledge*.8 + self.curiosity *.1 + self.wisdom*.1
    def setStamina(self): self.stamina = self.vitality*.6 + self.endurance*.4
    def setEvasion(self): self.evasion = self.awareness*.4 + self.reflexes*.6
    def setSpeed(self): self.speed = self.dexterity*.7 + self.strength*.3
    def setForm(self): self.form = self.wisdom*.1 + self.intelligence*.2 + self.dexterity*.7
    def setLift(self): self.lift = self.strength*.8 + self.form*.2
    def setLatentMagic(self): self.latentMagic = self.vitality*.4 + self.destiny*.4 + self.instinct*.2
    def setPracticedMagic(self): self.practicedMagic = self.intelligence*.8 + self.wisdom*.1 + self.focus*.1
    def setDivineMagic(self): self.divineMagic = self.faith*.7 + self.destiny*.1 + self.charisma*.2
    def setPerformanceMagic(self): self.performanceMagic = self.charisma*.7 + self.intelligence*.15 + self.dexterity*.15
    def setStrike(self): self.strike = self.strength*.8 + self.dexterity*.1 + self.instinct*.1
    def setSlash(self): self.slash = self.dexterity*.7 + self.strength*.1 + self.instinct*.1 + self.knowledge*.1
    def setThrust(self): self.thrust = self.dexterity*.6 + self.strength*.3 + self.instinct*.1
    def setPoise(self): self.poise = self.form*.5 + self.focus*.3 + self.endurance*.2
    def setDiplomacy(self): self.diplomacy = self.charisma*.5 + self.friendliness*.4 + self.instinct*.1

    #Stat Getters
    def str(self, value=None): return self.strength if value is None else self.setStrength(value)  
    def dex(self, value=None): return self.dexterity if value is None else self.setDexterity(value)  
    def vit(self, value=None): return self.vitality if value is None else self.setVitality(value)  
    def end(self, value=None): return self.endurance if value is None else self.setEndurance(value)  
    def res(self, value=None): return self.resistance if value is None else self.setResistance(value)  
    def wis(self, value=None): return self.wisdom if value is None else self.setWisdom(value)  
    def cha(self, value=None): return self.charisma if value is None else self.setCharisma(value)  
    def ind(self, value=None): return self.intimidation if value is None else self.setIntimidation(value)  
    def kno(self, value=None): return self.knowledge if value is None else self.setKnowledge(value)  
    def fai(self, value=None): return self.faith if value is None else self.setFaith(value)  
    def atr(self, value=None): return self.attractiveness if value is None else self.setAttractiveness(value)  
    def wil(self, value=None): return self.willpower if value is None else self.setWillpower(value)  
    def cur(self, value=None): return self.curiosity if value is None else self.setCuriosity(value)  
    def ins(self, value=None): return self.instinct if value is None else self.setInstinct(value)  
    def frn(self, value=None): return self.friendliness if value is None else self.setFriendliness(value)  
    def des(self, value=None): return self.destiny if value is None else self.setDestiny(value)  
    def awr(self, value=None): return self.awareness if value is None else self.setAwareness(value)  
    def ref(self, value=None): return self.reflexes if value is None else self.setReflexes(value)  
    def dec(self, value=None): return self.deceit if value is None else self.setDeceit(value)  
    def foc(self, value=None): return self.focus if value is None else self.setFocus(value)  
    def dfn(self, value=None): return self.defense if value is None else self.setDefense(value)  
    def int(self, value=None): return self.intelligence if value is None else self.setIntelligence(value)  
    def sta(self, value=None): return self.stamina if value is None else self.setStamina(value)  
    def eva(self, value=None): return self.evasion if value is None else self.setEvasion(value)  
    def spd(self, value=None): return self.speed if value is None else self.setSpeed(value)  
    def frm(self, value=None): return self.form if value is None else self.setForm(value)  
    def lft(self, value=None): return self.lift if value is None else self.setLift(value)  
    def ltmag(self, value=None): return self.latentMagic if value is None else self.setLatentMagic(value) 
    def prmag(self, value=None): return self.practicedMagic if value is None else self.setPracticedMagic(value) 
    def dvmaj(self, value=None): return self.divineMagic if value is None else self.setDivineMagic(value) 
    def pfmag(self, value=None): return self.performanceMagic if value is None else self.setPerformanceMagic(value) 
    def stk(self, value=None): return self.strike if value is None else self.setStrike(value)  
    def sls(self, value=None): return self.slash if value is None else self.setSlash(value)  
    def thr(self, value=None): return self.thrust if value is None else self.setThrust(value)  
    def poi(self, value=None): return self.poise if value is None else self.setPoise(value)
    def dip(self, value=None): return self.diplomacy if value is None else self.setDiplomacy(value)
   
    # Methods
    def update(self):
        self.setAwareness()
        self.setReflexes()
        self.setDeceit()
        self.setFocus()
        self.setDefense()
        self.setIntelligence()
        self.setStamina()
        self.setEvasion()
        self.setSpeed()
        self.setForm()
        self.setLift()
        self.setLatentMagic()
        self.setPracticedMagic()
        self.setDivineMagic()
        self.setPerformanceMagic()
        self.setStrike()
        self.setSlash()
        self.setThrust()
        self.setPoise()
        self.setDiplomacy()

    def rollstat(self):
        value = randint(4,24)
        return value

    def rollstats(self):
        self.strength = self.rollstat()
        self.dexterity = self.rollstat()
        self.vitality = self.rollstat()
        self.endurance = self.rollstat()
        self.resistance = self.rollstat()
        self.wisdom = self.rollstat()
        self.charisma = self.rollstat()
        self.intimidation = self.rollstat()
        self.knowledge = self.rollstat()
        self.faith = self.rollstat()
        self.attractiveness = self.rollstat()
        self.willpower = self.rollstat()
        self.curiosity = self.rollstat()
        self.instinct = self.rollstat()
        self.friendliness = self.rollstat()
        self.destiny = self.rollstat()
        self.update()

    def pnt(self):
        BaseStats = ["{:15} {}".format("name:", self.name),
            "{:15} {}".format("strength:", self.strength),
            "{:15} {}".format("dexterity:", self.dexterity),
            "{:15} {}".format("vitality:", self.vitality),
            "{:15} {}".format("endurance:", self.endurance),
            "{:15} {}".format("resistance:", self.resistance),
            "{:15} {}".format("wisdom:", self.wisdom),
            "{:15} {}".format("charisma:", self.charisma),
            "{:15} {}".format("intimidation:", self.intimidation),
            "{:15} {}".format("knowledge:", self.knowledge),
            "{:15} {}".format("faith:", self.faith),
            "{:15} {}".format("attractiveness:", self.attractiveness),
            "{:15} {}".format("willpower:", self.willpower),
            "{:15} {}".format("curiosity:", self.curiosity),
            "{:15} {}".format("instinct:", self.instinct),
            "{:15} {}".format("friendliness:", self.friendliness),
            "{:15} {}".format("destiny:", self.destiny)]

        CombStats = ["{:15} {}".format("awareness:", int( self.awareness )),
            "{:15} {}".format("reflexes:", int( self.reflexes )),
            "{:15} {}".format("deceit:", int( self.deceit )),
            "{:15} {}".format("focus:", int( self.focus )),
            "{:15} {}".format("defense:", int( self.defense )),
            "{:15} {}".format("intelligence:", int( self.intelligence )),
            "{:15} {}".format("stamina:", int( self.stamina )),
            "{:15} {}".format("evasion:", int( self.evasion )),
            "{:15} {}".format("speed:", int( self.speed )),
            "{:15} {}".format("form:", int( self.form )),
            "{:15} {}".format("lift:", int( self.lift )),
            "{:15} {}".format("latentMagic:", int( self.latentMagic )),
            "{:15} {}".format("practicedMagic:", int( self.practicedMagic )),
            "{:15} {}".format("divineMagic:", int( self.divineMagic )),
            "{:15} {}".format("performMagic:", int( self.performanceMagic )),
            "{:15} {}".format("strike:", int( self.strike )),
            "{:15} {}".format("thrust:", int( self.thrust )),
            "{:15} {}".format("poise:", int( self.poise )),
            "{:15} {}".format("diplomacy:", int( self.diplomacy ))]

        while len(BaseStats) < len(CombStats): BaseStats.append("")
        while len(BaseStats) < len(CombStats): CombStats.append("")

        for BS, CS in zip(BaseStats, CombStats):
            print("{:25} {}".format(BS, CS))

    def rank(self, stat, x=1):
        result = {
            "str" : lambda x: self.setStrength( self.strength + x ),
            "dex" : lambda x: self.setDexterity( self.dexterity + x ),
            "vit" : lambda x: self.setVitality( self.vitality + x ),
            "end" : lambda x: self.setEndurance( self.endurance + x ),
            "res" : lambda x: self.setResistance( self.resistance + x ),
            "wis" : lambda x: self.setWisdom( self.wisdom + x ),
            "cha" : lambda x: self.setCharisma( self.charisma + x ),
            "ind" : lambda x: self.setIntimidation( self.intimidation + x ),
            "kno" : lambda x: self.setKnowledge( self.knowledge + x ),
            "fai" : lambda x: self.setFaith( self.faith + x ),
            "atr" : lambda x: self.setAttractiveness( self.attractiveness + x ),
            "wil" : lambda x: self.setWillpower( self.willpower + x ),
            "cur" : lambda x: self.setCuriosity( self.curiosity + x ),
            "ins" : lambda x: self.setInstinct( self.instinct + x ),
            "frn" : lambda x: self.setFriendliness( self.friendliness + x ),
            "des" : lambda x: self.setDestiny( self.destiny + x )
        }[stat](x)

        self.update()

    def setBase(self, value):
        self.setStrength( value )
        self.setDexterity( value )
        self.setVitality( value )
        self.setEndurance( value )
        self.setResistance( value )
        self.setWisdom( value )
        self.setCharisma( value )
        self.setIntimidation( value )
        self.setKnowledge( value )
        self.setFaith( value )
        self.setAttractiveness( value )
        self.setWillpower( value )
        self.setCuriosity( value )
        self.setInstinct( value )
        self.setFriendliness( value )
        self.setDestiny( value )
        self.update()

    def __init__(self, name="Unnamed"):
        super(Player, self).__init__()
        # Character Info
        self.name = name

        # Base stats
        self.strength = 0
        self.dexterity = 0
        self.vitality = 0
        self.endurance = 0
        self.resistance = 0
        self.wisdom = 0
        self.charisma = 0
        self.intimidation = 0
        self.knowledge = 0
        self.faith = 0
        self.attractiveness = 0
        self.willpower = 0

        # Static Stats
        self.curiosity = 0
        self.instinct = 0
        self.friendliness = 0
        self.destiny = 0

        # Combined stats
        self.awareness = 0
        self.reflexes = 0
        self.deceit = 0
        self.focus = 0
        self.defense = 0
        self.intelligence = 0
        self.stamina = 0
        self.evasion = 0
        self.speed = 0
        self.form = 0
        self.lift = 0
        self.latentMagic = 0
        self.practicedMagic = 0
        self.divineMagic = 0
        self.performanceMagic = 0
        self.strike = 0
        self.slash = 0
        self.thrust = 0
        self.poise = 0
        self.diplomacy = 0


def main():
    char = Player()
    char.setBase(10)
    char.str(20)
    char.pnt()

if __name__ == '__main__':
    main()