import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='skip-onesignal-client',
    version='0.1.0',
    url='https://github.com/skip-pay/onesignal-client',
    description='OneSignal API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Radim Sückr, Skip Pay Developers',
    author_email='developers@skippay.cz',
    packages=['onesignal'],
    install_requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
