from setuptools import setup

setup(
    name='cloudinary-upload',
    version='0.0.1',
    description='Upload a signed image to cloudinary effectively',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url='https://github.com/faradayafrica/cloudinary-image-upload', 
    license='CC0 1.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3'
    ],
    keywords=['cloudinary', 'media asset'],
    install_requires=[
        'cloudinary',
        'python-decouple'
        'importlib-metadata; python_version <= "3.9"',
    ],
)