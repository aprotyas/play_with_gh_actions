from setuptools import setup

package_name = 'example_package'

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
    maintainer='Abrar Rahman Protyasha',
    maintainer_email='aprotyas@u.rochester.edu',
    keywords=['ROS', 'Python'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Example package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = example_package.publisher:main',
        ],
    },
)
