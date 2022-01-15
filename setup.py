from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version = "0.0.1",
    description="a small project",
    author="Divya",
    long_description = long_description,
    author_email = "divyaakshay011@gmail.com",
    long_description_content_type = "text/markdown",
    url = "https://github.com/Divya748/dvc_project",
    package_dir = {"":"src"},
    packages= find_packages(where = "src"),
    license="GNU",
    python_requires =">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]'
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)