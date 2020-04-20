from setuptools import setup, find_packages

setup(
    name="blobfish-ejbca-client-python",
    version="0.1.0",
    author="Jaime Hablutzel",
    author_email="hablutzel1@gmail.com",
    description="Blobfish's Python client for EJBCA services.",
    packages=find_packages(),
    # TODO determine if it would be a good practice to create a requirements.txt in addition to the following
    #  'install_requires'.
    install_requires=[
        # TODO evaluate to put some version restrictions here.
        "zeep",
        "pyOpenSSL"
    ]
)
