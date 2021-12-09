from setuptools import setup, find_packages

setup(
    name="automated-etl-3dhpe",
    version="0.0.1",
    description="""
        An automated pipeline tool which works like that
        --> [E]xtract images locally, [T]ranform them applying a 3D human pose estimation model
        and [L]oad them (+ more details) into PostgreSQL database.""",
    url="https://github.com/pan-efs/AutomatedETL_3DHPE",
    author="Panagiotis Efstratiou",
    author_email="pefstrat@gmail.com",
    license="",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)