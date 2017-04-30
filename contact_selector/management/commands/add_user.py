from django.core.management.base import BaseCommand, CommandError

from contact_selector.models import Contact
from contact_selector.phonenumber import validate_phonenumber

class Command(BaseCommand):
    help = 'Adds a contact to the contacts database'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('company')
        parser.add_argument('email')
        parser.add_argument('phone')

    def handle(self, *args, **options):
        try:
            phone = validate_phonenumber(options['phone'])
        except Exception, msg:
            raise CommandError(msg)

        contact = Contact(
            name=options['name'],
            company=options['company'],
            email=options['email'],
            phone=phone)
        contact.save()
        self.stdout.write(self.style.SUCCESS('Successfully created contact {}'.format(contact.name)))