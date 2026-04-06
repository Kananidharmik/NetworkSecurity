''' The setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools (or distutils in older Python versions) to define the configration of yout project, such as its metadat, dependencies, and more '''


from setuptools import setup, find_packages
from typing import List

def get_requirements()->list[str]:
    '''This function reads the requirements.txt file and returns a list of requirements'''
    
    requirement_list:list[str] = []

    try:
        with open('requirements.txt', 'r') as file :
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found." )

    return requirement_list

print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Dharmik Kanani",
    author_email = "dharmikkanani333@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)