import math

people = {
    "untrained": {
        "name": "untrained person",
        "con_stat": 10,
        "skill": 3,
        "buffer": 1
    },
    "highschool": {
        "name": "high school runner",
        "con_stat": 14,
        "skill": 10,
        "buffer": 1
    },

    "peak_human": {
        "name": "professional runner",
        "con_stat": 18,
        "skill": 74,
        "buffer": 1
    },

    "adventurer": {
        "name": "Abantey Adventurer",
        "con_stat": 16,
        "skill": 18,
        "buffer": 1
    },
    "wala": {
        "name": "WaLa Runner",
        "con_stat": 20,
        "skill": 76,
        "buffer": 1
    }
}


#
# important stuffs 
#

old_constants = {
        "walk": [30, 1, "min"],
        "trot": [2, .0833, "min"], 
        "run": [60, 5, "sec"], 
        "sprint": [2, 1, "sec"], 
    }

test_constants = {
        "walk": [1, 1, "hrs"], 
        "trot": [1, 15, "min"], 
        "run": [.5, 5, "min"], 
        "sprint": [2, 2, "sec"], 
    }

def old_max_time(type, person):
    constants = old_constants
    return constants[type][0] * (person["con_stat"]) + person["skill"]*constants[type][1]

def new_max_time(type, person):
    constants = test_constants
    return constants[type][0] * (person["con_stat"]) + person["skill"]*constants[type][1]

#
#
#
print("Testing formula:")
print("Time = (base * CON) + (scale * physical skill)")

print("\nOld Constants")
print("".ljust(10, "_"),"Scale".ljust(10, "_"), "Base".ljust(10, "_"), "+Per Skill Point".ljust(20, "_"))
for i in old_constants:
   print(str(i).ljust(10),old_constants[i][2].ljust(10), str(old_constants[i][0]).ljust(10), str(old_constants[i][1]).ljust(20))

print("\nNew Constants")
print("".ljust(10, "_"),"Scale".ljust(10, "_"), "Base".ljust(10, "_"), "+Per Skill Point".ljust(20, "_"))
for i in test_constants:
   print(str(i).ljust(10),test_constants[i][2].ljust(10), str(test_constants[i][0]).ljust(10), str(test_constants[i][1]).ljust(20))


print("\nOLD SYSTEM")
print("Person".ljust(20, "_"), "Walk".ljust(10, "_"), "Trot".ljust(10, "_"), "Run".ljust(10, "_"), "Sprint".ljust(10, "_"))
for p in people:
    sprint = f"{old_max_time('sprint', people[p])} sec".ljust(10)
    run = f"{round(old_max_time('run', people[p])/60,1)} min".ljust(10)
    trot = f"{round(old_max_time('trot', people[p]), 1)} min".ljust(10)
    walk = f"{round(old_max_time('walk', people[p])/60, 1)} hours".ljust(10)
    print(people[p]["name"].ljust(20),walk, trot, run, sprint)

print("\nTEST SYSTEM")
print("Person".ljust(20, "_"), "Walk".ljust(10, "_"), "Trot".ljust(10, "_"), "Run".ljust(10, "_"), "Sprint".ljust(10, "_"))
for p in people:
    sprint = f"{new_max_time('sprint', people[p])} sec".ljust(10)
    run = f"{round(new_max_time('run', people[p]),1)} min".ljust(10)
    trot = f"{round(new_max_time('trot', people[p])/60, 1)} hours".ljust(10)
    walk = f"{round(new_max_time('walk', people[p]), 1)} hours".ljust(10)
    print(people[p]["name"].ljust(20),walk, trot, run, sprint)