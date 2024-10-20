from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento-imagem",
    version="0.0.1",
    author="ANderson",
    description="pacote para processamento de imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anderson-si/dio-dados/tree/main/pacote-processamento-imagens/processamento-imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)