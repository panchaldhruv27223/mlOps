import os
from pathlib import Path

listOfFile = [
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/dataIngestion.py",
    "src/components/dataTransformation.py",
    "src/components/modelTrainer.py",
    "src/components/modelEvaluation.py",
    "src/pipeLine/__init__.py",
    "src/pipeLine/trainingPipeline.py",
    "src/pipeLine/predictionPipeline.py",
    "src/utils/__init__.py",     
    "src/utils/util.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirementsDev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for filePath in listOfFile:

    filePath = Path(filePath)

    fileDir, fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir,exist_ok = True)

    if (not os.path.exists(filePath)) or (os.path.getsize(fileName)==0) :
        with open(filePath,"w") as f:
            pass

