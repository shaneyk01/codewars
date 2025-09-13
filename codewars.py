
def even_or_odd(number):
    pass
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    

def number_to_string(number):
   return str(number)


def get_count(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count  