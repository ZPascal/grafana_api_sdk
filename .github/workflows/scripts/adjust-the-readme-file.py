with open("README.md", "r", encoding="utf-8") as fh:
    coverage_string: str = "![Coverage report](https://github.com/ZPascal/grafana_api_sdk/blob/main/docs/coverage.svg)"
    long_description: str = fh.read()

with open("README.md", "w", encoding="utf-8") as fh:
    fh.write(long_description.replace(coverage_string, ""))
