def add_stage(size=2, transparency=False):
    """
    add PASSIVE rigidbody cube for physic stage or depth background 

    Parameters
    ----------
    size : float, optional
        size of stage. The default is 2.
    transparency : bool, optional
        transparency for rgb but set limit for depth. The default is False.
    """
    import bpycv
    bpy.ops.mesh.primitive_cube_add(size=size, location=(0, 0, -size / 2))
    stage = bpy.context.active_object
    stage.name = 'stage'
    with bpycv.activate_obj(stage):
        bpy.ops.rigidbody.object_add()
        stage.rigid_body.type = 'PASSIVE'
        if transparency:
            stage.rigid_body.use_margin = True
            stage.rigid_body.collision_margin = 0.04
            stage.location.z -= stage.rigid_body.collision_margin
            material = bpy.data.materials.new('transparency_stage_bpycv')
            material.use_nodes = True
            material.node_tree.nodes.clear()
            with bpycv.activate_node_tree(material.node_tree):
                bpycv.Node('ShaderNodeOutputMaterial').Surface = bpycv.Node('ShaderNodeBsdfPrincipled', Alpha=0).BSDF
            stage.data.materials.append(material)
    return stage