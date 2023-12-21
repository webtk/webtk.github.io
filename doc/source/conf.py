import faulthandler

faulthandler.enable()

project = 'webtk.github.io'
copyright = '2023, Taekyung Lee'
author = 'Taekyung Lee'
release = '0.0.1'

extensions = [
        'sphinx_design',
        ]

templates_path = ['_templates']
exclude_patterns = [
        '_build',
        'Thumbs.db',
        '.DS_Store',
        '**.ipynb_checkpoints'
        ]

pygments_style = 'friendly'

root_doc = 'index'
language = 'ko'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
