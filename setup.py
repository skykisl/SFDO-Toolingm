"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name="sfdo-template-helpers",  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.15.0",  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="A set of Django helpers and utils used by sfdo-template projects.",
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    author="David Glick",  # Optional
    author_email="dglick@salesforce.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],  # Optional
    packages=find_packages(),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "markdown (>=3.0,<4.0)",
        "bleach (>=3.0,<4.0)",
        "django (>=2.1,<4.0)",
        "djangorestframework (>=3.9,<4.0)",
        "cryptography (>=2.5,<3.0)",
        "django-filter (>=2.1,<3.0)",
        "logfmt (>=0.4,<1.0)",
    ],
    extras_require={"test": ["django-allauth",]},
    # https://stackoverflow.com/a/16576850
    include_package_data=True,
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={},  # Optional
)
