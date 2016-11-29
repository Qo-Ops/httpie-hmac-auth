from setuptools import setup

setup(
    name='httpie-aws-auth',
    description='AWS auth plugin for HTTPie',
    long_description=open('README.rst').read().strip(),
    version='0.0.1',
    author='Ilya Gladyshev',
    keywords='aws httpie authentication',
    author_email='ilya.v.gladyshev@gmail.com',
    license='MIT',
    py_modules=['httpie_aws_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_aws_auth = httpie_aws_auth:AWSAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
