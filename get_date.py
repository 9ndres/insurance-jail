from datetime import date

current_date = date.today()
slash_date = current_date.strftime("%d/%m/%Y")


def str_date():
    if current_date.month == '9':
        month = 'setiembre'
        return
