from django.db import models

# Create your models here.


class Status(models.Model):
    display = models.CharField(max_length=50)
    text_identifier = models.CharField(max_length=2)
    next_status = models.CharField(max_length=2)
    prev_status = models.CharField(max_length=2)

class UserStory(models.Model):
    # Update form fields required for story creation as fields are added
    FORM_FIELDS = [
        {
            "field": 'short_name',
            "display": "User story name"
        },
        {
            "field": 'full_name',
            "display": "User story long form name"
        },
        {
            "field": 'parent_feature',
            "display": "Parent Feature"
        },
        {
            "field": 'git_branch',
            "display": "Git Branch Name"
        },
    ]

    short_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    parent_feature = models.CharField(max_length=50)
    git_branch = models.CharField(max_length=50)

    def is_completed(self):
        return self.status in {self.DONE}


class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    comment_user = models.CharField(max_length=100)
    comment_date_time = models.DateField(auto_now_add=True)
    user_story = models.ForeignKey(UserStory, on_delete=models.PROTECT)
