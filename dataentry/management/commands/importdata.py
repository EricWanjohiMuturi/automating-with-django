from venv import create
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

#proposed command to import data from a csv file through a file path


class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        #Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            #Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue #model not found in the app, continue searching in other apps
        
        if not model:
            raise CommandError(f"'{model_name}' model is not found in any installed apps.")
        

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))