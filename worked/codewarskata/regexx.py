import re
def validate_pin(pin):
    x = re.findall(r"^\d+$",pin)
    try:
        if(len(x[0])==4 or len(x[0])==6):
            return print("true")
        return print("False")
    except:
        return print("False")

validate_pin("1234")
validate_pin("-123")
validate_pin("-1234")
validate_pin("090909")
validate_pin("1.234")
validate_pin("0a")
