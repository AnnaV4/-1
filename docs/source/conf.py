import os
import sys



sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'djangotutorial')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

project = 'practica'
copyright = '2025, AnnaV'
author = 'AnnaV'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints', 
    'sphinxcontrib_django',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
