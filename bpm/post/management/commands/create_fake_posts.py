from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from faker import Faker
from tqdm import tqdm
from django.db import IntegrityError

from bpm.post.models import Post
from bpm.user.models import User
from bpm.tag.models import Tag
from bpm.comment.models import Comment
from bpm.category.models import SubSubCategory

faker = Faker()

class Command(BaseCommand):
    help = 'Create fake users, tags, and posts for testing purposes'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--num-posts',
            type=int,
            default=50,
            help='Number of posts to create (default is 50)'
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        num_posts = options['num_posts']
        
        try:
            for _ in tqdm(range(num_posts), desc="Creating posts"):
                # Create user
                user = User.objects.create(
                    first_name=faker.first_name(),
                    last_name=faker.last_name(),
                    username=faker.user_name(),
                    email=faker.email(),
                    status=faker.sentences(),
                    profession=faker.name(),
                    university=faker.sentence()
                )

                # Create tag
                tag = Tag.objects.create(
                    name=faker.word()  # Use a single word for tag instead of a name
                )

                #create random category
                cate_1 = SubSubCategory.objects.get(id=1)

                related_article = Post.objects.all()

                # Create post
                post = Post.objects.create(
                    title=faker.sentence(),
                    description=faker.text(),
                    
                    user=user,
                    meta_title=faker.sentence(),
                    meta_description=faker.sentences(),
                    slug=faker.word(),
                    category=cate_1
                )
                
                post.tag.add(tag)
                post.related_article.set(related_article)
                
                self.stdout.write(self.style.SUCCESS(f'Post "{post.title}" created by {user.username}.'))
                
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error creating post: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {e}'))
