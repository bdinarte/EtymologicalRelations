from setuptools import setup, find_packages

setup(
    name="tec.ic.ia.p2.g03",
    packages=find_packages(),
    description="Inteligencia Artificial: Proyecto II",
    long_description="Etymological Relations",
    version="1.0.0",
    author="Julian Salinas, Brandon Dinarte, Armando López",
    license="GNU General Public License v3.0",
    install_requires=['pandas', 'numpy', 'pyDatalog'],
    python_requires='>=3',
    include_package_data=True,
    package_data={"tec": ["*.txt", "*.csv", "*.xlsx", "*.pyc", "*.tsv"]},
    classifiers=[],
)
