# -*- coding: utf-8 -*-

import bpy as _bpy
import mathutils as _mathutils
from . import meta_classes

class BlenderObject:
    __primitive_add_funs = {
        "plane": _bpy.ops.mesh.primitive_plane_add,
        "cube": _bpy.ops.mesh.primitive_cube_add,
        "circle": _bpy.ops.mesh.primitive_circle_add,
        "uv_sphere": _bpy.ops.mesh.primitive_uv_sphere_add,
        "ico_sphere": _bpy.ops.mesh.primitive_ico_sphere_add,
        "cylinder": _bpy.ops.mesh.primitive_cylinder_add,
        "cone": _bpy.ops.mesh.primitive_cone_add,
        "torus": _bpy.ops.mesh.primitive_torus_add,
        "grid": _bpy.ops.mesh.primitive_grid_add,
        "monkey": _bpy.ops.mesh.primitive_monkey_add
    }

    def __init__(self, obj_type, *args, name = None, **kwargs):
        self.__primitive_add_funs[obj_type](*args, **kwargs)
        self.__object = _bpy.context.object
        if not name is None:
            self.__object.name = name

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        raise AttributeError("Direct modification is not allowed.")

    @property
    def name(self):
        return self.__object.name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("`name` must be of type `str`.")
        self.__object.name = new_name


class Plane(BlenderObject):

    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'plane', name = name, **kwargs)


class Cube(BlenderObject):
    
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'cube', name = name, **kwargs)

class Circle(BlenderObject):

    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = "circle", name = name, **kwargs)

class UVSphere(BlenderObject):
    
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'uv_sphere', name = name, **kwargs)

class ICOSphere(BlenderObject):

    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'ico_sphere', name = name, **kwargs)

class Cylinder(BlenderObject):

    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'cylinder', name = name, **kwargs)

class Cone(BlenderObject):
	
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'cone', name = name, **kwargs)

class Torus(BlenderObject):
	
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'torus', name = name, **kwargs)

class Grid(BlenderObject):
	
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'grid', name = name, **kwargs)

class Monkey(BlenderObject):
	
    def __init__(self, *args, name = None, **kwargs):
        return super().__init__(*args, obj_type = 'monkey', name = name, **kwargs)


class Polygon:

    def __init__(self, name, vertices, faces, select = True):

        mesh = _bpy.data.meshes.new(name)
        mesh.from_pydata(vertices, [], faces)
        self.object = _bpy.data.objects.new(name, mesh)

        # Link the object to scene
        scn = _bpy.context.scene
        scn.objects.link(self.object)

        self.name = name
        self.object.select = select
