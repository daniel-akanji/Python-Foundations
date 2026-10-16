def initials_badge(full_name):
    cleaned = full_name.strip()
    uses = cleaned.split()

    first_char = ""
    for use in uses:
        first_char += use[0]
        First = first_char.upper() 
    
    output = ".".join(First)

    return (f"{output}.")

print(initials_badge(" Ada Lovelace "))
print(initials_badge("Mary Jane Watson"))