from setuptools import setup, find_packages

readme = open('README.md').read()
history = open('HISTORY.md').read()
reqs = [x.strip() for x in open('requirements.txt').readlines()]

setup(
    name='decorated_registry',
    version='0.0.2',
    author='Andrey Cizov',
    author_email='acizov@gmail.com',
    packages=find_packages(include=('decorated_registry', 'decorated_registry.*',)),
    description='Decorator-based registry for objects with arbitrary payloads',
    keywords='',
    url='https://github.com/andreycizov/python-decorated_registry',
    include_package_data=True,
    long_description=readme,
    install_requires=reqs,
    entry_points={
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
