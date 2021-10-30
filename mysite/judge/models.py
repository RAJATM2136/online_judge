from django.db import models


class Problems(models.Model):
    Statement = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    Difficulty = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Solutions(models.Model):
    Problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=200)
    Submitted_At = models.DateTimeField('date published')

    def __str__(self):
        return self.Verdict

    def was_published_recently(self):
        return self.Submitted_At >= timezone.now() - datetime.timedelta(days=1)


class TestCases(models.Model):
    Input = models.CharField(max_length=200)
    Output = models.CharField(max_length=200)
    Problem = models.ForeignKey(Problems, on_delete=models.CASCADE)

    def __str__(self):
        return self.Input
