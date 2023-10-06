from .models import CustomUser
from .validators import HashPW

# This custom authentication allows users to sign in with their email instead of their username
class EmailBackend:
    def authenticate(self, request, email=None, password=None):
        print(f"Attempting to authenticate with email: {email, password}")
        try:
            user = CustomUser.objects.get(email=email)
            hashed_pw = HashPW(password)

            print(f"User found: {user}")
            if hashed_pw[1].verify(hashed_pw[0], password):
                print("Password matches")
                return user
            print("Password does not match")
            return None
        except CustomUser.DoesNotExist:
            print("User does not exist" )
            return None
   
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            print("User does not exist")
            return None