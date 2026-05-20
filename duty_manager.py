import data, utils

def get_soldier_duties(ma:int):
    for soldier in data.soldier_list:
        if soldier["ma"] == ma:
            return soldier["duties"]
    raise KeyError(f"No soldier found with ma: {ma}")


def add_duty_to_soldier(ma: int, duty_name: str, day: str) -> None:
    if not utils.is_valid_ma(ma):
        raise ValueError(f"ma {ma} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(duty_name):
        raise ValueError(f"name {duty_name} is not valid, should be str 1 - 20 chars")
    elif not utils.is_valid_day(day):
        raise ValueError(f"day: {day} is not out of sonday-thursday")
    
    soldier, index = utils.find_soldier_by_id(ma)
    if not soldier:
        raise ValueError(f"ma {ma} was not found in the database")
    if utils.soldier_has_duty(soldier, duty_name):
        raise ValueError(f"soldier - {soldier["name"]} allready has duty: {duty_name}.")
    
    soldier["duties"].append({"name":duty_name, "day":day, "status":"pending"})


def update_duty_status(ma: int, duty_name: str, new_status: str) -> None:
    if not utils.is_valid_ma(ma):
        raise ValueError(f"ma {ma} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(duty_name):
        raise ValueError(f"name {duty_name} is not valid, should be str 1 - 20 chars")
    elif not utils.is_valid_status(new_status):
        raise ValueError(f"new status: {new_status} is not out of pending / completed / missed")
    
    soldier, index = utils.find_soldier_by_id(ma)
    if not soldier:
        raise ValueError(f"ma {ma} was not found in the database")
    if not utils.soldier_has_duty(soldier, duty_name):
        raise ValueError(f"soldier - {soldier["name"]} does not have duty: {duty_name}.")
    
    soldier[3]["status"] = new_status

    
    