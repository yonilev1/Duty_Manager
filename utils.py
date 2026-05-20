def is_valid_name(name: str) -> bool:
    return 0 < len(name) <= 20 
    
print(is_valid_name("ge"))