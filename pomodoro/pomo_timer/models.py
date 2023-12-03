from django.db import models


class timers(models.Model):
    name = models.CharField(max_length=10, default="DEF")
    pomodoro = models.IntegerField(default=25)
    long_break = models.IntegerField(default=15)
    short_break = models.IntegerField(default=5)

    def __str__(self):
        return self.name


class tasks(models.Model):
    task_desc = models.CharField(max_length=200)
    est_pomodoro = models.IntegerField()
    status = models.BooleanField(default=False)
    custom_id = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_task = tasks.objects.order_by('-custom_id').first()
            if last_task:
                self.custom_id = last_task.custom_id + 1
            else:
                self.custom_id = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.custom_id)
