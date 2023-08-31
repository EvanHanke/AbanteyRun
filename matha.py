import matplotlib.pyplot as plt
import numpy as np

people = {
    "minimum": {
        "name": "7 year old",
        "con_stat": 6,
        "skill": 0,
        "level": 0,
        "stb": 0
    },
    "untrained": {
        "name": "untrained person",
        "con_stat": 10,
        "skill": 3,
        "level": 1,
        "stb": 0
    },
    "highschool": {
        "name": "high school runner",
        "con_stat": 14,
        "skill": 10,
        "level": 1,
        "stb": 0
    },

    "peak_human": {
        "name": "professional runner",
        "con_stat": 18,
        "skill": 74,
        "level": 5,
        "stb": 4
    },

    "adventurer": {
        "name": "Abantey Adventurer",
        "con_stat": 16,
        "skill": 18,
        "level": 2,
        "stb": 2
    },
    "wala": {
        "name": "WaLa Runner",
        "con_stat": 24,
        "skill": 76,
        "level": 5,
        "stb": 10
    }
}


#
# data area
#

old_constants = {
        "walk": [30, 1, "min"],
        "trot": [2, .0833, "min"], 
        "run": [60, 5, "sec"], 
        "sprint": [2, 1, "sec"], 
    }

test_constants = {
        "walk": [1, 'n/a', "hrs"], 
        "trot": [4, 'n/a', "hours"], 
        "run": [.25, 'n/a', "min"], 
        "sprint": [.5, 'n/a', "sec"], 
    }

def old_max_time(type, person):
    constants = old_constants
    return constants[type][0] * (person["con_stat"]) + person["skill"]*constants[type][1]

def new_max_time(type, person):
    constants = test_constants
    return (1+(person["level"]+person["stb"]+person["skill"]))/constants[type][0]

#
# end data area
#

#
# test area below
#
print("\nAbantey Run Test\n")
print("Testing formula:")
print("Time = (1+level+con_stb+resist_skill)/constant")

def PrintOldC():
    print("\nOld Constants")
    print("".ljust(10, "_"),"Scale".ljust(10, "_"), "Denominator".ljust(10, "_"), "+Per Physical Skill".ljust(20, "_"))
    for i in old_constants:
        print(str(i).ljust(10),old_constants[i][2].ljust(10), str(old_constants[i][0]).ljust(10), str(old_constants[i][1]).ljust(20))

def PrintNewC():
    print("\nNew Constants")
    print("".ljust(10, "_"), "Scale".ljust(10, "_"), "Base".ljust(10, "_"),"+Per Skill Point".ljust(20, "_"))
    for i in test_constants:
        print(str(i).ljust(10),test_constants[i][2].ljust(10), str(test_constants[i][0]).ljust(10), str(test_constants[i][1]).ljust(20))

def TestOld():
    print("\nOld Values")
    print("Person".ljust(20, "_"), "Walk".ljust(10, "_"), "Trot".ljust(10, "_"), "Run".ljust(10, "_"), "Sprint".ljust(10, "_"))
    for p in people:
        sprint = f"{old_max_time('sprint', people[p])} sec".ljust(10)
        run = f"{round(old_max_time('run', people[p])/60,1)} min".ljust(10)
        trot = f"{round(old_max_time('trot', people[p]), 1)} min".ljust(10)
        walk = f"{round(old_max_time('walk', people[p])/60, 1)} hours".ljust(10)
        print(people[p]["name"].ljust(20),walk, trot, run, sprint)

def TestNew():
    print("\nNew Values")
    print("Person".ljust(20, "_"), "Walk".ljust(10, "_"), "Trot".ljust(10, "_"), "Run".ljust(10, "_"), "Sprint".ljust(10, "_"))
    for p in people:
        sprint = f"{round(new_max_time('sprint', people[p]),1)} sec".ljust(10)
        run = f"{round(new_max_time('run', people[p]),1)} min".ljust(10)
        trot = f"{round(new_max_time('trot', people[p]), 1)} hours".ljust(10)
        walk = f"{round(new_max_time('walk', people[p]), 1)} hours".ljust(10)
        print(people[p]["name"].ljust(20),walk, trot, run, sprint)

PrintNewC()
TestNew()


def plot(speed= "walk", scale="hours", sample = ["untrained", "adventurer","peak_human", "wala"]):
    x = np.arange(0, 72, 8)
    for p in sample:
        times = []
        for i in x:
            people[p]["skill"] = i
            times.append(new_max_time(speed, people[p]))
        plt.plot(x, times, marker='o', linestyle='-', label=people[p]["name"])
    # Add labels and title
    plt.xlabel('Resist Skill+')
    plt.ylabel(f'{speed.capitalize()} time ({scale})')
    plt.title(f'{speed.capitalize()} Time per Resist skill+')

    # Add a legend
    plt.legend()

    # Display the plot
    #plt.show()
    plt.savefig(f"{speed}_plot.png")
    plt.close()

plot("walk")
plot("trot")
plot("run")
plot("sprint")