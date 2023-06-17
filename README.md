# Lispi Documentation

## Introduction

`lispi` (Learning Interactive Slides and PIthon) is a Python package that provides a convenient way to convert Jupyter notebooks into interactive slides. It allows users to create engaging presentations with interactive elements directly from the slides.

## Installation

To install `lispi` package, you can use pip, the Python package installer. Open your terminal and run the following command:

```
pip install lispi
```

## Usage
### Command Line Interface
To use lispi, in your terminal follow these steps:
After installing the package, you can use the `lispi` command to convert your Jupyter notebook into interactive slides. In your terminal, navigate to the folder containing the notebooks and run the following command:

```lispi```

Upon running the command, the package will prompt you to enter the path to your Jupyter notebook file. Enter the name of the file press enter. The package will convert the Jupyter notebook into interactive slides and save the output HTML file in the output folder in the same directory as html file and audio file folder.

### Python
If you want to use lispi in your Python code, you can import the package and use it as a library. To use lispi, in python follow these steps:

1. Import the `Gen` class from the package:

   ```python
   import lispi
   ```
   or 

   ```python
    from lispi import *
   ```

2. Create an instance of the `Interactive Slides Generator` class:

   ```python
   generator = lispi.Gen
   ```

3. Specify the Jupyter notebook file you want to convert:

   ```python
   notebook_file = "path/to/your/notebook.ipynb"
   ```

4. Generate the interactive slides:

   ```python
   generator(notebook_file)
   ```

5. The package will convert the Jupyter notebook into interactive slides and save the output HTML file in the output folder in the same directory as html file and audio file folder.

## Configuration

Lispi provides several configuration options to customize the output slides. You can pass these options as arguments when creating an instance of the `lispi` class. Here are the available configuration options:

- `audio`: Specify if you wish the output without audio (default: "unmute").
- `output_file`: Specify the output file path for the generated slides (default: "output.html").

Example:

```python
generator = lispi(
    audio="unmute",
    output_file="path/to/output/slides.html"
)
```

## Examples

Here is an example that comes with the package. To run the example, in your terminal or python code provide 'original_example' as the file name.

```python
import lispi

# Create an instance of the lispi class
generator = lispi.Gen

# Specify the example notebook file
notebook_file = "original_example"

# Generate the interactive slides
generator(notebook_file)
```

## Conclusion

Lispi package provides a convenient way to convert Jupyter notebooks into interactive slides. It allows users to create engaging presentations with interactive elements easily. By following the installation and usage instructions outlined in this documentation, you can leverage this package to generate interactive slides from your Jupyter notebooks effortlessly.
