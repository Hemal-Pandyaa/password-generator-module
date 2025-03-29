from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Hemal Pandya",
    author_email="your_email@example.com",
    description="A customizable password generator with entropy-based length calculation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/password_generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13',
)
