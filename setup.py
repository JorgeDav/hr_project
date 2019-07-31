from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme=f.read()

setup(
    name="hr",
    version="0.1.0",
    description="Manage users on a server based on an 'inventory' JSON file",
    author="Jorge",
    author_email="jorge.davilardz@hotmail.com",
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
            'console_scripts':['hr=hr.cli:main',]
        }
)
