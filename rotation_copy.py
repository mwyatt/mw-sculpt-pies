def world_to_basis(active, ob, context):
    """put world coords of active as basis coords of ob"""
    local = ob.parent.matrix_world.inverted() @ active.matrix_world
    P = ob.matrix_basis @ ob.matrix_local.inverted()
    mat = P @ local
    return(mat)

def do_rotation_copy(item, mat):
    """Copy rotation to item from matrix mat depending on item.rotation_mode"""
    if item.rotation_mode == 'QUATERNION':
        item.rotation_quaternion = mat.to_3x3().to_quaternion()
    elif item.rotation_mode == 'AXIS_ANGLE':
        rot = mat.to_3x3().to_quaternion().to_axis_angle()    # returns (Vector((x, y, z)), w)
        axis_angle = rot[1], rot[0][0], rot[0][1], rot[0][2]  # convert to w, x, y, z
        item.rotation_axis_angle = axis_angle
    else:
        item.rotation_euler = mat.to_3x3().to_euler(item.rotation_mode)

def copyRotation(ob, active, context):
    if ob.parent:
        mat = world_to_basis(active, ob, context)
        do_rotation_copy(ob, mat.to_3x3())
    else:
        do_rotation_copy(ob, active.matrix_world.to_3x3())
    return('INFO', "Object rotation copied")