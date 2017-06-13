"""A setup module for pip"""
from setuptools import setup, find_packages
setup(
    name='TurbulentTailing',
    version='1.0.0',
    description='A car chase game where you avoid obstacles and try not to get captured.',
    url='https://github.com/ncarr/ICS2O1Final',

    author='Victor Lin and Nicholas Carr',
    license='MIT',

    classifiers=[
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries :: pygame',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7'
    ],
    keywords='pygame game car',
    packages=find_packages(),
    install_requires=['pygame']
)
