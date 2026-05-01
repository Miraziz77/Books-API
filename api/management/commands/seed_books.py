from django.core.management.base import BaseCommand
from api.models import Book, Author, Category, SubCategory
from api.parsing_json.parsing_json import parse_json


class Command(BaseCommand):
    help = "Seed database with books data"

    def handle(self, *args, **kwargs):

        if Book.objects.exists():
            self.stdout.write("DB already seeded, skipping...")
            return

        self.stdout.write("Seeding database...")

        parse_json()

        self.stdout.write(self.style.SUCCESS("Done!"))