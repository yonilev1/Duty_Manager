import utils

def add_soldier(all_soldiers:list, soldier_id: int, name: str) -> None:
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(name):
        raise ValueError(f"name {name} is not valid, should be str 1 - 20 chars")
    elif utils.find_soldier_by_id(all_soldiers, soldier_id)[0]:
        raise ValueError(f"soldier_id {soldier_id} is already in use, soldier_id should be unique")
    else:
        all_soldiers.append({"soldier_id":soldier_id, "name":name, "duties":[]})


def remove_soldier(all_soldiers:list, soldier_id: int) -> None:
    if not utils.is_valid_soldier_id(soldier_id):
        raise ValueError(f"soldier_id {soldier_id} is not valid, should be number with 1 - 10 digits")
    soldier, index = utils.find_soldier_by_id(all_soldiers, soldier_id)
    if not soldier:
        raise ValueError(f"soldier_id {soldier_id} was not found in the database")
    else:
        del all_soldiers[index]


def get_all_soldiers(all_soldiers:list) -> list:
    for soldier in all_soldiers:
        print(f"=== soldier_id: {soldier["soldier_id"]}, name: {soldier["name"]} ===")
  