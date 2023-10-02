from .models import Register

def validation(username, email):
    
    message_list = []
    if Register.objects.filter(username=username).exists():
        message_list.append('Username already exists!')
    if Register.objects.filter(email=email).exists():
        message_list.append('Email already used for another account!')
    if message_list == []:
        return None
    return message_list

    