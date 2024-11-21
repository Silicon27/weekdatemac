from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstall(install):
    def run(self):
        # Call the original install process
        install.run(self)
        # Run the install.sh script
        subprocess.call(["/bin/bash", "install.sh"])

setup(
    name='weekdatemac',
    version='1.0.0',
    packages=['weekdatemac'],
    cmdclass={'install': CustomInstall},
    install_requires=[],  # List of Python dependencies (if any)
    include_package_data=True,  # To include non-Python files like install.sh
    long_description=open('README.md').read(),  # Add long description from README
    long_description_content_type='text/markdown',
    author='Yang Silicon',
    author_email='yangsiliconl@gmail.com',
    description='A macOS script to display the current week number in the menu bar.',
    url='https://github.com/Silicon27/weekdatemac',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
