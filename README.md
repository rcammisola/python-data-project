# Cookiecutter for Python Data Projects

This is a template cookiecutter project for bootstrapping your work on python data projects. It contains :

- a directory structure for sorting your notebooks, data, models, figures, tasks and source code to reuse in notebooks
- a conda environment file with the basic python libraries and some extras :
  - numpy / pandas / scikit-learn / seaborn / statsmodels / plotly / jupyterlab classic Data Science stack
  - [lightgbm](https://lightgbm.readthedocs.io/en/latest/) for prediction
  - [missingno](https://github.com/ResidentMario/missingno) for missing data analysis
  - [invoke](http://docs.pyinvoke.org/) as a replacement to `Makefile` for managing project tasks
  - [nbdime](https://github.com/jupyter/nbdime) for diffing and merging notebooks
  - [path.py](https://pathpy.readthedocs.io/en/stable/) for browsing files in Python
  - [kaggle-api](https://github.com/Kaggle/kaggle-api) a CLI for interacting with Kaggle API (Optional)
  - pytest and coverage (with badges)

The template post-hook will: 
* install itself as a package
* add an ipykernel so that the environment is properly referenced by Jupyter

## Prerequisites

- [Cookiecutter](https://github.com/audreyr/cookiecutter) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```bash
$ pip install cookiecutter
```

## Generate a new project

In a folder where you want your project generated :
`cookiecutter git@github.com:rcammisola/python-data-project.git`

You can also clone the project in `<path/to/template>`,
and from the folder where you want to generate your project, launch `cookiecutter <path/to/template>`

It will ask for the following values :

```
full_name
email
project_name
project_short_description
python_version
version
for_kaggle
```

Complete the values for your project and voilà ! Then follow the `README` inside your new project for further installation.

## Contributing guide

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## Credits

This project is heavily influenced by [drivendata's Data Science cookiecutter](https://github.com/drivendata/cookiecutter-data-science) 
and [cookiecutter Kaggle template project](https://github.com/andfanilo/cookiecutter-kaggle).

Other links that helped shape this cookiecutter :

- [Write less terrible code with Jupyter Notebook](https://blog.godatadriven.com/write-less-terrible-notebook-code)
- [Cookiecutter DataScience Opinions](http://drivendata.github.io/cookiecutter-data-science/#opinions)
- [Working efficiently with JupyterLab](https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/)
- [Python Packaging - Ionel's Codelog](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure)

## TODO:

* Git init
* Add nb-clean to dev requiremnts
* Add bumpversion
