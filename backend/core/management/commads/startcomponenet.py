## this is the file for adding the command in the django project for adding components
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Create a new component in the django project'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the app to create')
        parser.add_argument('component_name', type=str, help='Name of the component to create')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        component_name = kwargs['component_name']
        # check the existence of the app
        if not os.path.exists(f'./{app_name}'):
            self.stdout.write(self.style.ERROR(f'App {app_name} does not exist'))
            return 1
        # check if the component is already exsits
        if os.path.exists(f'./{app_name}/{component_name}'):
            self.stdout.write(self.style.ERROR(f'Component {component_name} already exists'))
            return 1

        # create the component
        os.makedirs(f'./{app_name}/{component_name}')
        with open(f'./{app_name}/{component_name}/__init__.py', 'w') as f:
            f.write('')
        with open(f'./{app_name}/{component_name}/tests.py', 'w') as f:
            f.write('from rest_framework.test import APITestCase\nfrom rest_framework import status\nfrom django.urls import reverse\n\n## Please add the test in the test class for the component\n\nclass Tests(APITestCase):\n\tpass')
        with open(f'./{app_name}/{component_name}/urls.py', 'w') as f:
            f.write(f'from django.urls import path\n\n#add the urls here for the component\n\napp_name = "{component_name}"\n\nurlpatterns = []')
        with open(f'./{app_name}/{component_name}/views.py', 'w') as f:
            f.write('from rest_framework.views import APIView\nfrom rest_framework.response import Response\nfrom rest_framework import status\n\n#add the views here for the component\n\n')
        os.mkdir(f'./{app_name}/{component_name}/utils')
        with open(f'./{app_name}/{component_name}/utils/__init__.py', 'w') as f:
            f.write('')
        with open(f'./{app_name}/{component_name}/models.py','w') as f:
            f.write('from django.db import models\n\n#please add the models here')
        if not os.path.exists(f'./{app_name}/urls.py'):
            with open(f'./{app_name}/urls.py', 'w') as f:
                f.write('from django.urls import path,include\n\nurlpatterns = []\n\n#please the urls here\n\n')
        with open(f'./{app_name}/urls.py', 'a') as f:
            f.write(f'\n##{component_name} urls\n\nurlpatterns += [\n\tpath("{component_name}", include(("{app_name}.{component_name}.urls", "{component_name}"), namespace = "{component_name}"))\n]')
        if not os.path.exists(f'./{app_name}/tests.py'):
            with open(f'./{app_name}/tests.py', 'w') as f:
                f.write('from django.test import TestCase\n\n## Please add the test in the test class for the component\n\n')
        with open(f'./{app_name}/tests.py', 'a') as f:
            f.write(f'\n##{component_name} tests\n\nfrom .{component_name}.tests import *')
        if not os.path.exists(f'./{app_name}/models.py'):
            with open(f'./{app_name}/models.py', 'w') as f:
                f.write('from django.db import models\n\n#please add the models here\n\n')
        with open(f'./{app_name}/models.py', 'a') as f:
            f.write(f'\n##{component_name} models\n\nfrom .{component_name}.models import *\n\n')
        self.stdout.write(self.style.SUCCESS(f'Component {component_name} created successfully'))
