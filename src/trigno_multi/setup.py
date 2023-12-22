from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'trigno_multi'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
       (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cfl',
    maintainer_email='anway.bose@temple.edu',
    description='Publish trigno sensor data',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trigno = trigno_multi.trigno:main'
        ],
    },
)
