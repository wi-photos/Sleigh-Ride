from setuptools import setup

setup(
    name="SleighRide",
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.jpg',
                '**/*.png',
                '**/*.egg',
                '**/*.ptf',
                '**/*.txt',
                '**/*.ogg',
                '**/*.jpeg',
            ],
            'platforms': [
                'macosx_10_9_x86_64',
                'manylinux2014_x86_64',
                'win_amd64',
            ],
            'gui_apps': {
                'SleighRide': 'main.py',
            },
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
        }
    }
)
