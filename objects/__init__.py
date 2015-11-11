# -*- coding: utf-8 -*-

import bpy as _bpy
import mathutils as _mathutils

def Plane(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_plane_add(*args, **kwargs)
    plane = _bpy.context.object
    if not name is None:
        plane.name = name
    
    return plane

def Cube(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_cube_add(*args, **kwargs)
    cube = _bpy.context.object
    if not name is None:
        cube.name = name
    return cube

def Circle(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_circle_add(*args, **kwargs)
    circle = _bpy.context.object
    if not name is None:
        circle.name = name
    return circle

def UVSphere(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_uv_sphere_add(*args, **kwargs)
    uv_sphere = _bpy.context.object
    if not name is None:
        uv_shere.name = name
    return uv_shere

def ICOSphere(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_ico_sphere_add(*args, **kwargs)
    ico_sphpere = _bpy.context.object
    if not name is None:
        ico_sphere.name = name
    return ico_sphere

def Cylinder(*args, name = None, **kwargs):
    _bpy.ops.mesh.primitive_cylinder_add(*args, **kwargs)
    cylinder = _bpy.context.object
    if not name is None:
        cylinder.name = name
    return cylinder

def Cone(*args, name = None, **kwargs):
	_bpy.ops.mesh.primitive_cone_add(*args, **kwargs)
	cone = _bpy.context.object

	if not name is None:
		cone.name = name

	return cone

def Torus(*args, name = None, **kwargs):
	_bpy.ops.mesh.primitive_torus_add(*args, **kwargs)
	torus = _bpy.context.object

	if not name is None:
		torus.name = name

	return torus

def Grid(*args, name = None, **kwargs):
	_bpy.ops.mesh.primitive_grid_add(*args, **kwargs)
	grid = _bpy.context.object

	if not name is None:
		grid.name = name

	return grid

def Monkey(*args, name = None, **kwargs):
	_bpy.ops.mesh.primitive_monkey_add(*args, **kwargs)
	monkey = _bpy.context.object

	if not name is None:
		monkey.name = name

	return monkey


class Polygon:
    pass
