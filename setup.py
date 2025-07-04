from setuptools import setup, find_packages

setup(
    name='ethernet_communication', 
    version='0.1.0',
    author='None',
    author_email='None',
    description='CNN communication library based on ethernet.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),  # tools 폴더를 패키지로 포함
    package_dir={'': '.'},
    include_package_data=True,
    install_requires=[
        'torch',
        'torchvision',
        'Pillow',
        'numpy'
    ],
    python_requires='>=3.11',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
