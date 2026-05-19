def main():
    """
    יצירת מערך לחיילים 
    יצירת מערך עזר למשימות
      וקבלת בחירה מהמשתמש
    """




def add_soldier(ma:int, name:str):
    """
    בדיקה עם קיים עי check_soldiers_ditails, אם לא קיים
    הוספת רשומת מילון של חייל לתוך רשימת החיילים הכללית
    המילון מכיר 3 ערכים - מספר אישי, שם, ורשימה ריקה למשימות
    """


def check_soldiers_ditails(ma:int,name: None |str)->bool:
    """
    בדיקה שהמספר אישי לא קיים כבר במערכת אחרת מחזיר - KeyError
    ושהמספר אישי מספר שלם חוקי של 7 ספרות אחרת מחזיר - ValueError
    ושהשם מחרוזת חוקית של עד 20 תווים אחרת מחזיר - ValueError
    """


def delete_soldier(ma:int):
    """
   check_soldiers_ditails עפ מספר חייל, בדיקה אם קיים. עי 
    אם כן נמחוק את הרשומה שלו
    """


def show_all_soldiers():
    """
    הדפסת רשימת כל שמות החיילים בזוג - חייל ומספר אישי.
    אם אין חיילים נחזיר שגיאת KeyError שאין חיילים
    """


def add_task_to_soldier(ma):
    """
    מקבלים מספר אישי
    ועוברים לפונקציה set_task()
    שם נגדיר משימה
    ואז נחזור לפה ונבדוק עי הפונקציה check_if_has_this_task האם יש את אותה משימה לחייל
    אם אין נוסיף לו, ואם יש נחזיר שגיאת KeyError
    """


def update_tasks_status(status):
    """
   check_if_status_valid נבדוק שהסטטוס ואלידי עי 
   אם כן נעדכן
    """


def check_if_status_valid(status):
    """
    נבדוק שהסטטוס נמצא ברשימת הואלידיים p,c,m
    אחרת נחזיר שגיאת ValueError
    """


def show_soldiers_tasks(ma):
    """
   search_existing_soldier נבדוק שהחייל קיים עי 
   אם קיים נדפיס את כל המשימות שלו
   אם אין לו משימות נדפיס שאין לו משימות
    """


def search_existing_soldier(ma):
    """
    מקבלים מספר אישי ובודקים עפ רשימת החיילים שהחייל קיים
    אם קיים נחזיר אותו כאובייקט
    אחרת נחזיר שגיאת KeyError
    """

def set_task():
    """
    נבקש מהמשתמש שם משימה, יום וסטטוס.
   check_if_day_is_valid נבדוק שהיום תקין עי
   check_if_status_valid ונבדוק שהסטטוס תקין עי
   אחרת ValueError
    """


def check_if_day_is_valid(day):
    """
           ValueError נבדוק שהיום תקין בין ראשון וחמישי כולל אחרת
    """