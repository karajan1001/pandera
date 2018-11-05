from setuptools import setup


setup(
    name="pandera",
    version="0.0.1",
    author="Niels Bantilan",
    author_email="niels.bantilan@gmail.com",
    description="A pandas data structure validation library",
    url="https://github.com/cosmicBboy/pandera",
    keywords=["pandas", "validation", "data-structures"],
    license="MIT",
    install_requires=[
        "numpy >= 1.9.0",
        "pandas >= 0.23.0",
        "schema >= 0.6.8",
        "wrapt",
    ]
)
