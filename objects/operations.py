# -*- coding: utf-8 -*-

import bpy as _bpy

def select_object(name):
    obj = _bpy.data.objects.get(name, None)
    obj.select = True
    return obj