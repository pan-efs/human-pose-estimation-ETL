from setuptools import setup, find_packages

setup(
    name="automated-etl-hpe",
    version="0.0.1",
    description="""
        An automated pipeline tool which works like that --> [E]xtract images locally, 
        [T]ransform them and apply a human pose estimation model on them
        and [L]oad them (+ more details) into PostgreSQL database system.""",
    url="https://github.com/pan-efs/automated-etl-hpe",
    author="Panagiotis Efstratiou",
    author_email="pefstrat@gmail.com",
    license="",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)