import time
from optparse import make_option

from django.db import transaction
from django.core.management.base import BaseCommand

from tasks.models import Task


# execute api tasks
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            "--timer",
            action="store",
            type="int",
            dest="timer",
            default=10,
            help="""Sleep Timer (in seconds) before checking for new tasks
            (default is 10 seconds)"""),
    )

    #handle is what actualy will be executed
    def handle(self, *args, **options):
        #get oldest task
        while True:
            with transaction.atomic():
                task = Task.objects.filter(
                    active=False
                ).order_by("date").first()

                if task:
                    task.active = True
                    task.save()

            if task:
                obj = task.get_child()
                obj.process()
                task.delete()
                #to make not sure to many api requests will be made from tasks
                time.sleep(1)
            else:
                self.stdout.write("sleep test")
                time.sleep(options['timer'])
