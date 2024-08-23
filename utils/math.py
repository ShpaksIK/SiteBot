from datetime import datetime, timezone


def calculate_server_age(creation_date):
    current_date = datetime.utcnow().replace(tzinfo=timezone.utc)
    delta = current_date - creation_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return years, months, days