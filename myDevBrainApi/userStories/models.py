from django.db import models

# Create your models here.


class Status(models.Model):
    IDEATED = 'ID'
    PLANNED = 'P'
    INPROGRESS = 'IP'
    INTEST = 'IT'
    DONE = 'D'
    STATUS_CHOICES = [
        ('ID', 'Ideated'),
        ('P', 'Planned'),
        ('IP', 'In Progress'),
        ('IT', 'In Test'),
        ('D', 'Done'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=IDEATED,
    )

    def is_completed(self):
        return self.status in {self.DONE}


class UserStory(models.Model):
    short_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    parent_feature = models.CharField(max_length=50)
    git_branch = models.CharField(max_length=50)


class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    comment_user = models.CharField(max_length=100)
    comment_date_time = models.DateField(auto_now_add=True)
    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE)
