import data, utils

def get_soldier_duties(all_soldiers:list, soldier_id:int):
    for soldier in all_soldiers:
        if soldier["soldier_id"] == soldier_id:
            return soldier["duties"]
    raise KeyError(f"No soldier found with soldier_id: {soldier_id}")


def add_duty_to_soldier(all_soldiers:list, soldier_id: int, duty_name: str, day: str) -> None:
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(duty_name):
        raise ValueError(f"name {duty_name} is not valid, should be str 1 - 20 chars")
    elif not utils.is_valid_day(day):
        raise ValueError(f"day: {day} is not out of sonday-thursday")
    
    soldier, index = utils.find_soldier_by_id(all_soldiers, soldier_id)
    if not soldier:
        raise ValueError(f"soldier_id {soldier_id} was not found in the database")
    if utils.soldier_has_duty(soldier, duty_name):
        raise ValueError(f"soldier - {soldier["name"]} already has duty: {duty_name}.")
    
    soldier["duties"].append({"name":duty_name, "day":day, "status":"pending"})


def update_duty_status(all_soldiers:list, soldier_id: int, duty_name: str, new_status: str) -> None:
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(duty_name):
        raise ValueError(f"name {duty_name} is not valid, should be str 1 - 20 chars")
    elif not utils.is_valid_status(new_status):
        raise ValueError(f"new status: {new_status} is not out of pending / completed / missed")
    
    soldier, index = utils.find_soldier_by_id(all_soldiers, soldier_id)
    if not soldier:
        raise ValueError(f"soldier_id {soldier_id} was not found in the database")
    if not utils.soldier_has_duty(soldier, duty_name):
        raise ValueError(f"soldier - {soldier["name"]} does not have duty: {duty_name}.")
    
    duty = utils.find_duty_by_name(soldier["duties"], duty_name)
    duty["status"] = new_status

    
    