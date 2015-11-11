# Blender Python API Wrapper

A simple wrapper based on `bpy`.

## Motivation

I don't like the api provided by the `bpy` module. It is not ituitive to use it.

## Basic Usage

**All these scripts must be run under Blender rather than standard python**

```{python}
from blender_wrapper import *
from blender_wrapper.objects.operations import *

cube = Cube(name = 'MyCube', location = (2, 1, 3), radius = 0.5) # Add a cube with name.
cube.name
# >>> 'MyCube'
select_object("MyCube")  # Select object by name
```

## Installation

- go to the Blender application folder and find the python folder.
	- For `Mac`, it would be `/Applications/Blender/blender.app/Contents/Resources/2.76/python/lib/python3.4/site-packages`
- run `git clone https://github.com/dboyliao/blender_wrapper.git`

## To Do

- Creation of `Polygon` object.
	- An object definded by its vertex and edges.
- Transformation to objects
	- rotation, transition,...etc