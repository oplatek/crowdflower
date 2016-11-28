from setuptools import setup, find_packages

setup(
    name='crowdflower',
    version='0.1.5',
    author='Christopher Brown, Python3 fixes Ondrej Platek',
    author_email='io@henrian.com, ondrej.platek@seznam.cz',
    url='https://github.com/oplatek/crowdflower',
    keywords='crowdflower crowdsourcing api client',
    description='CrowdFlower API - Python client',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        # https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
        'requests>=2.0.0',
    ],
)
