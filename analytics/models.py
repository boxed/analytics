from django.db import models


class Referrers(models.Model):
    page_url = models.URLField(db_index=True)
    referrer = models.URLField()


class PageCounts(models.Model):
    page_url = models.URLField(db_index=True)
    count = models.BigIntegerField(default=0)


class UserAgents(models.Model):
    user_agent = models.CharField(max_length=200, db_index=True)
    count = models.BigIntegerField(default=0)


class Claps(models.Model):
    page_url = models.URLField()
    count = models.BigIntegerField(default=0)
