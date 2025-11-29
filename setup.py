from setuptools import setup, find_packages

setup(
    name="paybin-sdk",
    version="0.0.0",  # Version will be set by CI/CD
    description="Official Python SDK for Paybin API",
    author="Paybin",
    author_email="support@paybin.io",
    url="https://github.com/paybin/paybin-python",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
