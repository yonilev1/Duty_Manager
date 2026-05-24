import utils

def add_soldier(all_soldiers:list, soldier_id: int, name: str) -> None:
    """
    add new soldier to list of soldiers

    Args:
        all_soldiers(list): list of all soldiers
        soldier_id(int): soldier uniqe id
        name(str): soldier name
    
    Returns:
        Nonw
   
    Raises:
        ValueError: if name or id not valid ot not uniqe
    """
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(name):
        raise ValueError(f"name {name} is not valid, should be str 1 - 20 chars")
    elif utils.find_soldier_by_id(all_soldiers, soldier_id)[0]:
        raise ValueError(f"soldier_id {soldier_id} is already in use, soldier_id should be unique")
    else:
        all_soldiers.append({"soldier_id":soldier_id, "name":name, "duties":[]})


def remove_soldier(all_soldiers:list, soldier_id: int) -> None:
    """
    remove soldier from list of soldiers
    Args:
        all_soldiers(list): list of all soldiers
        soldier_id(int): soldier uniqe id

    Returns:
        None

    Raises: 
        ValueError if id not valid ot not uniqe
    """
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    soldier, index = utils.find_soldier_by_id(all_soldiers, soldier_id)
    if not soldier:
        raise ValueError(f"soldier_id {soldier_id} was not found in the database")
    else:
        del all_soldiers[index]


def get_all_soldiers(all_soldiers:list) -> list:
    """
    get and print list of all soldiers

    Args:
        all_soldiers(list): list of all soldiers

    Returns: 
        None
    """
    for soldier in all_soldiers:
        print(f"=== soldier_id: {soldier["soldier_id"]}, name: {soldier["name"]} ===")
  