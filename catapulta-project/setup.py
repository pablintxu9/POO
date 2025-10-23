from setuptools import setup, find_packages

setup(
    name='catapulta-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Aquí puedes agregar las dependencias necesarias
    ],
    entry_points={
        'console_scripts': [
            'catapulta=main:main',  # Asumiendo que main.py tiene una función main()
        ],
    },
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Un proyecto de catapulta en Python utilizando programación orientada a objetos.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/catapulta-project',  # Cambia esto por la URL de tu repositorio
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Cambia esto si usas otra licencia
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)