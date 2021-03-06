import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    coverage_string: str = "![Coverage report](https://github.com/ZPascal/grafana_api_sdk/blob/main/docs/coverage.svg)"
    long_description: str = fh.read()

long_description = long_description.replace(coverage_string, "")

setuptools.setup(
    name="grafana-api-sdk",
    version="0.0.7",
    author="Pascal Zimmermann",
    author_email="info@theiotstudio.com",
    description="A Grafana API SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZPascal/grafana_api_sdk",
    project_urls={
        "Source": "https://github.com/ZPascal/grafana_api_sdk",
        "Bug Tracker": "https://github.com/ZPascal/grafana_api_sdk/issues",
        "Documentation": "https://zpascal.github.io/grafana_api_sdk/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["requests"],
    python_requires=">=3.6",
)
