calls = 0

def count_calls ():
    global calls
    calls += 1

def is_contains (string, list_to_search):
    count_calls()
    for elem in list_to_search:
        if string.lower() in elem.lower():
            return True
    else:
        return False

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN))
print(is_contains('cyclic', ['recycling', 'cyclic'])) # No matches))

def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
print(string_info("Armageddon"))
print(string_info("capybara"))
print(calls)










