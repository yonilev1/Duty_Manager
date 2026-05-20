import data

def is_valid_name(name: str) -> bool:
    return 0 < len(name) <= 20 
    

def is_valid_ma(ma:int):
    return ma < 1000000000


def find_soldier_by_id(ma):
    for index, soldier in enumerate(data.soldier_list):
        if soldier["ma"] == ma:
            return soldier, index
    return None, None


def is_valid_day(status: str) -> bool:
    return status.lower() in ["sunday", "monday", "tuesday", "wednesday", "thursday"]


def is_valid_status(status: str) -> bool:
    return status.lower() in [ "pending", "completed", "missed"]


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None
          
