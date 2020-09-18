from django.core.management.base import BaseCommand, CommandError
import json
from square.client import Client

client = Client(
    access_token='EAAAEB45GwcUifjYSX7HFhLPbORToCnJrpMCh7jY82180zkrXr544yKJs8v50BXc',
    environment='sandbox',
)

inventory_api = client.inventory
catalog_api = client.catalog

class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for item in json.loads(catalog_api.list_catalog().text)['objects']:
            print(item)


