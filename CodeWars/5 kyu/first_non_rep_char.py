def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i in range(0, len(string_lower)):
        if string_lower.count(string_lower[i]) == 1:
            return string[i]
    return ''
