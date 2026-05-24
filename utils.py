MAX_ID = 1000000000
MIN_ID = 1
MAX_LEN_NAME = 20
MIN_LEN_NAME = 1

def is_valid_name(name: str) -> bool:
    """
    check if name is valid - len between 1 to 20

    Args:
        name(str): name to check

    Returns: 
        bool: True if name is valid, else False
    """
    return MIN_LEN_NAME <= len(name) <= MAX_LEN_NAME 
    

def is_valid_soldier_id(soldier_id:int):
    """
    check if id is valid - number between 1 to 1000000000

    Args:
        soldier_id(int): id to check

    Returns: 
        bool: True if id is valid, else False
    """
    return MIN_ID <= soldier_id < MAX_ID


def find_soldier_by_id(all_soldiers:list, soldier_id:int):
    """
    searches for soldier by id

    Args:  
        all_soldiers(list): list of all soldiers
        soldier_id(int): id of target soldier

    Return:
        Dict: soldiers object
        int: index of soldier in all_soldiers, if soldier not exsits return None
    """
    for index, soldier in enumerate(all_soldiers):
        if soldier["soldier_id"] == soldier_id:
            return soldier, index
    return None, None


def is_valid_day(status: str) -> bool:
    """
    check if day is valid - day between sunday-thursdsay

    Args:
        day(str): day to check

    Returns:
        bool: True if day valid, else False
    """
    return status.lower() in ["sunday", "monday", "tuesday", "wednesday", "thursday"]


def is_valid_status(status: str) -> bool:
    """
    check if status is valid - day between pending/completed/missed

    Args:
        status(str): status to check

    Returns:
        bool: True if status valid, else False
    """
    return status.lower() in [ "pending", "completed", "missed"]


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    check if soldier already has duty with this name

    Args:
        soldier(dict): soldiers object
        duty_name(str): name of searched duty

    Returns:
        bool: True if soldier has that duty, else False
    """
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    check if duty list already has duty with this name
    
     Args:
        soldier(dict): soldiers object
        duty_name(str): name of searched duty

    Returns:
        dict: return searched duty if exsits, else None
    """
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None

          
