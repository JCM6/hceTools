#This script is to be used in the exporting of geometry from Blender into a .jms format.

blInfo = {
    "name":"HCE JMS BSP Exporter",
    "author":"Dontu",
    "version":(1,0,0),
    "location":"File > Export > HCE JMS BSP Exporter",
    "warning":"",
    "wikiUrl":"",
    "trackerUrl":"",
    "category":"Import-Export"
    
}

#imports
import bpy
import os
from bp_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty

class JMSExport(bpy.types.Operator, ExportHelper):
    bl_idname = 'dontuExport.jms'
    bl_label = 'Export'
    __doc__ = 'HCE BSP .JMS Exporter'
    filename_ext = '.jms'
    filter_glab = StringProperty(default = "*.jms", options={'HIDDEN'})
    
    filepath = StringProperty(
        name = "File Path",
        description = "File path used for exporting the JMS file.",
        maxlen = 1024,
        default = ""
    )
    
    option_selection_only = BoolProperty(
        name = "Selection only.",
        description = "Export only the selected scene geometry",
        default = True
    )
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.prop(self, 'option_selection_only')
        
    def serialiseModel():
        frameNode = 1
        outputNodes = ""
                        


#Varialbles

#objects
selectedObjects = bpy.context.selected_objects

for obj in selectedObjects:
    selectedObjectNames = obj.name

#nodes
nodeObjects = []
nodeObjectArray = []
nodeTransaltion = []
nodeChildIndicies = []
nodeFirstChildIndicies = []
nodeNextSiblingIndicies = []

#markers
markerArray = []
markerParentIndex = []
markerTranslation = []
markerRotation = []

#geomerty
geometryObjects = []
geometryParentIndex = []
geometryMaterials = []
geometryBoneArray = []
geometryObjectSkinBool = False
geometryObjectTVertsBool = False
geometryMeshFaces = []
faceVerts = []
faceMatId = []
faceSG = []
faceTVerts = []
faceShaderIndex = []

vertPos = []
vertNode0Index = []
vertNode1Index = []
vertNode1Weight = []
vertNormal = []
tVertPos = []

exportFailed = False
sceneParent = None
nodeParent = None
numFaces = 0
boneAffectWarning = False
validJMS = False

#needs to be implemented.
def getFaceSmoothing():
    return

print(selectedObjects)
