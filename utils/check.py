def check_status(discord, user_id):
    user_status = user_id.status
    if user_status == discord.Status.online:
        status = "🟢 В сети"
    elif user_status == discord.Status.offline:
        status = "⚫️ Не в сети"
    elif user_status == discord.Status.idle:
        status = "🟠 Не активен"
    elif user_status == discord.Status.dnd:
        status = "🔴 Не беспокоить"
    else:
        status = "Не определен"
    return status