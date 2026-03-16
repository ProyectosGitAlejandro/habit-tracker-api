from datetime import date, timedelta
from habits.models import Habit
from logs.models import HabitLog



def get_user_analytics(user):
    """
    Calculate general analytics metrics for a user.

    Returns key statistics about the user's habits,
    including total habits, habits completed today,
    completion rate and consistency score.
    """

    today = date.today()

    total_habits = Habit.objects.filter(user=user).count()

    completed_today = HabitLog.objects.filter(
        user=user,
        date=today,
        completed=True
    ).count()

    completion_rate = 0

    if total_habits > 0:
        completion_rate = int((completed_today / total_habits) * 100)

    # NEW → calculate consistency score
    consistency_score = get_consistency_score(user)

    return {
        "total_habits": total_habits,
        "completed_today": completed_today,
        "completion_rate": completion_rate,
        "consistency_score": consistency_score,  # NEW
    }

def get_user_heatmap(user):
    """
    Generate heatmap data for the last 365 days.

    Returns a list of daily activity counts similar to
    GitHub contribution heatmaps.
    """

    today = date.today()
    start_date = today - timedelta(days=365)

    logs = HabitLog.objects.filter(
        user=user,
        date__gte=start_date
    )

    logs_dict = {}

    for log in logs:
        day = log.date
        logs_dict[day] = logs_dict.get(day, 0) + 1

    heatmap = []

    for i in range(366):
        current_day = start_date + timedelta(days=i)

        heatmap.append({
            "date": current_day,
            "count": logs_dict.get(current_day, 0)
        })

    return heatmap

def get_consistency_score(user, days=30):
    """
    Calculate the user's habit consistency score.

    The score represents the percentage of days
    in which at least one habit was completed
    during the given time range.
    """

    today = date.today()
    start_date = today - timedelta(days=days)

    logs = HabitLog.objects.filter(
        user=user,
        completed=True,
        date__gte=start_date
    )

    active_days = {log.date for log in logs}

    consistency_score = int((len(active_days) / days) * 100)

    return consistency_score

def get_weekly_completion(user):
    """
    Calculate completed habits grouped by week.

    Returns a list of dictionaries containing
    the week number and completed habit count.
    """

    logs = HabitLog.objects.filter(
        user=user,
        completed=True
    )

    weekly_counts = {}

    for log in logs:
        week = log.date.isocalendar()[1]

        weekly_counts[week] = weekly_counts.get(week, 0) + 1

    results = [
        {"week": week, "completed": count}
        for week, count in sorted(weekly_counts.items())
    ]

    return results

def get_best_habits(user):
    """
    Calculate the completion rate for each habit of the user.

    This function aggregates habit logs and calculates
    how often each habit has been completed compared
    to the total number of logs.

    The result is ordered by completion rate (descending).
    """

    habits = Habit.objects.filter(user=user)

    results = []

    for habit in habits:
        total_logs = HabitLog.objects.filter(
            user=user,
            habit=habit
        ).count()

        completed_logs = HabitLog.objects.filter(
            user=user,
            habit=habit,
            completed=True
        ).count()

        completion_rate = 0

        if total_logs > 0:
            completion_rate = int((completed_logs / total_logs) * 100)

        results.append({
            "habit": habit.name,
            "completion_rate": completion_rate
        })

    results.sort(key=lambda x: x["completion_rate"], reverse=True)

    return results

def get_monthly_completion(user):
    """
    Calculate completed habits grouped by month.

    Returns a list containing month number and
    number of completed habit logs.
    """

    logs = HabitLog.objects.filter(
        user=user,
        completed=True
    )

    monthly_counts = {}

    for log in logs:
        month = log.date.month

        monthly_counts[month] = monthly_counts.get(month, 0) + 1

    results = [
        {"month": month, "completed": count}
        for month, count in sorted(monthly_counts.items())
    ]

    return results