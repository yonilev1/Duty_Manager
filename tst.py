
# Q1

def turn_tuple(tpl):
    """מקבלת טאפל הופכת אותו ומחזירה טאפל חדש"""
    tmp_lst = []
    for i in range(len(tpl)):
        tmp_lst.insert(0, tpl[i])
    return tuple(tmp_lst)
		
# ========================================
# Q2
def second_max(lst):
    """מקבל רשימה ומחזירה מספר שלם השני הכי גדול אם קיים אחרת None"""
    if len(lst) in [0,1]: return None
    max_el = max(lst)
    second_m = None
    tmp_lst = []
    for el in lst:
        if el != max_el:
            tmp_lst.append(el)
    if len(tmp_lst) == 0: return None
    return max(tmp_lst)

# ========================================
# Q3
def rotate(lst, k):
    """נקבל רשימה ומפר שלם ונזיז את ערכי השרימה K פעמים שמאלה"""
    actual_rotate = k % len(lst)
    lst = lst[::-1]
    new_lst1 = lst[:actual_rotate:-1]
    new_lst2 = lst[actual_rotate::-1]
    lst = new_lst2 + new_lst1
    return lst

# ========================================
# Q4
def tuple_count(tpl):
    """מקבל טאפל ומחזיר טאפל של טאפלים"""
    large_tpl = []
    count = {}
    for item in tpl:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
    for key,val in count.items():
        large_tpl.append((key, val))
    return tuple(large_tpl)

# ========================================
# Q5
def over_threshhold(dict, threshold):
    """מקבל מילון ומחזיר מילון עם כל הערכים מעל הסף"""
    over = {}
    for key,val in dict.itmes():
            if val > threshold:
                over[key] = val
    return over


# ========================================
# Q6
def only_in_one(lst1, lst2):
    """מקבל 2 מחרוזות ומחזיר מחרוזת אחת הבנוי משניהם מהפרש סימטרי"""
    new_lst = []
    for el in lst1:
        if el not in lst2 and lst2 not in new_lst:
            new_lst.append(el)
    for el in lst2:
        if el not in lst1 and lst2 not in new_lst:
            new_lst.append(el)
    new_lst.sort()
    return new_lst


print(only_in_one([1,2,3], [1,4,5]))


# ========================================
# Q7
def set_age(age):
    """מקבל מספר שלם ומחזיר מספר שלם אם ואלידי אחרת שגיאה"""
    if age < 0 or age > 150:
        raise ValueError("age not valid")
    return age


# ========================================
# Q8
def swap_dict(dict):
    """מקבל מילון ומחזיר מילון בהיפוך ערכים ומפתחות"""
    new_dict = {}
    for key, val in dict.itmes():
        new_dict[val] = key
    return new_dict

# ========================================
# Q9
def both_dicts(dict1, dict2):
    """מקבל שני מילונים ומחזיר מילון המורכב מאיברי שניהם, אם יש ערך שבשניהם הערך מהמילון השני מנצח"""
    new_dict = {}
    second_dicts_keys = dict2.keys() #אני לא בטוח שזה הסינטקס ברח לי מהראש אבל התכוונתי לפונקציה שמחזירה את המפתחות של המילון
    for key, val in dict1.items():
        if key in second_dicts_keys:
            new_dict[key] = dict2[key]
        else:
            new_dict[key] = dict1[key]
    return new_dict


# ========================================
# Q10
def map_first_letter(lst):
    """נקבל רשימה ונמפה כל מילה לאות שבו היא מתחילה במילון ונחזיר את המילון הנל"""
    new_dict = {}
    for word in lst:
        if word[0] in new_dict.keys():#אני לא בטוח שזה הסינטקס ברח לי מהראש אבל התכוונתי לפונקציה שמחזירה את המפתחות של המילון
            new_dict[word[0]].append(word)
        else:
            new_dict[word[0]] = [word]
    return new_dict
