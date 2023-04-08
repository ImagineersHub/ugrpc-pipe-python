from setuptools import setup, find_packages

setup(
    name='ugrpc_pipe',
    version='0.0.12',
    license='MIT',
    description='protobuf for grpc Pipe',
    author='esun',
    author_email='esun@voteb.com',
    url='https://github.com/ImagineersHub/unity-grpc-build-proto-pipe',
    keywords=['python', 'grpc'],
    packages=find_packages(),
    install_requires=[
        'grpcio==1.50.0',
        'grpcio-tools==1.50.0',
        'protobuf==4.21.8',
        'betterproto[compiler]>=2.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.10'
    ]
)
