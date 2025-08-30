from django.core.management.base import BaseCommand

# Proposed command = python manage.py greeting Name
#Proposed output = Hello {Name}, Good Evening!
class Command(BaseCommand):
    help = 'Hello, This is a greeting command'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies the username to greet')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f"Hello, {name}, Good Evening!"
        self.stdout.write(self.style.SUCCESS(greeting))
