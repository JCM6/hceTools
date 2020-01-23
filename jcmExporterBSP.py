import bpy, os
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty


#Declare objects

#All
def allObjectsArray():
    objects = bpy.context.scene.objects
    return objects

allSceneObjects = allObjectsArray()

def allObjectNames(sceneObjects):
    for obj in sceneObjects:
        names = str(obj.name)
        print(names)
    return names

allObjectNames(allSceneObjects)

#Nodes
nodeObjects = []
nodeArray = []
nodeTranslation = []
nodeRotation = []
nodeChildIndicies = []
nodeFirstChildIndex = []
nodeNextSiblingIndex = []

#Markers
markerArray = []
markerParentIndex = []
markerTranslation = []
markerRotation = []

#Geometry
geomObjects = []
geomParentIndex = []
geomMaterials = []
geomBoneArray = []
geomObjectHasSkin = []
geomObjectHasTVerts = []
geomMeshFaces = []

#Faces
faceVerts = []
facematID = []
faceSG = []
faceTVerts = []
faceShaderIndex = []

#verts
vertPos = []
vertNode0Index = []
vertNode1Index = []
vertNode1Weight = []
vertNormal = []
tVertPos = []

#Status Variables
exportFailure = False
sceneParent = None
nodeParent = None
numFaces = 0
boneAffectWarning = False
validJMS = False



#Main Panel
class jcmExporterBSP(bpy.types.Panel):
    bl_idname = "OBJECT_PT_JMSExporterBody"
    bl_label = "Dontu .JMS Exporter"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        self.layout.label(text="Dontu's .JMS Exporter.")
        self.layout.label(text='Use this script to export.jms geometry.')
        
bpy.utils.register_class(jcmExporterBSP)



