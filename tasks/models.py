import decimal

from django.db import models
from django.db import IntegrityError

from apps.characters.models import CharacterApi, CharacterJournal
from apps.corporations.models import CorporationApi

import utils


class Task(models.Model):
    """
    Task parent. Task will be sometimes generated to run asynchroon
    A worker will run these task one by one when enough resources are free
    """

    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def get_child(self):
        try:
            obj = self.journal
            return obj
        except Journal.DoesNotExist:
            pass


class Journal(Task):
    """ create character/corporation transactions """

    character = models.BooleanField(default=True)
    #primarykey of character/corporationapi
    key = models.IntegerField()
    fromid = models.BigIntegerField(null=True)
    rowcount = models.SmallIntegerField(null=True)
    accountkey = models.SmallIntegerField(null=True)

    def __unicode__(self):
        return "Journal Task"

    def process(self):
        if self.character:
            try:
                obj = CharacterApi.objects.get(pk=self.key)
                self.character_transactions(obj)
            except CharacterApi.DoesNotExist:
                return
        else:
            try:
                obj = CorporationApi.objects.get(pk=self.key)

            except CorporationApi.DoesNotExist:
                return
        return

    #create aditional character transactions
    def character_transactions(self, obj):
        kwargs = {}
        if self.fromid:
            kwargs['fromid'] = self.fromid
        if self.rowcount:
            kwargs['rowcount'] = self.rowcount

        transactions = utils.connection.api_request(
            "WalletJournal", obj=obj, **kwargs
        ).transactions

        for t in transactions:
            try:
                taxreceiverid = int(t.taxReceiverID)
            except ValueError:
                taxreceiverid = None

            try:
                taxamount = decimal.Decimal(t.taxAmount)
            except decimal.InvalidOperation:
                taxamount = None

            try:
                CharacterJournal.objects.create(
                    characterapi=obj,
                    refid=t.refID,
                    date=utils.common.convert_timestamp(t.date),
                    balance=t.balance,
                    reftypeid=t.refTypeID,
                    ownername1=t.ownerName1,
                    ownerid1=t.ownerID1,
                    ownername2=t.ownerName2,
                    ownerid2=t.ownerID2,
                    argname1=t.argName1,
                    argid1=t.argID1,
                    amount=t.amount,
                    reason=t.reason,
                    taxreceiverid=taxreceiverid,
                    taxamount=taxamount,
                )
            except IntegrityError:
                #means the journalentry already exists
                pass
