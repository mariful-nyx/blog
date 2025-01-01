from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from bpm.post.models import Post
from bpm.user.models import User
from bpm.comment.models import Comment
from random import randint
from faker import Faker
from django.db import IntegrityError
from tqdm import tqdm


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--num-comments', type=int, default=10
        )
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        help = 'Create fake comment for development purpose'
        num_comments = options['num_comments']
        fake = Faker()
        
        posts = Post.objects.all()
        users = User.objects.all()

        try:
            for _ in tqdm(range(num_comments)):
                comment = Comment.objects.create(
                    user = users[randint(0, 49)],
                    post = posts[randint(0, 49)],
                    comment = fake.text()
                )
                comment.save()
                self.stdout.write(self.style.SUCCESS('Comment is created.'))


        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error creating post: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {e}'))

