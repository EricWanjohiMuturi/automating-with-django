from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints Hello World'

    def handle(self, *args, **kwargs):
        #we write the logic we want to perform here
        self.stdout.write('Hello World')