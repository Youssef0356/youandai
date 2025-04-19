from setuptools import setup, find_packages

setup(
    name='YouAndAi',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'google-generativeai'
    ],
    entry_points={
        'console_scripts': [
            'youandai=youandai.game:main',
        ],
    },
    author='Youssef0356',
    description='A minimalist AI-powered text adventure game.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Youssef0356/youandai',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
