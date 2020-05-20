import csv
import random

roulette = []
# using a file "topics.csv"
with open("topics.csv", newline="") as file:
    reader = csv.reader(file, delimiter=",", quotechar='"')
    for row in reader:
        # exclude rows based on criteria added to index 9 and 1 of CSV
        if row[9] == "" and row[1] != "":
            # with index number at index[0], Title at index[1] and Description at index[2]
            roulette.append(
                "You should write about topic: "
                + row[0]
                + " - "
                + row[1]
                + "\n"
                + row[2]
            )

# Return random row according to the format set in the for loop
print(random.choice(roulette))
