# Import classes from your brand new package
from animals import Mammals
from animals import Birds

# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()


#Second part of exercise
import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()
