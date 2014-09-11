
from django.core.management.base import BaseCommand, CommandError
from spoc import models

class Command(BaseCommand):
    help = "Create data if it doesn't exist."
  
    def handle(self, *args, **options):
        self.stdout.write('Start creating initial data.')
        self.insert_formula_types()

    def insert_formula_types(self):
        self.stdout.write('Start creating formula types.')
        for t in models.FormulaType.DEFAULT_TYPES:
            formula_type = models.FormulaType(code=t).save()
            if formula_type is None:
                self.stdout.write('Formula type "{}" EXISTS'.format(t))
            else:
                self.stdout.write('Created formula type {}.'.format(t))
                
