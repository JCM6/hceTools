#voxel maker blender tutorial

#first get the info


bl_info = {
    "name":"voxObjectName",
    "author":"dontu",
    "version":{1, 0},
    "blender": {2, 80, 0},
    "location":"View30 > Add > Mesh > New Object",
    "warning":"",
    "wiki_url":"",
    "category":"Add Mesh"
}

import bpy
from bpy.types import Operator (
    AddonPreferences,
    Operator,
)
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


class OBJECT_OT_voxObjectName(Operator)
