from distutils.core import setup

setup(
    # Metadata
    name='lab-gauth',
    version='0.1.0',
    description='Mostly drop in django app to use Google Apps for lab users.'
    packages=['fixtures',
              'migrations',
              'template'
    ],
    url='https://gitlab.com/thelabnyc/lab-gauth',
    license='ISC',
    author='Leilani Raranga',
    author_email='Leilani.Ann.Raranga@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],

    # Dependencies
    install_requires=[
        'Django>=1.9.6',
    ],

)
