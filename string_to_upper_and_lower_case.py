def alternate_case(s, remove_spaces = True, start_lower = True, alternate_interval = 1):
    result = ""
    if remove_spaces:
        s = s.replace(" ","")
    for i in range(len(s)):
        if i % alternate_interval == 0:
            if start_lower:
                result += s[i].lower()
            else:
                result += s[i].upper()
        else:
            if start_lower:
                result += s[i].upper()
            else:
                result += s[i].lower()
    return result


# Esempio di utilizzo
input_string = "ciao a tutti  21"
output_string = alternate_case(input_string, remove_spaces = True, start_lower = False, alternate_interval = 2)
print(output_string)