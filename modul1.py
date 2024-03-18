def text_length(text, max_num):
    if len(text) < max_num:
        length = len(text)
    else:
        length = max_num
    return length

def count_letter(length, text, letter):
    return text.count(letter, 0, length)

def max_letter(text, num, letter):
    if num == 1:
        t = text_length(text, 100)
        c = count_letter(t, text, letter)
    elif num == 2:
        t = text_length(text, 1000)
        c = count_letter(t, text, letter)
    elif num == 3:
        t = text_length(text, 10000)
        c = count_letter(t, text, letter)
    rate = c / t * 100
    return c, rate

def student_info(std_info):
    print(std_info)
    
student = {
    "name": "Mehmet Emin",
    "last name": "Yilmaz",
    "number": "211213036",
    "message": "Congratulations!"
    }
