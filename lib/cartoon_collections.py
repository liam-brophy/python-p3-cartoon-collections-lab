def roll_call_dwarves(dwarves):
    for index, name in enumerate(dwarves, start=1):
        print(f"{index}. {name}")

def summon_captain_planet(palaneteer_calls):
    summons = [call.capitalize() + "!" for call in palaneteer_calls]
    return summons

def long_planeteer_calls(calls):
 for call in calls:
    if len(call) > 4:
        return True
 return False

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            return food
    return None
