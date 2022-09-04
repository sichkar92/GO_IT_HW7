from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='this script sorted files in folder by categories and delete empty folders',
    author='Sichkar Dmytro',
    author_email='sichkar.dima@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_script': ['clean_folder=clean_folder.clean:main']}
    )
