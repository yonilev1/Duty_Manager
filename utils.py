import data

def is_valid_name(name: str) -> bool:
    return 0 < len(name) <= 20 
    

def is_valid_ma(ma:int):
    return ma < 1000000000


def find_soldier_by_id(ma):
    for soldier in data.soldier_list:
        if soldier["ma"] == ma:
            return soldier
    return None


def is_valid_status(status: str) -> bool:
    return status.lower() in ["sunday", "monday", "tuesday", "wednesday", "thursday"]
