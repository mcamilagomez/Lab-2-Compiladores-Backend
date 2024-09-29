import re
def validate_regex(regex):
    try:
        re.compile(regex)
        return True  #Is a valid regex
    except re.error:
        return False  #Has a mistake