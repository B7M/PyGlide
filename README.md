# Lispi Documentation

## Introduction

Lispi (Educational Slide Studio) is a Python package that provides a convenient way to convert Jupyter notebooks into interactive slides. It allows users to create engaging presentations with interactive elements directly from the slides.

## Installation

To install `lispi` package, you can use pip, the Python package installer. Open your terminal and run the following command:

```
pip install lispi
```

## Usage

To use lispi, follow these steps:

1. Import the `lispi` class from the package:

   ```python
    import lispi
   ```

2. Create an instance of the `InteractiveSlidesGenerator` class:

   ```python
   generator = lispi()
   ```

3. Specify the Jupyter notebook file you want to convert:

   ```python
   notebook_file = "path/to/your/notebook.ipynb"
   ```

4. Generate the interactive slides:

   ```python
   generator.generate_slides(notebook_file)
   ```

5. The package will convert the Jupyter notebook into interactive slides and save the output HTML file.

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

Here are a few examples demonstrating the usage of `lispi`:

```python
from lispi import lispi

# Create an instance of the lispi class
generator = lispi()

# Specify the Jupyter notebook file
notebook_file = "path/to/your/notebook.ipynb"

# Generate the interactive slides
generator.generate_slides(notebook_file)
```

## Conclusion

Lispi package provides a convenient way to convert Jupyter notebooks into interactive slides. It allows users to create engaging presentations with interactive elements easily. By following the installation and usage instructions outlined in this documentation, you can leverage this package to generate interactive slides from your Jupyter notebooks effortlessly.
