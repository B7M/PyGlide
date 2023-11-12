Notebook preparation
====================
To use PyGlide, you need to prepare your notebook in a specific way. This page will show you how to prepare your notebook for PyGlide.

#. Open a new Jupyter notebook or use an existing one.
#. Add a markdown cell at the top of the notebook. Use level 1 heading to specify the title of the presentation and level 2 heading to specify the author and additional information.
#. Make sure each markdown cell is labeled with the right Slide Type (e.g. Slide, Sub-Slide, Fragment, Skip, Notes, etc.). This step is very **important** as it will determine the slide presentation and the audio files generated for each slide. The slide audio will be reflective of the notes provided in **Note** labeled cell.
#. While preparing the slides you may wish to receive input from the user. PyGlide allows you to receive input from the user as simple text or as executable code. To do so, you should use <div><!--Course_Text--></div> in any slides you want to receive *simple text*. This HTML line will not be visible in the output slides. It will be server as a target for PyGlide. Similarly, to add PyScript to your slides, you can use <div><!--Course_Code--></div> in any slides you want to receive executable code. The package will automatically convert the input cells into interactive cells in the output slides.


We included an example notebook in the package to show you how to prepare your notebook for PyGlide. To access the example notebook run the following line in the command line:

.. code-block:: bash

    pyglide original_example

This will generate a folder output which will contain the example notebook file. You can use this notebook to see how you can prepare your notebooks.