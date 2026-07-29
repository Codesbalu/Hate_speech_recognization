import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="hate_speech"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_evalution.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/util.py",
    "notebook/Experiment.ipynb",
    ".dockerignore",
    "app.py",
    "demo.py",
    "Dockerfile",
    "setup.py",
    "tokenzier.pickle"
]

for filepath in list_of_files:
    filepath=Path(filepath)

    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creaing_directory: {filedir} for the file{filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")