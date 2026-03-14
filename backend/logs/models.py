# Import Django models
from django.db import models

# Import the User model
from django.contrib.auth.models import User

# Import the Habit model
from habits.models import Habit


class HabitLog(models.Model):
    """
    Represents a daily log entry for a habit.
    This tracks whether a user completed a habit on a specific date.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="logs"
    )

    date = models.DateField()

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.habit.name} - {self.date}"