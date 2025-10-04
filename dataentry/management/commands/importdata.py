from venv import create
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import DataError
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
        
        #compare csv header with model's field names
        #get all the field names of the model
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames

            #compare csv header with model's field names
            if csv_header != model_fields:
                raise DataError(f"CSV file doesn't match with the {model_name} table fields")
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))