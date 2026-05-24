MAX_ID = 1000000000
MIN_ID = 1
MAX_LEN_NAME = 20
MIN_LEN_NAME = 1

def is_valid_name(name: str) -> bool:
    """
    check if name is valid - len between 1 to 20
    gets: str
    returns: bool
    """
    return MIN_LEN_NAME <= len(name) <= MAX_LEN_NAME 
    

def is_valid_soldier_id(soldier_id:int):
    """
    check if id is valid - number between 1 to 1000000000
    gets: int
    returns: bool
    """
    return MIN_ID <= soldier_id < MAX_ID


def find_soldier_by_id(all_soldiers:list, soldier_id):
    """
    searches for soldier by id
    get: list, int
    return: dict, int
    """
    for index, soldier in enumerate(all_soldiers):
        if soldier["soldier_id"] == soldier_id:
            return soldier, index
    return None, None


def is_valid_day(status: str) -> bool:
    """
    check if day is valid - day between sunday-thursdsay
    gets: str
    returns: bool
    """
    return status.lower() in ["sunday", "monday", "tuesday", "wednesday", "thursday"]


def is_valid_status(status: str) -> bool:
    """
    check if status is valid - day between pending/completed/missed
    gets: str
    returns: bool
    """
    return status.lower() in [ "pending", "completed", "missed"]


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    check if soldier already has duty with this name
    gets: dict, str
    returns: bool
    """
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    check if duty list already has duty with this name
    gets: list, str
    returns: dict
    """
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None

          
