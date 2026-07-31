# Hate Speech Recognization

The Hate Speech Recognization project applies Natural Language Processing (NLP) and Machine Learning (ML) techniques to detect and categorize hateful, abusive, or offensive text. It provides an end-to-end pipeline for ingesting text data, transforming it for model training, training/evaluating models, and packaging/pushing trained artifacts for deployment.

## Quick summary
- Detects and categorizes hate speech in text data.
- Organized as a Python package with components for ingestion, transformation, training, evaluation and deployment.
- Useful for researchers, ML engineers, and developers building content moderation or text classification systems.

## Stack
- Language(s): Python (100%)
- Runtime / Framework: Plain Python (project is structured as a package; add a web framework or inference-serving framework as needed)
- Notable project modules: hate_speech.components (pipeline steps), hate_speech.ml (model code), hate_speech.configuration (cloud sync helpers)

## Repository layout (top-level)
```
.gitignore
.dockerignore
Dockerfile
LICENSE
README.md             <- (this file)
requirements.txt
setup.py
app.py                 <- application / entry point (inspect to learn runtime)
demo.py                <- demo script
template.py            <- example / helper script
tokenzier.pickle       <- serialized tokenizer artifact (note spelling)
notebook/              <- Jupyter notebooks
hate_speech/           <- package: core pipeline, ml, utils, config
hate_speech/components/        data_ingestion.py, data_transformation.py, model_trainer.py, model_pusher.py, model_evalution.py
hate_speech/configuration/     gcloud_syncer.py
hate_speech/constants/         __init__.py
hate_speech/entity/            config_entity.py, artifact_entity.py
hate_speech/exception/         project-specific exceptions
hate_speech/logger/            logging utilities
hate_speech/ml/                model.py
```

How it fits together
- The project is structured as a small Python package. The "components" folder groups pipeline steps (ingest, transform, train, evaluate, push). The "ml" folder contains model definition(s) and the serialized tokenizer lives at the repository root. The app.py / demo.py files appear to be entry points for running the application or demo — inspect them to confirm whether they start a server, CLI, or run example flows.

## Installation

1. Clone the repository
```bash
git clone https://github.com/Codesbalu/Hate_speech_recognization.git
cd Hate_speech_recognization
```

2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
# Unix / macOS
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
# optionally
python setup.py install
```

Notes:
- Inspect `requirements.txt` and `setup.py` to ensure versions and extras match your environment.

## Quick start / Usage

Run the demo (if demo script implements a runnable example):
```bash
python demo.py
```

Run the app (if `app.py` implements a web app or CLI):
```bash
python app.py
```


## Training pipeline (high-level)
The repository includes pipeline components intended for a standard ML workflow:

- Data ingestion: `hate_speech/components/data_ingestion.py`
- Data transformation / preprocessing: `hate_speech/components/data_transformation.py`
- Model training: `hate_speech/components/model_trainer.py`
- Model evaluation: `hate_speech/components/model_evalution.py`
- Model push / deployment helpers: `hate_speech/components/model_pusher.py`
- Artifacts and config: `hate_speech/entity/*`, `hate_speech/constants`, `tokenzier.pickle`
- Cloud sync helper: `hate_speech/configuration/gcloud_syncer.py` (for uploading artifacts to cloud storage)

Typical workflow (adjust to actual function/class names in the code):
1. Place raw dataset in a data/ directory (CSV/JSON with text and label columns).
2. Run ingestion to produce cleaned/extracted files.
3. Transform text (tokenize, vectorize) — tokenizer artifact exists at `tokenzier.pickle`.
4. Train model and save artifacts under an artifacts directory.
5. Evaluate the model locally using evaluation scripts.
6. Push artifacts to cloud storage or model registry using `model_pusher` and `gcloud_syncer`.

## Web app (app.py) — FastAPI

The repository exposes a small FastAPI application in `app.py` that provides two main endpoints and a docs UI:

- Framework: FastAPI + Uvicorn
- Entry point imports:
  - TrainPipeline from `hate.pipeline.train_pipeline`
  - PredictionPipeline from `hate.pipeline.prediction_pipeline`
  - CustomException from `hate.exception`
  - APP_HOST and APP_PORT from `hate.constants`

Behavior / endpoints
- GET /  
  - Redirects to the automatic API docs at /docs (Swagger UI).
- GET /train  
  - Triggers a pipeline run: constructs `TrainPipeline()` and calls `train_pipeline.run_pipeline()`.
  - Response: 200 with "Training successful !!" on success, or a 500-style Response containing the exception message on failure.
- POST /predict  
  - Runs `PredictionPipeline()` and calls `obj.run_pipeline(text)` where `text` is provided as a request query parameter.
  - Note: the endpoint signature is `async def predict_route(text)`, so FastAPI expects `text` as a required query parameter (e.g., /predict?text=...).
  - Response: whatever `PredictionPipeline.run_pipeline` returns (e.g., prediction / label / scores). Exceptions are raised as `CustomException`.

How to run the app
- From the repository root (APP_HOST and APP_PORT are read from `hate.constants`):
```bash
# run via the module entry point
python app.py

# or use uvicorn directly (recommended for development with reload)
uvicorn app:app --reload --host 0.0.0.0 --port 8000

Because some component files in the repository are present as pipeline placeholders, inspect each component module for the exact function and class names and adapt the commands accordingly.

## Inference example
A basic inference flow (pseudocode — inspect `app.py` / `template.py` to find exact entry points):
```python
from hate_speech.ml.model import load_model, predict
# or
# from template import run_inference_example

model = load_model("artifacts/model.pkl")
tokenizer = load_tokenizer("tokenzier.pickle")
pred = predict(model, tokenizer, "Sample input text to classify")
print(pred)
```
Replace function/class names above with the actual names used in the code.

## Notes & repository observations
- The repository contains a serialized tokenizer file `tokenzier.pickle` (note the filename spelling; consider renaming to `tokenizer.pickle` to avoid confusion).
- Several modules appear to be placeholders or small; open `hate_speech/components/` files to verify they contain the expected implementations (some files are present but empty or minimal).
- There is a `Dockerfile` present — ensure it includes the correct runtime commands and exposes the port your app uses, or update it.

## Tests
- There are no explicit test files at the repository root. Consider adding unit tests (pytest) for:
  - Data ingestion and transformation functions
  - Model training/evaluation pipeline
  - Inference/prediction functions

## Contributing
If you want to contribute:
- Open an issue describing the feature or bug.
- Fork the repo, create a feature branch, make changes, and open a pull request.
- Add tests for new features and ensure the pipeline example runs end-to-end.

Suggested contribution roadmap:
- Add clear example dataset and a short notebook that reproduces training -> evaluation -> inference.
- Add unit tests and CI for basic pipeline runs.
- Improve packaging and entry points (console_scripts in setup.py) to make running pipeline components easier.

## License
This project is provided under the LICENSE in the repository root. Please review it before using or contributing.

## Contact / Authors
See repository owner on GitHub: Codesbalu
