import data, utils

def get_soldier_duties(ma:int):
    for soldier in data.soldier_list:
        if soldier["ma"] == ma:
            return soldier
    raise KeyError(f"No soldier found with ma: {ma}")


def add_duty_to_soldier(ma: int, duty_name: str, day: str, status:str) -> None:
    if not utils.is_valid_ma(ma):
        raise ValueError(f"ma {ma} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(duty_name):
        raise ValueError(f"name {duty_name} is not valid, should be str 1 - 20 chars")
    elif not utils.is_valid_day(day):
        raise ValueError(f"day: {day} is not out of sonday-thursday")
    elif not utils.is_valid_status(status):
        raise ValueError(f"status: {status} is not out of pending / completed / missed")
    
    soldier, index = utils.find_soldier_by_id(ma)
    if not soldier:
        raise ValueError(f"ma {ma} was not found in the database")
    if utils.soldier_has_duty(soldier, duty_name):
        raise ValueError(f"soldier - {soldier["name"]} allready has duty: {duty_name}.")
    
    soldier[3].append({"name":duty_name, "day":day, "status":status})
    
    