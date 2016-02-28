# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='django_brfied',
    packages=['django_brfied',
              'python_brfied', ],
    package_data={
        'django_brfied.static.js': ['*'],
    },
    version='0.1.4',
    description='Django Application specific brazilian fields types',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/django_brfied', 
    download_url='https://github.com/kelsoncm/django_brfied/releases/tag/0.1.4',
    keywords=['django', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)