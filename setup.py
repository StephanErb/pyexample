from setuptools import setup, find_packages

setup(
    name='test-package',
    packages=find_packages(exclude=['tests']),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
