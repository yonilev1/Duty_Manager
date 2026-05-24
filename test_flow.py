"""
End-to-end flow tests for the duty manager project.
Tests all happy paths and edge cases directly on the logic layer.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import soldier_manager
import duty_manager
import utils

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

results = []

def check(test_name, condition, detail=""):
    status = PASS if condition else FAIL
    print(f"  [{status}] {test_name}" + (f" | {detail}" if detail else ""))
    results.append((test_name, condition))

def expect_exception(test_name, exc_type, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
        print(f"  [{FAIL}] {test_name} | expected {exc_type.__name__}, got no exception")
        results.append((test_name, False))
    except exc_type as e:
        print(f"  [{PASS}] {test_name} | raised {exc_type.__name__}: {e}")
        results.append((test_name, True))
    except Exception as e:
        print(f"  [{FAIL}] {test_name} | expected {exc_type.__name__}, got {type(e).__name__}: {e}")
        results.append((test_name, False))

def fresh_list():
    return []

# ──────────────────────────────────────────────
print("\n=== SOLDIER MANAGER: add_soldier ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 1001, "Alice")
check("add valid soldier", len(soldiers) == 1)
check("soldier has correct id", soldiers[0]["soldier_id"] == 1001)
check("soldier has correct name", soldiers[0]["name"] == "Alice")
check("soldier starts with empty duties", soldiers[0]["duties"] == [])

soldier_manager.add_soldier(soldiers, 2002, "Bob")
check("add second soldier", len(soldiers) == 2)

# duplicate id
expect_exception("duplicate soldier_id raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, 1001, "Alice2")

# invalid id – zero
expect_exception("id=0 raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, 0, "Zero")

# invalid id – negative
expect_exception("negative id raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, -5, "Neg")

# invalid id – too large (>= MAX_ID = 1_000_000_000)
expect_exception("id too large raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, 1_000_000_000, "Huge")

# invalid name – empty
expect_exception("empty name raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, 3003, "")

# invalid name – too long (21 chars)
expect_exception("name too long raises ValueError", ValueError,
                 soldier_manager.add_soldier, soldiers, 3003, "A" * 21)

# valid boundary: name exactly 20 chars
soldier_manager.add_soldier(soldiers, 3003, "B" * 20)
check("name exactly 20 chars accepted", len(soldiers) == 3)

# valid boundary: id = 1
soldier_manager.add_soldier(soldiers, 1, "MinId")
check("id=1 (min) accepted", any(s["soldier_id"] == 1 for s in soldiers))

# valid boundary: id = MAX_ID - 1
soldier_manager.add_soldier(soldiers, 999_999_999, "MaxId")
check("id=999999999 (max-1) accepted", any(s["soldier_id"] == 999_999_999 for s in soldiers))

# ──────────────────────────────────────────────
print("\n=== SOLDIER MANAGER: remove_soldier ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 100, "ToRemove")
soldier_manager.remove_soldier(soldiers, 100)
check("remove existing soldier", len(soldiers) == 0)

expect_exception("remove non-existent soldier raises ValueError", ValueError,
                 soldier_manager.remove_soldier, soldiers, 100)

expect_exception("remove with invalid id raises ValueError", ValueError,
                 soldier_manager.remove_soldier, soldiers, 0)

# ──────────────────────────────────────────────
print("\n=== SOLDIER MANAGER: get_all_soldiers ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 111, "Charlie")
soldier_manager.add_soldier(soldiers, 222, "Dana")
# just check it doesn't raise
try:
    soldier_manager.get_all_soldiers(soldiers)
    check("get_all_soldiers runs without error (2 soldiers)", True)
except Exception as e:
    check("get_all_soldiers runs without error", False, str(e))

soldiers_empty = fresh_list()
try:
    soldier_manager.get_all_soldiers(soldiers_empty)
    check("get_all_soldiers on empty list doesn't raise", True)
except Exception as e:
    check("get_all_soldiers on empty list doesn't raise", False, str(e))

# ──────────────────────────────────────────────
print("\n=== DUTY MANAGER: add_duty_to_soldier ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 500, "Eve")

duty_manager.add_duty_to_soldier(soldiers, 500, "Guard", "Monday")
check("add valid duty", len(soldiers[0]["duties"]) == 1)
check("duty has correct name", soldiers[0]["duties"][0]["name"] == "Guard")
check("duty default status is pending", soldiers[0]["duties"][0]["status"] == "pending")
check("duty has correct day", soldiers[0]["duties"][0]["day"] == "Monday")

# duplicate duty
expect_exception("duplicate duty name raises ValueError", ValueError,
                 duty_manager.add_duty_to_soldier, soldiers, 500, "Guard", "Tuesday")

# invalid day
expect_exception("invalid day raises ValueError", ValueError,
                 duty_manager.add_duty_to_soldier, soldiers, 500, "Patrol", "Friday")

# soldier not found
expect_exception("duty to non-existent soldier raises ValueError", ValueError,
                 duty_manager.add_duty_to_soldier, soldiers, 999, "Patrol", "Monday")

# invalid soldier id
expect_exception("duty with invalid soldier_id raises ValueError", ValueError,
                 duty_manager.add_duty_to_soldier, soldiers, -1, "Patrol", "Monday")

# invalid duty name (empty)
expect_exception("empty duty name raises ValueError", ValueError,
                 duty_manager.add_duty_to_soldier, soldiers, 500, "", "Monday")

# valid: all days
for day in ["sunday", "monday", "tuesday", "wednesday", "thursday"]:
    soldiers2 = fresh_list()
    soldier_manager.add_soldier(soldiers2, 600, "Frank")
    duty_manager.add_duty_to_soldier(soldiers2, 600, "Task", day)
    check(f"day '{day}' accepted", soldiers2[0]["duties"][0]["day"] == day)

# case-insensitive day check (utils level)
check("is_valid_day case insensitive Sunday", utils.is_valid_day("Sunday"))
check("is_valid_day case insensitive MONDAY", utils.is_valid_day("MONDAY"))

# ──────────────────────────────────────────────
print("\n=== DUTY MANAGER: update_duty_status ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 700, "Grace")
duty_manager.add_duty_to_soldier(soldiers, 700, "Cleaning", "Wednesday")

duty_manager.update_duty_status(soldiers, 700, "Cleaning", "completed")
check("status updated to completed", soldiers[0]["duties"][0]["status"] == "completed")

duty_manager.update_duty_status(soldiers, 700, "Cleaning", "missed")
check("status updated to missed", soldiers[0]["duties"][0]["status"] == "missed")

duty_manager.update_duty_status(soldiers, 700, "Cleaning", "pending")
check("status updated back to pending", soldiers[0]["duties"][0]["status"] == "pending")

# invalid status
expect_exception("invalid status raises ValueError", ValueError,
                 duty_manager.update_duty_status, soldiers, 700, "Cleaning", "done")

# soldier not found
expect_exception("update status for non-existent soldier raises ValueError", ValueError,
                 duty_manager.update_duty_status, soldiers, 999, "Cleaning", "completed")

# duty not found on soldier
expect_exception("update status for non-existent duty raises ValueError", ValueError,
                 duty_manager.update_duty_status, soldiers, 700, "NoSuchDuty", "completed")

# invalid id
expect_exception("update status with invalid id raises ValueError", ValueError,
                 duty_manager.update_duty_status, soldiers, 0, "Cleaning", "completed")

# case-insensitive status
check("is_valid_status 'Pending' case-insensitive", utils.is_valid_status("Pending"))
check("is_valid_status 'COMPLETED'", utils.is_valid_status("COMPLETED"))
check("is_valid_status 'Missed'", utils.is_valid_status("Missed"))

# ──────────────────────────────────────────────
print("\n=== DUTY MANAGER: get_soldier_duties ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 800, "Hank")
duty_manager.add_duty_to_soldier(soldiers, 800, "Patrol", "Thursday")
duty_manager.add_duty_to_soldier(soldiers, 800, "Logistics", "Sunday")

duties = duty_manager.get_soldier_duties(soldiers, 800)
check("get_soldier_duties returns 2 duties", len(duties) == 2)
check("first duty name correct", duties[0]["name"] == "Patrol")
check("second duty name correct", duties[1]["name"] == "Logistics")

expect_exception("get_soldier_duties for non-existent soldier raises KeyError", KeyError,
                 duty_manager.get_soldier_duties, soldiers, 9999)

# ──────────────────────────────────────────────
print("\n=== FULL END-TO-END SCENARIO ===")

soldiers = fresh_list()
soldier_manager.add_soldier(soldiers, 1, "Alpha")
soldier_manager.add_soldier(soldiers, 2, "Bravo")
duty_manager.add_duty_to_soldier(soldiers, 1, "Watch", "Monday")
duty_manager.add_duty_to_soldier(soldiers, 1, "Cook", "Tuesday")
duty_manager.add_duty_to_soldier(soldiers, 2, "Drive", "Wednesday")
duty_manager.update_duty_status(soldiers, 1, "Watch", "completed")
duty_manager.update_duty_status(soldiers, 2, "Drive", "missed")
soldier_manager.remove_soldier(soldiers, 2)

check("e2e: one soldier left after removal", len(soldiers) == 1)
check("e2e: remaining soldier is Alpha", soldiers[0]["name"] == "Alpha")
check("e2e: Alpha has 2 duties", len(soldiers[0]["duties"]) == 2)
check("e2e: Watch is completed", soldiers[0]["duties"][0]["status"] == "completed")
check("e2e: Cook is still pending", soldiers[0]["duties"][1]["status"] == "pending")
expect_exception("e2e: Bravo's duties gone (KeyError)", KeyError,
                 duty_manager.get_soldier_duties, soldiers, 2)

# ──────────────────────────────────────────────
print("\n=== SUMMARY ===")
total = len(results)
passed = sum(1 for _, ok in results if ok)
failed = total - passed
print(f"  Total: {total}  |  Passed: {passed}  |  Failed: {failed}")
if failed:
    print("\nFailed tests:")
    for name, ok in results:
        if not ok:
            print(f"  - {name}")
    sys.exit(1)
else:
    print("\nAll tests passed!")
