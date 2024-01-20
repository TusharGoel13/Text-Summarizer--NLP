import setuptools

# Read the content of README.md for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"  # Placeholder version, replace with actual version number
REPO_NAME = "Text-Summarizer--NLP"
AUTHOR_USER_NAME = "TusharGoel13"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "tushargoel4613@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",  # Specify that the long description is in markdown format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL to the project's repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  # Additional project URLs
    package_dir={"": "src"},  # Specify that the packages are located in the "src" directory
    packages=setuptools.find_packages(where="src")  # Automatically discover and include packages
)
