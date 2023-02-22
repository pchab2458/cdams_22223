
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
