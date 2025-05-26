from setuptools import find_packages, setup

package_name = 'move_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='darshit',
    maintainer_email='darshit@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = move_robot.my_first_node:main",
            "draw_circle = move_robot.draw_circle:main",
            "pose_subscriber = move_robot.pose_subscriber:main",
            "turtle_controller=move_robot.turtle_controller:main"
        ],
    },
)
