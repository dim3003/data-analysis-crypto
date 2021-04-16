# Advanced data analysis

```bash
git clone https://github.com/GuillaumePv/data-analysis-crypto.git
```
2) installer les librairies nécessaires pour le projet

Python 2
```bash
pip install -r requirements.txt
```

Python 3
```bash
pip3 install -r requirements.txt
```
## Data

put datasets in the "raw" folder 

# Project structure

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Struturing project
* https://drivendata.github.io/cookiecutter-data-science/
* https://towardsdatascience.com/structuring-machine-learning-projects-be473775a1b6
* https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600

# TO-DO

* merge data

* scrap all data form twitter -> use threading

* add access to google drive :) https://medium.com/@chingjunetao/simple-way-to-access-to-google-service-api-a22f4251bb52

* create a structure tree for the report
https://github.com/hbast/pyTree

* paramétrer les output du notebooks pour éviter que ça prenne trop de storage pour github

* enlever les tweets qui sont dupliquer

* tester Prophet AI (Facebook) => améliorer notre model 
* https://facebook.github.io/prophet/docs/diagnostics.html#cross-validation

