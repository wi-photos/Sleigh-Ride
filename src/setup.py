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
            'gui_apps': {
                'SleighRide': 'main.py',
            },
            'log_filename': '$USER_APPDATA/SleighRide/output.log',
            'log_append': False,
            'plugins': [
                'pandagl',
                'p3tinydisplay',
                'p3openal_audio',
                
            ],
            'platforms': [
                'manylinux1_x86_64',
                'macosx_10_6_x86_64',
                'win_amd64',
                'win32',
                'manylinux1_i686',
                'macosx_10_6_i386',
            ],
            'use_optimized_wheels': True,
            'optimized_wheel_index': 'https://archive.panda3d.org/branches/deploy-ng',

            
        }
    }
)