from setuptools import setup, find_packages

version = '1.4.2'

setup(
    name="django-nose-qunit",
    version=version,
    author="Jeremy Bowman",
    author_email="jbowman@safaribooksonline.com",
    description="Integrate QUnit JavaScript tests into a Django test suite via nose",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={
        'django_nose_qunit': [
            'run-qunit.js',
            'static/*.css',
            'static/*.js',
            'static/django_nose_qunit/test/*.js',
            'templates/django_nose_qunit/*.html',
            'templates/django_nose_qunit/fixtures/*.html',
        ],
    },
    zip_safe=False,
    install_requires=[
        'Django>=1.4',
        'django-nose',
        'requests',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'django-qunit = django_nose_qunit.nose_plugin:QUnitPlugin',
            'django-qunit-index = django_nose_qunit.nose_plugin:QUnitIndexPlugin'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Testing',
    ],
)
