from setuptools import setup

package_name = 'obstacle_avoidance'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A ROS 2 package for obstacle avoidance.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_node = obstacle_avoidance.lidar.lidar_node:main',
            'camera_publisher_node = obstacle_avoidance.camera.camera_publisher_node:main',
            'sensor_fusion_node = obstacle_avoidance.navigation.sensor_fusion_node:main',
        ],
    },
)

