import datetime
from django.db import models
from django.utils import timezone


class PublishedQuestionsManager(models.Manager):
    def get_queryset(self):
        return Question.objects.annotate(choice_count=models.Count('choice')) \
            .filter(pub_date__lte=timezone.now(), choice_count__gt=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    objects = models.Manager()
    published = PublishedQuestionsManager()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
