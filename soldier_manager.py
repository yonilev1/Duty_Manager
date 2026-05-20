import utils, data

def add_soldier(ma: int, name: str) -> None:
    if not utils.is_valid_ma(ma):
        raise ValueError(f"ma {ma} is not valid, should be number with 1 - 10 digits")
    elif not utils.is_valid_name(name):
        raise ValueError(f"name {name} is not valid, should be str 1 - 20 chars")
    elif utils.find_soldier_by_id(ma)[0]:
        raise ValueError(f"ma {ma} is allready in use, ma should be unique")
    else:
        data.soldier_list.append({"ma":ma, "name":name, "duties":[]})


def remove_soldier(ma: int) -> None:
    if not utils.is_valid_ma(ma):
        raise ValueError(f"ma {ma} is not valid, should be number with 1 - 10 digits")
    soldier, index = utils.find_soldier_by_id(ma)
    if not soldier:
        raise ValueError(f"ma {ma} was not found in the database")
    else:
        data.soldier_list.remove(index)


def get_all_soldiers() -> list:
    for soldier in data.soldier_list:
        print(f"=== ma: {soldier["ma"]}, name: {soldier["name"]} ===")

       







