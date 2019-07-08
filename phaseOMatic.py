import random

class PhaseOMatic:
    def __init__(self):
        self.wordListOne = ["24/7","multi-Tier",
        "30,000 foot","B-to-B","win-win","frontend",
        "web-based","pervasive", "smart", "sixsigma","critical-path", 
        "dynamic"]
        self.wordListTwo = ["empowered", "sticky",
        "value-added", "oriented", "centric", "distributed",
        "clustered", "branded","outside-the-box", "positioned",
        "networked", "focused", "leveraged", "aligned",
        "targeted", "shared", "cooperative", "accelerated"]
        self.wordListThree = ["process", "tippingpoint",
        "solution", "architecture", "core competency",
        "strategy", "mindshare", "portal", "space", "vision",
        "paradigm", "mission"]

    def makePhase(self):
        #lenght of each word list
        oneLength = len(self.wordListOne)
        twoLength = len(self.wordListTwo)
        threeLength = len(self.wordListThree)

        #generate random number using word list length
        rand1 = int(random.randint(0, oneLength -1))
        rand2 = int(random.randint(0, twoLength -1))
        rand3 = int(random.randint(0, threeLength -1))

        #make the phase
        phase = f"{self.wordListOne[rand1]} {self.wordListTwo[rand2]} {self.wordListThree[rand3]}" 

        return phase

phaseMaker = PhaseOMatic()
for i in range(0, 10):
    print(phaseMaker.makePhase())