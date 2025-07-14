from setuptools import find_packages, setup

package_name = 'uav_hardware'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pedro',
    maintainer_email='pedro.l.s.lobo@gmail.com',
    description='Pacote ROS 2 para controle de buzzer e LED com GPIOZero',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'buzzer_and_led_node = uav_hardware.buzzer_and_led_node:main',
        ],
    },
)
