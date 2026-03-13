from setuptools import setup, find_packages
from typing import List



def get_requirements() -> List[str]:
    requirements_list:List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            lines=file.readlines()
            for line in lines:
                requirements =line.strip()
                ##ignore empty lines and e- .
                if requirements and not requirements.startswith('-e .'):
                    requirements_list.append(requirements)
            
    except FileNotFoundError:
        print(f"Error: requirements.txt file not found.")
    return requirements_list  


setup(
    name='Network_Security',
    version='0.0.1',
    author='David Ayman',
    author_email="davaidayman259@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
