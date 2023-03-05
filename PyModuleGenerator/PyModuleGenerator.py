from dataclasses import dataclass
import os, shutil

@dataclass
class PyModuleGeneratorConfig:
    pythonCommand: str = "py"
    
    modulePath: str = ""
    buildFolder: str = ""

    moduleName: str = ""
    moduleVersion: str = ""
    moduleDescription: str = ""
    moduleLongDescription: str = ""
    moduleLongDescriptionType: str = ""

    githubURL: str = ""
    moduleAuthor: str = ""
    moduleAuthorEmail: str = ""
    moduleLicense: str = ""

    moduleDependencies: list[str] = ""
    moduleTags: list[str] = ""


def PyModuleGenerator(config: PyModuleGeneratorConfig, clearBuildFolder: bool = False, publishToPypi: bool = False) -> None:
    print("PyModuleGenerator: " + config.moduleName)

    # Create the build folder if it doesn't exist
    print("PyModuleGenerator: check build folder " + config.buildFolder)
    if not os.path.exists(config.buildFolder):
        print("PyModuleGenerator: create build folder " + config.buildFolder)
        os.makedirs(config.buildFolder)

    # Clear the build folder
    print("PyModuleGenerator: clear build folder")
    for file in os.listdir(config.buildFolder):
        print("PyModuleGenerator: remove " + file)
        os.remove(os.path.join(config.buildFolder, file))

    # Create the README.md file from the long description
    print("PyModuleGenerator: create README.md")
    readmeFile = open(os.path.join(config.buildFolder, "README.md"), "w")
    readmeFile.write(config.moduleLongDescription)
    readmeFile.close()

    # Create the setup.py file
    print("PyModuleGenerator: create setup.py")
    setupFile = open(os.path.join(config.buildFolder, "setup.py"), "w")
    setupFile.write("from setuptools import setup" + os.linesep)
    setupFile.write(os.linesep)
    setupFile.write('with open("README.md","r") as fh:' + os.linesep)
    setupFile.write("    long_description = fh.read()" + os.linesep)
    setupFile.write(os.linesep)
    setupFile.write("setup(" + os.linesep)
    setupFile.write("    name='" + config.moduleName + "'," + os.linesep)
    setupFile.write("    version='" + config.moduleVersion + "'," + os.linesep)
    setupFile.write("    description='" + config.moduleDescription + "'," + os.linesep)
    setupFile.write("    long_description=long_description," + os.linesep)
    setupFile.write("    long_description_content_type='" + config.moduleLongDescriptionType + "'," + os.linesep)
    setupFile.write("    url='" + config.githubURL + "'," + os.linesep)
    setupFile.write("    author='" + config.moduleAuthor + "'," + os.linesep)
    setupFile.write("    author_email='" + config.moduleAuthorEmail + "'," + os.linesep)
    setupFile.write("    license='" + config.moduleLicense + "'," + os.linesep)
    setupFile.write("    packages=find_packages()," + os.linesep)
    setupFile.write("    install_requires=[" + os.linesep)
    for dependency in config.moduleDependencies:
        setupFile.write("        '" + dependency + "'," + os.linesep)
    setupFile.write("    ]," + os.linesep)
    setupFile.write(os.linesep)
    setupFile.write("    classifiers=[" + os.linesep)
    for tag in config.moduleTags:
        setupFile.write("        '" + tag + "'," + os.linesep)
    setupFile.write("    ]," + os.linesep)
    setupFile.write(")" + os.linesep)
    setupFile.close()
    
    # Copy the module to the build folder
    print("PyModuleGenerator: copy module to build folder")
    shutil.copytree(config.modulePath, os.path.join(config.buildFolder, config.moduleName))

    # Check if the module is a package
    print("PyModuleGenerator: check if module is correctly packaged")
    os.chdir(config.buildFolder)
    os.system(config.pythonCommand+" setup.py check")
    input("Everything look good? Press enter to continue...")
    
    # Build the module
    print("PyModuleGenerator: build module")
    os.system(config.pythonCommand+" setup.py sdist")

    # Publish the module
    if publishToPypi:
        print("PyModuleGenerator: publish module")
        os.system("twine upload dist/*")

    # Clean up
    if clearBuildFolder:
        print("PyModuleGenerator: clean up")
        os.chdir(config.modulePath)
        os.system("rmdir /s /q " + config.buildFolder)
    return
