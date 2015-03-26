from datetime import datetime

from django.db import models
from django.utils.timezone import utc


class Sovereignty(models.Model):
    """ what solarsystems can change owners """

    solarsystemid = models.BigIntegerField(unique=True)
    solarsystemname = models.CharField(max_length=254, unique=True)

    def __unicode__(self):
        return self.solarsystemname


class SovereigntyHolder(models.Model):
    """ who holds the sovereignty of a system """

    now = datetime.now().replace(tzinfo=utc)
    sovereignty = models.ForeignKey("bulk.Sovereignty")
    last_refresh = models.DateTimeField(default=now)
    allianceid = models.BigIntegerField(null=True)
    corporationid = models.BigIntegerField(null=True)
    factionid = models.BigIntegerField(null=True)

    def __unicode__(self):
        return self.sovereignty.solarsystemname

