from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function returns a list of requirements.
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Reading lines from the file
            lines = file.readlines()
            # Process each line
            for i in lines:
                requirement = i.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('File not found')

    return requirement_lst


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Yash Gaikwad',
    author_email='yashsgaikwad23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)