import PyModuleGenerator

long_description = open("D:\Dev\Projects\PyModuleGenerator\README.md", "r", encoding="utf-8").read()

config: PyModuleGenerator.PyModuleGeneratorConfig = PyModuleGenerator.PyModuleGeneratorConfig(
    pythonCommand="py",    # Python command to use (python or python3 or py)

    modulePath="D:\\Dev\\Projects\\PyModuleGenerator\\PyModuleGenerator",
    buildFolder="D:\\Dev\\Projects\\PyModuleGenerator\\build",
    moduleName="PyModuleGenerator",
    moduleVersion="1.0.1",
    moduleDescription="A simple python module generator",
    moduleLongDescription=long_description,
    moduleLongDescriptionType="text/markdown",

    githubURL="https://github.com/ProfesseurIssou/PyModuleGenerator",
    moduleAuthor="Alix Hamidou",
    moduleAuthorEmail="alix.hamidou@gmail.com",
    moduleLicense="MIT",

    packages=["PyModuleGenerator"],
    moduleDependencies=[
        "setuptools==63.2.0",
        "twine==3.8.0"
    ],
    moduleTags=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ] # https://pypi.org/classifiers/
)


PyModuleGenerator.PyModuleGenerator(
    config=config,
    clearBuildFolder=True,      # Erase the build folder after the build
    publishToPypi=True          # Publish the module to pypi
)