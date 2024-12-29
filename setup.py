from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT='-e .'

def get_requirements(file_path:str)->List:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Aditya',
    author_email='aditya29jadhav@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)