from setuptools import setup

package_name = 'cmd_vel_odrive_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sebastian',
    maintainer_email='s.benkel@fw-robotics.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
entry_points={
        'console_scripts': [
                'cmd_vel_odrive_node = cmd_vel_odrive_node.cmd_vel_odrive_node:main',
        ],
},)
