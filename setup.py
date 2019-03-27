"""A setuptools based setup module.
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='qencode',
    version='0.0.1',
    description='Qencode Python SDK',
    url='https://github.com/qencode-dev/qencode-api-python3-client',
    # url=here,
    author='Qencode Developer',
    author_email='team@qencode.com',
    license='proprietary',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.x'

    ],
    keywords='qencode, qencode.com, cloud.qencode.com',
    packages=['qencode']
)   