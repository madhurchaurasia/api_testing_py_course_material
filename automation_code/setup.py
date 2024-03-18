from setuptools import setup, find_packages


setup(
    name='ssqaapitest',
    version='1.0',
    description="Practice API testing",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "pytest==8.1.1",
        "pytest-html==4.1.1",
        "requests==2.31.0",
        "requests-oauthlib==1.4.0",
        "PyMySQL==1.1.0",
        "WooCommerce==2.1.1"
    ]
)
