from .models import CustomUser
from .validators import HashPW

# This custom authentication allows users to sign in with their email instead of their username
class EmailBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            hashed_pw = HashPW(password)
            if hashed_pw[1].verify(hashed_pw[0], password):
                return user
            return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None