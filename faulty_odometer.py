def correct_number(numb):
    count = 0
    corrected_number = 0
    while True:
        rem = numb%10
        numb = numb - rem
        numb = numb/10
        if rem > 5:
            rem -= 1
        elif rem == 4:
            raise ValueError
        corrected_number = corrected_number + ((9**count)*rem)
        count += 1
        if not numb:
            break
        
    return corrected_number