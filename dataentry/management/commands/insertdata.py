from django.core.management.base import BaseCommand
from dataentry.models import Student

#I want to add data to the database using a custom management command

class Command(BaseCommand):
    help = 'Insert data into the database'

    def handle(self, *args, **kwargs):
        #multiple dataset
        dataset = [
            {'roll_no':1006, 'name':"Cristiano Ronaldo", 'age':36},
            {'roll_no':1005, 'name':"Leonel Messi", 'age':35},
            {'roll_no':1004, 'name':"Neymar Junior", 'age':34},
            {'roll_no':1004, 'name':"Neymar Junior", 'age':34},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
           
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))