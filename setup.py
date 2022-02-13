from setuptools import setup, find_packages

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="django_tailwind",
    version="1.0",
    description="Django Tailwind utilities",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
)
