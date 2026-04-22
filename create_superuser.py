from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="newadmin",
        email="admin@amalaoriki.com",
        password="baby55555555"
    )