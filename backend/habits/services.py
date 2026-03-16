# Import HabitLog model
from logs.models import HabitLog

# Import datetime utilities
from datetime import date, timedelta


def calculate_current_streak(habit, user):
    """
    Calculate the current streak for a habit.
    The streak counts consecutive days the habit has been completed.
    """

    today = date.today()
    streak = 0

    while True:

        log_exists = HabitLog.objects.filter(
            habit=habit,
            user=user,
            date=today,
            completed=True
        ).exists()

        if log_exists:
            streak += 1
            today -= timedelta(days=1)
        else:
            break

    return streak


def calculate_longest_streak(habit, user):
    """
    Calculate the longest streak achieved for a habit.
    """

    logs = HabitLog.objects.filter(
        habit=habit,
        user=user,
        completed=True
    ).order_by('date')

    longest = 0
    current = 0
    previous_date = None

    for log in logs:

        if previous_date:
            if (log.date - previous_date).days == 1:
                current += 1
            else:
                current = 1
        else:
            current = 1

        longest = max(longest, current)
        previous_date = log.date

    return longest