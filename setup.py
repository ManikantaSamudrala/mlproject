from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This will give list of file requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [line.replace("\n", "") for line in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(name='mlproject',
      version=0.01,
      author='Manikanta Samudrala',
      author_email='samudralamanikanta@gmail.com',
      packages=find_packages(),
      install_requires=['pandas', 'numpy', 'seaborn']

      )
