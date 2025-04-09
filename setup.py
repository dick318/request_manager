# setup.py
from setuptools import setup, find_packages

setup(
    name='request_manager',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,  # 这一行确保包含非 Python 文件
    package_data={
        # 包含所有指定包下的js文件
        'request_manager': ['*.js'],
    },
    install_requires=[
        'curl_cffi==0.10.0',
        'schedule==1.2.2',
        'PyExecJS==1.5.1'
    ],
    author='dick',
    author_email='dick@qq.com',
    description='1',
    url='https://github.com/dick318/request_manager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    semaphore='5',
    python_requires='>=3.6',

)
