import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grafana-api-sdk",
    version="0.0.1",
    author="Pascal Zimmermann",
    author_email="info@theiotstudio.com",
    description="A Grafana API SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZPascal/grafana_api_sdk",
    project_urls={
        "Bug Tracker": "https://github.com/ZPascal/grafana_api_sdk/issues",
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
