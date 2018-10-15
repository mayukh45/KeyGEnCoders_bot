def is_int(n):
    try:
        n = int(n)
        return True

    except:
        return False

def is_year(n):
    if len(n)==4 and is_int(n):
        return True
    else:
        return False
