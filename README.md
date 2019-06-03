# Portability In Action

What does Facebook's portability platform really look like? This repository will let you explore some anonymized data and anonymize your own data if you so desire.

The anonymized Facebook data can be found in the folder `facebook-data-anonymous`. To get a sense of how the data in each file is structured, check out `datastructures.json`. This file contains the basic anonymization rules, and can give a less overwhelming sense of the barebones structure of the data set.

More technically inclined users can either poke around this data using pandas in a Jupyter Notebook or download and anonymize their own data.

## Environment Setup / Running

Before running any of the code in this project, make sure to set up the environment.

```
pipenv --python 3.5 shell
pipenv install
```

To explore the data using a [Jupyter Notebook](https://jupyter.org/install), simply run the `jupyter notebook` command in the terminal, and when `http://localhost:8888/` opens on the browser, select `notebooks/pandas_sandbox.ipynb`

To anonymize your own data, [download your data from Facebook](https://www.facebook.com/help/1701730696756992?helpref=hc_global_nav) as a JSON and move the `facebook-data` folder you get into this directory. Your own anonymized data should appear in teh `facebook-data-anonymous` folder after running:

```
cd scripts
python anonymize_data.py
```