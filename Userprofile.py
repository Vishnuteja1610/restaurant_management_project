from django.contrib.auth.models import User
user = User.objects.create_user(username="vishnu",email="vishnu@example.com",password="test1432")

user.profile.phone_number = "9876543210"
user.profile.save()

print(user.profile.phone_number)