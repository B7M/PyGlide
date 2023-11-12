Customize
=========

.. _installation:

Installation
------------

To use PyGlide on your personal computer, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pyglide

Check installation
------------------
To check that PyGlide is installed correctly, run the following command:
.. code-block:: console

   (.venv) $ pyglide

If PyGlide is installed correctly, you should see the following output:

.. code-block:: console

    > pyglide
      usage: pyglide [-h] [-v] [-m] [-p] [-i INPUT] [-t THEME] [filename]

      positional arguments:
      filename       Pass the file name without extension

      options:
      -h, --help     show this help message and exit
      -v, --version  Display the version of PyGlide
      -m, --mute     Mute the audio
      -p, --dPrompt  Disable prompt window
      -i INPUT       The file name without extension
      -t THEME       The theme of the out


The ``-h`` option displays the help message and exits. The ``-v`` option displays the version of PyGlide. The ``-m`` option mutes the audio. The ``-p`` option disables the prompt window(Tutor). The ``-i`` option specifies the file name without extension, for example if you wish to convert the notebook named `original_example.ipynb`, you will enter `original_example` and press enter. The ``-t`` option specifies the theme of the output. The theme is inherited from nbconvert package. The default theme is ``'light'``. The available themes are ``['light', 'dark', 'solarized']``.

To use the PyGlide after installation, you can either use the command line interface or import the package in your python code.
Once you prepared your notebook, open a terminal window, navigate to the directory where your notebook is located, and run the following command:

.. code-block:: console

    > pyglide 'filename'

where ``filename`` is the name of your notebook without the extension.

If you want to use PyGlide in your Python code, you can import the package and use it as a library. To use PyGlide, in python follow these steps:

Import the Gen class from the package:

.. code-block:: python

    import pyglide

or

.. code-block:: python
   from pyglide import *

Create an instance of the PyGlide, and pass the notebook file to the generator

.. code-block:: python
   generator = pyglide.Gen
   notebook_file = "path/to/your/notebook.ipynb"
   generator(notebook_file)

Host the notebooks
------------------

Now that your notebook is converted to a HTML, you can host it on a server. You can use any server you like, but we believe that the easiest way to host your notebook is to use Gihub Pages. To host your notebook on Github Pages. First, create a repository on Github. Make sure to enable Github Pages for your repository. Then, push your notebook to the ``gh-pages`` branch. Your notebook will be available at ``https://<username>.github.io/<repository_name>/<notebook_name>.html``.
