# This program runs a simple simulated race between 20 randomly generated drivers.
# Each driver will have a random first and last name, as well as a random sponsor.
# They will also have a random top speed for their car between 100 and 140 mph.
# At the start of the race, all drivers will have a speed of 0 and have traveled 0 miles.
# At each game tick, each driver will accelerate between -20 and 40 mph and move forward depending on their speed.
# Each tick is a minute of race time, and once a driver reaches 500 miles they will have "crosses the finish line".
# The program will then print the winner. If More than one car crosses in the same tick, it will print all of them.
# Version 1.01
# ~Jacob Cloward
# Dec 15 2014
#
# Ah nostalgia. I added a couple more outputs because I have fun looking at the  various
# random numbers this file prints out. Specifically it saves all the drivers to a named file in the
# same directory. I also added a global variable for tick speed, and made the console clear
# after every frame to get rid of a lot of the stutter. Oh, and I added a couple new names to
# the name lists.
# Version 1.02
# ~Jacob Cloward
# Dec 19 2016

from random import randint
from time import sleep
import os
import csv

numberOfRacers = 40
trackLength = 15000  # Miles
minTopSpeed = 800
maxTopSpeed = 1200
minAcceleration = -35
maxAcceleration = 80
# Items added in v1.02
tickSpeed = .1  # In seconds
outputFilename = "drivers.csv"



class Car():
    """
    Class Car describes an object used for racing.
    Contains methods that manage changes in speed and virtual movement.
    """

    def __init__(self, carNumber, odometer_miles, speed, minAccel, maxAccel, topSpeed, name, sponsor):
        """(self, float, float, list, string)"""
        self.odometer_miles = odometer_miles
        self.speed = speed
        self.name = name[0] + " " + name[1]  # Variable name is a list, this turns it into a string
        # Creates an abbreviation of name name. Ex. if the name is Chuck Donovan the abbrev is C. DONO
        self.abbrev = '{0:02d}'.format(carNumber) + ' ' + str.upper(name[1][0:4])
        self.carNumber = carNumber
        self.sponsor = sponsor
        self.topSpeed = topSpeed
        self.minAccel = minAccel
        self.maxAccel = maxAccel

    def accelerate(self):
        """
        Accelerates the vehicle between minAcceleration and maxAcceleration mph. The vehicle's speed will not drop below 0 or above self.topSpeed
        """
        acceleration = randint(self.minAccel, self.maxAccel)
        self.speed = self.speed + acceleration
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.topSpeed:
            self.speed = self.topSpeed

    def move(self):
        # self.speed/60 because ticks are measured in minutes, not hours
        self.odometer_miles += self.speed / 60

    def milesTraveled(self):
        return int(self.odometer_miles)


class GameTick():
    """Keeps track of time based variables."""

    def __init__(self):
        self.currentTick = 0  # Each tick is a minute of the race

    def increment(self):
        self.currentTick += 1

    def getTime(self):
        # Displays the time in minutes and hours
        return str("{0:02d}:{1:02d}".format(self.currentTick // 60, self.currentTick % 60))


# Names picked by random name generator and other people in my house
firstNames = ["Joshua", "Malcom", "Sherlock", "Watson", "McKinley", "Brutus", "Sally", "Kathleen", "Christopher",
              "Ursula", "Wallie", "Vincent", "Jarool", "Joe", "Lauren", "Chuck", "Kieth", "Donald", "Alice", "Paul",
              "Jesus", "Shelby", "Pete", "John", "Sonic", "Ash"]
lastNames = ["Baker", "Gorlami", "Jarosz", "Parsons", "Douglas", "Fabishe", "Woltman", "Turing", "Halar", "Orwell",
             "Steinbeck", "Smith", "Jones", "Townsen", "Belaro", "Hedgehog", "McGarthy", "McGuire", "Donovan", "Klaus",
             "Heinz", "Hurst", "Anderson", "Wazniak", "Clark", "Ketchem"]
sponsors = ["Oreo", "Soap Box", "Comcast", "UAT", "Nintendo", "Microsoft", "Sony", "General Motors", "IBM", "LG",
            "S.H.I.E.L.D", "The Hidden Leaf Village", "Guppy the Cat", "Ubrella Corporation", "Bacon",
            "Aperture Laboratories", "Crocker Corp", "NELA", "Delicious Fudge", "The Beta Kids", "Guy Fieri",
            "Eric's Exotic Wares", "The Activity Club", "The Templars", "Annet", "The Emporer"]

def newName(firstNameList, lastNameList):
    """Generates a new name based off of a list of first and a list of last names."""
    first = firstNameList[randint(0, len(firstNameList) - 1)]
    last = lastNameList[randint(0, len(lastNameList) - 1)]
    return [first, last]


def newSponsor(sponsorlist):
    """Picks a random sponsor from a list of sponsors"""
    return sponsorlist[randint(0, len(sponsorlist) - 1)]


def newTopSpeed():
    """To make the game more interesting, generates random top speed for each car"""
    return randint(minTopSpeed, maxTopSpeed)

def newMinAcceleration():
    return randint(minAcceleration, 0)    

def newMaxAcceleration():
    return randint(round(maxAcceleration/2), maxAcceleration)    

def generateDrivers(number):
    """Generates number Car objects and returns a list of them"""
    driverList = []
    for i in range(number):
        driverList.append(
            Car(i+1, 0, 0, newMinAcceleration(), newMaxAcceleration(), newTopSpeed(),
                newName(firstNames, lastNames), newSponsor(sponsors)))
    return driverList

# These next functions are all about printing text to the user

def printDrivers(racers):
    iteration = 0
    for racer in racers:
        if iteration == 0:
            print("First in the lineup is...\n")
        elif iteration == len(racers):
            print("And finally!\n")
        else:
            print("Next up on our roster...\n")

        print("{0}\n\
            Driving a car with a top speed of {1} mph!\n\
            Sponsored by {2}!\n\
            ".format(racer.name, racer.topSpeed, racer.sponsor))
        iteration += 1
        sleep(1)
    print("\n" + "-" * 15 + "\n")  # Linebreak

def exportDrivers(racers, filename):
    with open(filename, 'w', newline='') as file:
        f = csv.writer(file)
        outlist = [['Number', 'Name', 'Abbrev', 'Sponsor', 'Top Speed', 'Min Accel', 'Max Accel', 'Avg Accel', 'Win Coeff']]
        for racer in racers:
            avgAccel=racer.maxAccel+racer.minAccel
            speedRange = maxTopSpeed-minTopSpeed
            racerSpeedPlace = racer.topSpeed-minTopSpeed
            racerPlacedPercentage = (racerSpeedPlace/speedRange)
            accelRange = maxAcceleration-(maxAcceleration/2+minAcceleration)
            racerAccelPercentage = (avgAccel/accelRange)
            winCoeff=(racerPlacedPercentage+(racerAccelPercentage))/2
            outlist.append([racer.carNumber, racer.name, racer.abbrev, racer.sponsor,
                racer.topSpeed, racer.minAccel, racer.maxAccel, avgAccel, winCoeff])
        f.writerows(outlist)

def printPlace(driver):
    """(Car)
    Prints the name of driver and a '-' before it for every 10 miles that driver has driven as well as a "finish line" at space 50, and it's current speed and progress
    If driver.name = John Smith and driver.milesTraveled() = 300 then the function will print:
    ------------------------------ J. SMIT           |    110mph, 300 miles
    """
    dist = driver.milesTraveled() // 100
    print(("-" * dist) + driver.abbrev + (" " * (trackLength//100 - dist - 1)) \
          + "|    {0}mph, {1} miles".format(driver.speed, driver.milesTraveled()))


def printWelcomeMessage():
    print("Welcome to NASCAR ACTION racing!")
    print("The race is about to get under way,\nLet's take a look at today's competitors!\n")


def printEndMessage(winnerList):
    if len(winnerList) == 1:
        print("We have a winner!\nThe one who finished first was {0}!".format(
            winnerList[0].name))
    else:
        print("It would seem we have a tie!\nThe winners of this race are:")
        for car in winnerList:
            print("{0}!".format(car.name))
    print("\nThanks for watching!\nTune in next time for more NASCAR ACTION!")


def main():
    printWelcomeMessage()
    cont = input("Press the enter key to continue.\n")
    racerList = generateDrivers(numberOfRacers)
    exportDrivers(racerList, outputFilename)
    # printDrivers(racerList)

    tick = GameTick()  #Initialize the game tick
    running = True  #Setting up for a while loop
    winners = []  #There could be multiple winners
    cont = input("Press the enter key to begin the race!\n") # Wait to start the race
    while running:  #There it is!
        os.system("cls")
        print("Time:", tick.getTime())
        tick.increment()
        for car in racerList:
            printPlace(car)
            car.accelerate()
            car.move()
            if car.odometer_miles >= trackLength:
                running = False
                winners.append(car)
        # print("\n\n\n")  # Adding whitespace between each print loop makes it look like an animation.
        sleep(tickSpeed)   # Instead we clear the console to make it look better.
    printEndMessage(winners)


if __name__ == '__main__':
    main()
    exit = input("Press the enter key to exit.")