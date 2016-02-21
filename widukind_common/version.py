VERSION = (0, 2, 6)

def version_str():
    if len(VERSION) == 3: 
        return "%s.%s.%s" % VERSION
    elif len(VERSION) == 4: 
        return "%s.%s.%s-%s" % VERSION
    else:
        raise IndexError("Incorrect format for the VERSION tuple")
