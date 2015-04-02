import os
from django.core.management.base import BaseCommand
from django.conf import settings


# setup cronjobs
# You can add these by adding ./manage.py crontab to contrab -e
# or overwrite crontab with ./manage.py crontab | crontab -
# crontab command asumes your virtualenv has the same name as your project
# end is located in the same directory as your project folder
class Command(BaseCommand):
    def handle(self, *args, **options):
        venv_path = os.path.join(
            settings.BASE_DIR, "../", "venv",
            settings.PROJECT_NAME, "bin", "python"
        )
        task_path = task = os.path.join(
            settings.BASE_DIR, "manage.py"
        )

        self.stdout.write("# http://www.unix.com/man-page/linux/5/crontab/")

        #add regular wallet updates
        cron = "@weekly"
        task = "update_wallets"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))

        # update alliances
        cron = "@daily"
        task = "update_alliances"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))

        #update sovereingthy
        cron = "0 */2 * * *"
        task = "update_sovereignty"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))
