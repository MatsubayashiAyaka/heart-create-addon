bl_info = {
    "name": "Heart Mesh Generator",
    "author": "ChatGPT",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "Add > Mesh > Heart",
    "description": "Generate a 3D heart-shaped mesh",
    "category": "Add Mesh",
}

import bpy
import bmesh
import math


def create_heart_mesh(context, size, depth, resolution):
    mesh = bpy.data.meshes.new("Heart")
    obj = bpy.data.objects.new("Heart", mesh)
    context.collection.objects.link(obj)
    context.view_layer.objects.active = obj
    obj.select_set(True)

    bm = bmesh.new()

    verts = []

    # ハートの数学式（極座標ベース）
    for i in range(resolution):
        t = math.pi * 2 * i / resolution
        x = size * 16 * math.sin(t)**3
        y = size * (
            13 * math.cos(t)
            - 5 * math.cos(2*t)
            - 2 * math.cos(3*t)
            - math.cos(4*t)
        )
        v = bm.verts.new((x * 0.05, y * 0.05, 0))
        verts.append(v)

    bm.faces.new(verts)
    bm.normal_update()
    bm.to_mesh(mesh)
    bm.free()

    # 厚み付け（Solidify）
    solid = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
    solid.thickness = depth
    solid.offset = 0

    bpy.ops.object.modifier_apply(modifier=solid.name)

    return obj


class MESH_OT_add_heart(bpy.types.Operator):
    """Add a 3D Heart Mesh"""
    bl_idname = "mesh.add_heart"
    bl_label = "Add Heart"
    bl_options = {'REGISTER', 'UNDO'}

    size: bpy.props.FloatProperty(
        name="Size",
        default=1.0,
        min=0.1,
        max=10.0
    )

    depth: bpy.props.FloatProperty(
        name="Depth",
        default=0.3,
        min=0.01,
        max=5.0
    )

    resolution: bpy.props.IntProperty(
        name="Resolution",
        default=64,
        min=16,
        max=256
    )

    def execute(self, context):
        create_heart_mesh(context, self.size, self.depth, self.resolution)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(MESH_OT_add_heart.bl_idname, icon='MESH_CUBE')


def register():
    bpy.utils.register_class(MESH_OT_add_heart)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    bpy.utils.unregister_class(MESH_OT_add_heart)


if __name__ == "__main__":
    register()
