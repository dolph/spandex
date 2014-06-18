import setuptools


setuptools.setup(
    name='spandex',
    version='0.0.0',
    description='Do something useful with elasticsearch.',
    author='Dolph Mathews',
    author_email='dolph.mathews@gmail.com',
    url='http://github.com/dolph/spandex',
    install_requires=['requests', 'pyyaml'],
    entry_points={'console_scripts': ['spandex = spandex.cli:main']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
    ],
)
