table_size = 121
table_age = [None] * table_size

def add_name(name, age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
        return
    table_age[age] = name
    
def get_name_by_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
        return
    return table_age[age]

add_name("name1", 25)
add_name("name2", 30)
add_name("name3", 40)

print("name of who is 25 years: ", get_name_by_age(25))
print("name of who is 30 years: ", get_name_by_age(30))
print("name of who is 40 years: ", get_name_by_age(40))
print("name of who is 50 years: ", get_name_by_age(50))

