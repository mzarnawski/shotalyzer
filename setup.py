from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author='Mikolaj Zarnawski',
    author_email='mzarnawski@gmail.com',
    description='SnapshotAlyzer 3000 is a tool to manage EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)