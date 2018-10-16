def is_int(n):
    try:
        n = int(n)
        return True

    except:
        return False

def is_year(n):
    return len(n)==4 and is_int(n)
       
