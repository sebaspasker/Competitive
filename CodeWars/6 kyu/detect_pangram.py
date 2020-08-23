from string import ascii_lowercase

def is_pangram(s):
    s_lower = s.lower()
    for char in ascii_lowercase:
        if not char in s_lower:
            return False
    return True
