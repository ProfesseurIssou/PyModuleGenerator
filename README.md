# PyModuleGenerator
 Module to generate a python module

## Installation
```bash
pip install PyModuleGenerator
```

## Prerequisites
### Folders
- Module folder
- - src
- - - \_\_init\_\_.py
- - - MyModule.py
- - - README.md
- - - LICENSE
- - - .gitignore
### \_\_init\_\_.py
```python
"""
pyexample.

An example python library.
"""

__version__ = "1.0.0"
__author__ = 'Your Name'
__credits__ = '###'

{{Rest of the file}}
```

## Utilisation
```python
import PyModuleGenerator

config: PyModuleGenerator.PyModuleGeneratorConfig = PyModuleGenerator.PyModuleGeneratorConfig(
    pythonCommand="python",    # Python command to use (python or python3 or py)

    modulePath="C:/.../MyModuleFolder/src",
    buildFolder="C:/.../MyModuleFolder/build",
    moduleName="MyModule",
    moduleVersion="1.0.0",
    moduleDescription="My module description",
    moduleLongDescription="My module long description displayed on pypi", # You can read file from README.md
    moduleLongDescriptionType="text/markdown",

    githubURL="",
    moduleAuthor="My name",
    moduleAuthorEmail="",
    moduleLicense="MIT",

    packages=["MyModule"],
    moduleDependencies=[],
    moduleTags=[], # https://pypi.org/classifiers/
)


PyModuleGenerator.PyModuleGenerator(
    config=config,
    clearBuildFolder=False,      # Erase the build folder after the build
    publishToPypi=False          # Publish the module to pypi
)
```