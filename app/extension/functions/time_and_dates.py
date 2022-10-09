from datetime import datetime


def date_and_hours_now():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    
def date_now():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime('%d/%m/%Y')