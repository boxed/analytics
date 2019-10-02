from django.db import models


class Referrers(models.Model):
    page_url = models.URLField(db_index=True)
    referrer = models.URLField()
    count = models.BigIntegerField()

    class Meta:
        unique_together = ('page_url', 'referrer')


class PageCounts(models.Model):
    page_url = models.URLField(db_index=True, unique=True)
    count = models.BigIntegerField(default=0)


class UserAgents(models.Model):
    user_agent = models.CharField(max_length=200, db_index=True, unique=True)
    count = models.BigIntegerField(default=0)


class Claps(models.Model):
    page_url = models.URLField(db_index=True, unique=True)
    count = models.BigIntegerField(default=0)
