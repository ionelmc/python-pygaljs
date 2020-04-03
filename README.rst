========
pygal.js
========

.. list-table::
    :stub-columns: 1

    * - package
      - |version| |downloads|

.. |version| image:: https://img.shields.io/pypi/v/pygaljs.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pygaljs

.. |downloads| image:: https://img.shields.io/pypi/dm/pygaljs.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pygaljs

Python package providing assets from https://github.com/Kozea/pygal.js

* Free software: LGPLv3 license

Installation
============

::

    pip install pygaljs

Releasing
=========

::


    git submodule foreach "git fetch; git reset --hard origin/gh-pages"
    git submodule sync
