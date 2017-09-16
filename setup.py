import setuptools

setuptools.setup(
    name="gimme_input",
    version="0.1.0",
    url="https://github.com/dcdanko/gimme_input",

    author="David C. Danko",
    author_email="dcdanko@gmail.com",

    description="A library of useful functions to get input from users for command line programs.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
