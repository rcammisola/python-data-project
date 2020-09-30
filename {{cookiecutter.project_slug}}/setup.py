import os

from setuptools import setup, find_packages


def readme():
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    :return: String
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


def requirements_contents(filename="requirements.txt"):
    """
    Read the contents of a requirements.txt file so that we can use the list
    in the install_requires for the package.

    :param filename:
    :return:
    """
    with open(filename) as f:
        requirements = f.read().splitlines()

    requirements = [r for r in requirements if not r.startswith("-")]
    return requirements


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    url='',
    license='',
    author='{{ cookiecutter.full_name.replace("\'", "\\\'") }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_short_description }}',
    python_requires='>=3',
    long_description=readme(),
    install_requires=requirements_contents(),
    extras_require={
        'dev': requirements_contents("requirements-dev.txt"),
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
