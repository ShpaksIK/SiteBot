from datetime import datetime, timezone
import math


def calculate_server_age(creation_date):
    """ Подсчет возраста сервера """
    current_date = datetime.utcnow().replace(tzinfo=timezone.utc)
    delta = current_date - creation_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return years, months, days

def calculate_expression(expression):
    """ Математическй подсчет выражения """
    try:
        result = eval(expression, {"__builtins__": {}}, {"abs": abs, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "pow": math.pow})
        return result
    except Exception:
        pass