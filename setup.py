import sys

from setuptools import setup, find_packages

def is_running_tests():
    return {'pytest', 'test', 'ptr'}.intersection(sys.argv)

setup_requires = []

if is_running_tests:
    setup_requires.append('pytest-runner')

DESCRIPTION = (
    'Python library for interacting with the Patreon API. '
    'OAuth-centric for now.'
)

setup(
    name='patreon',
    version='0.5.2',
    description=DESCRIPTION,
    url='http://github.com/Patreon/patreon-python',
    author='Patreon',
    author_email='platform@patreon.com',
    license='Apache 2.0',
    packages=find_packages(
        exclude=['examples', 'examples.*', 'test', 'test.*']
    ),
    setup_requires=setup_requires,
    install_requires=[
        'requests',
        'six>=1.10.0',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'mock',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
