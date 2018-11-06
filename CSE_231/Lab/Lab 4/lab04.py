def leap_year (a):
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        return True
    else:
        return False

def rotate (s, n):
    s = str(s)
    n = int(n)
    a = s[-n:] + s[:-n]
    return a

def digit_count (n):
    even = "2468"
    odd = "13579"
    even_count = 0
    odd_count = 0 
    zero_count = 0
    for ch in n:
        if ch == ".":
            break
        elif ch in even:
            even_count += 1
        elif ch in odd:
            odd_count += 1
        else:
            zero_count += 1
    return (even_count, odd_count, zero_count)

def float_check (s):
    dec_count = 0
    for ch in s:
        if ch == ".":
            dec_count += 1
        elif not ch.isdigit():
            return False       
    if dec_count <= 1:
        return True
    else:
        return False