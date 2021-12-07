import statistics
import math

crabs = [int(crab) for crab in open("Data/aoc_07.txt").read().split(",")]
print(f"Answer 1: {sum(abs(crab - statistics.median(crabs)) for crab in crabs)}")
print(f"Answer 2: {sum(((distance**2)+distance)/2 for distance in [abs(crab - math.floor(statistics.mean(crabs))) for crab in crabs])}")


