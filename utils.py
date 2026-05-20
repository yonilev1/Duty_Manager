MAX_ID = 1000000000
MIN_ID = 1
MAX_LEN_NAME = 20
MIN_LEN_NAME = 1

def is_valid_name(name: str) -> bool:
    return MIN_LEN_NAME <= len(name) <= MAX_LEN_NAME 
    

def is_valid_soldier_id(soldier_id:int):
    return MIN_ID <= soldier_id < MAX_ID


def find_soldier_by_id(all_soldiers:list, soldier_id):
    for index, soldier in enumerate(all_soldiers):
        if soldier["soldier_id"] == soldier_id:
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

          
