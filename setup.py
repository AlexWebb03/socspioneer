import os

from glob import glob
from setuptools import setup

package_name = 'socspioneer'

setup(
    name=package_name,
    version='3.0.0',
    packages=['socspioneer'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'data'), glob('data/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alex Alderman Webb',
    maintainer_email='s2186366@ed.ac.uk',
    description='SOCSPioneer packages with simulation support.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'twist_publisher = socspioneer.twist_publisher:main',
            'marker_publisher = socspioneer.marker_publisher:main'
        ]
    }
)
