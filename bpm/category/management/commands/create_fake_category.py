import traceback
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from faker import Faker
from bpm.category.models import Category, SubCategory, SubSubCategory
import tqdm

faker = Faker()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--num-categories', type=int, default=10, help='Number of categories to create')

    def handle(self, *args, **options):
        num_categories = options['num_categories']
        
        try:
            for _ in tqdm.tqdm(range(num_categories)):
                category = Category.objects.create(
                    name=faker.word(),
                    description=faker.sentence()
                )
                self.stdout.write(self.style.SUCCESS(f'Category "{category.name}"'))

                for _ in tqdm.tqdm(range(5)):
                    sub_category = SubCategory.objects.create(
                        name=faker.word(),
                        description=faker.sentence(),
                        category=category
                    )
                    self.stdout.write(self.style.SUCCESS(f'SubCategory "{sub_category.name}"'))

                    for _ in tqdm.tqdm(range(5)):
                        sub_sub_category = SubSubCategory.objects.create(
                            name=faker.word(),
                            description=faker.sentence(),
                            subcategory=sub_category
                        )
                        self.stdout.write(self.style.SUCCESS(f'SubSubCategory "{sub_sub_category.name}"'))

        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error creating post: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
            self.stdout.write(self.style.ERROR(f'Traceback: {traceback.format_exc()}'))
