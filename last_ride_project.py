import bpy

def executeCommands():
	pass
	bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.object.shade_smooth()
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=6, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=7, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=6, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.object.modifier_add(type='DISPLACE')
	bpy.ops.texture.new()
	bpy.data.textures["Texture"].type = 'VORONOI'
	bpy.data.textures["Texture"].noise_scale = 0.4
	bpy.data.textures["Texture"].noise_scale = 1.15
	bpy.ops.object.particle_system_add()
	bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.transform.translate(value=(-0.0215909, -0.0955665, 0.00125983), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(1.27671, 7.758, 0.724703), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings"].instance_object = None
	bpy.data.particles["ParticleSettings"].particle_size = 0.03
	bpy.data.particles["ParticleSettings"].count = 20000
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.object.material_slot_add()
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.208234, 0.0349931, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.208234, 0.0349931, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[1].default_value = 10
	bpy.context.object.active_material.use_nodes = False
	bpy.context.object.active_material.use_nodes = True
	bpy.context.object.active_material.use_nodes = False
	bpy.context.object.active_material.use_nodes = True
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.outliner.item_rename()
	bpy.context.object.active_material_index = 0
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.161208, 0.0441099, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.308764, 0.0356621, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.308764, 0.0356621, 1)
	bpy.context.scene.eevee.use_bloom = True
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.865206, 0.198863, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.871869, 0.210286, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.871869, 0.210286, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[1].default_value = 10
	bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.0508761, 0.0508761, 0.0508761, 1)
	bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.0508761, 0.0508761, 0.0508761, 1)
	bpy.data.particles["ParticleSettings"].particle_size = 0.02
	bpy.ops.ptcache.bake(bake=True)
	bpy.ops.transform.translate(value=(-2.44571, 3.10202, 3.534), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, cursor_transform=True, release_confirm=True)
	bpy.ops.ptcache.bake(bake=True)
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0862579, 0.193983, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.131594, 0.134626, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.131594, 0.134626, 1)
	bpy.ops.ptcache.free_bake()
	bpy.data.particles["ParticleSettings"].tangent_factor = 3
	bpy.data.particles["ParticleSettings"].tangent_factor = 0
	bpy.data.particles["ParticleSettings"].tangent_phase = 1
	bpy.data.particles["ParticleSettings"].tangent_phase = 0
	bpy.data.particles["ParticleSettings"].object_align_factor[1] = 20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 5
	bpy.data.particles["ParticleSettings"].lifetime = 25
	bpy.data.particles["ParticleSettings"].use_rotations = True
	bpy.data.particles["ParticleSettings"].use_rotations = False
	bpy.data.particles["ParticleSettings"].physics_type = 'NO'
	bpy.data.particles["ParticleSettings"].physics_type = 'NEWTON'
	bpy.data.particles["ParticleSettings"].physics_type = 'KEYED'
	bpy.data.particles["ParticleSettings"].physics_type = 'BOIDS'
	bpy.data.particles["ParticleSettings"].physics_type = 'FLUID'
	bpy.data.particles["ParticleSettings"].physics_type = 'NEWTON'
	bpy.data.particles["ParticleSettings"].mass = 0.5
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = True
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = False
	bpy.data.particles["ParticleSettings"].mass = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.ops.transform.translate(value=(0.825043, -11.0967, -4.23457), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0.797877, -7.92323, -0.444953), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.particles["ParticleSettings"].tangent_factor = -0.5
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = True
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = False
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = True
	bpy.data.particles["ParticleSettings"].use_multiply_size_mass = False
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.object.constraint_add(type='FOLLOW_TRACK')
	bpy.ops.transform.translate(value=(-0.486234, 4.42046, -0.202444), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, cursor_transform=True, release_confirm=True)
	bpy.ops.curve.primitive_nurbs_path_add(radius=1, enter_editmode=False, align='WORLD', location=(-1.47177, 11.0082, 1.08735), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.context.scene.cursor.location[0] = 0
	bpy.context.scene.cursor.location[1] = 0
	bpy.context.scene.cursor.location[2] = 0
	bpy.context.scene.cursor.rotation_euler[0] = 0
	bpy.context.scene.cursor.rotation_euler[1] = 0
	bpy.context.scene.cursor.rotation_euler[2] = 0
	bpy.context.scene.cursor.rotation_euler[1] = 0
	bpy.context.scene.cursor.rotation_euler[2] = 1.5708
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.context.object.location[0] = 0
	bpy.context.object.location[1] = 0
	bpy.context.object.location[2] = 0
	bpy.context.scene.cursor.rotation_euler[2] = 0
	bpy.ops.transform.rotate(value=2.41296, orient_axis='Z', orient_type='VIEW', orient_matrix=((-0.689996, -0.723718, -0.011707), (0.259815, -0.26274, 0.929228), (-0.675575, 0.638122, 0.369322)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.context.object.constraints["Follow Track"].name = "Follow Track"
	bpy.ops.constraint.delete(constraint="Follow Track", owner='OBJECT')
	bpy.ops.object.constraint_add(type='FOLLOW_PATH')
	bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')
	bpy.context.object.constraints["Follow Path"].target = None
	bpy.context.object.constraints["Follow Path"].target = None
	bpy.context.object.constraints["Follow Path"].target = None
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.transform.translate(value=(0.47511, 0.676678, 1.26183), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.object.select_all(action='SELECT')
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.particles["ParticleSettings"].tangent_factor = -5
	bpy.data.particles["ParticleSettings"].tangent_factor = 5
	bpy.data.particles["ParticleSettings"].object_align_factor[1] = 0
	bpy.data.particles["ParticleSettings"].object_align_factor[0] = 20
	bpy.data.particles["ParticleSettings"].object_align_factor[0] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 10
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -10
	bpy.data.particles["ParticleSettings"].tangent_factor = 0
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.object.editmode_toggle()
	bpy.ops.transform.translate(value=(0.252661, 0.567877, 1.82439), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0, 4.60837, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0.18774, 4.73076, 0.655885), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0, 0, 1.89), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.curve.select_all(action='SELECT')
	bpy.ops.transform.translate(value=(0.162202, 1.78419, 1.23854), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(1.84441, 4.52688, 1.86708), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(-1.52705, -3.62127, 0.765642), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0.569215, -0.650057, 2.08897), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(-0.679877, -2.55795, 1.46364), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.transform.translate(value=(0.732997, 23.9213, 7.00301), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(8.05571, 11.1458, 6.30981), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(4.1246, 1.47322, 8.34572), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(-0.380633, 3.07434, 7.4279), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(0.0563934, 5.51539, 10.5718), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.object.constraint_add(type='FOLLOW_PATH')
	bpy.ops.constraint.delete(constraint="Follow Path", owner='OBJECT')
	bpy.ops.transform.translate(value=(-1.97025, -0.80498, -2.84389), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, cursor_transform=True, release_confirm=True)
	bpy.ops.transform.translate(value=(2.0054, -0.621194, -1.13255), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, cursor_transform=True, release_confirm=True)
	bpy.context.scene.frame_current = 131
	bpy.context.scene.frame_current = 102
	bpy.context.scene.frame_end = 100
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_rename()
	bpy.context.scene.frame_end = 250
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.context.object.data.path_duration = 250
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(7.58988, -20.2141, 1.54235), rotation=(1.4159, 0.0100775, -1.34413), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	bpy.context.object.location[0] = -100
	bpy.context.object.location[1] = 0
	bpy.context.object.location[2] = 0
	bpy.context.object.location[0] = -20
	bpy.ops.transform.translate(value=(-1.12006, 22.1772, 7.63792), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(-20.1461, -6.17632, 2.1235), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.view3d.object_as_camera()
	bpy.ops.view3d.object_as_camera()
	bpy.ops.view3d.object_as_camera()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	bpy.ops.transform.rotate(value=0.0393691, orient_axis='Z', orient_type='VIEW', orient_matrix=((0.224716, -0.974372, -0.0100773), (0.152569, 0.0249684, 0.987977), (-0.962406, -0.223552, 0.15427)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(6.16757, 1.17106, -1.19209e-07), orient_type='VIEW', orient_matrix=((0.218537, -0.9746, -0.0489552), (0.161295, -0.0134012, 0.986815), (-0.962406, -0.223552, 0.15427)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	bpy.ops.transform.translate(value=(6.92831, 0.600877, -1.48229e-05), orient_type='VIEW', orient_matrix=((0.218537, -0.9746, -0.0489552), (0.161295, -0.0134012, 0.986815), (-0.962406, -0.223552, 0.15427)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.particles["ParticleSettings"].frame_end = 250
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.ops.transform.translate(value=(-60.0804, -11.1408, -7.92023), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0706565, 0.0220176, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0706565, 0.0220176, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.152673, 0.03713, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.152673, 0.03713, 1)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.970182, 0.173631, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.970182, 0.173631, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[1].default_value = 5
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle.001']
	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-3.24527, 5.75146, -3.21547), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle.001']
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle']
	bpy.ops.outliner.item_rename()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle2']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle2']
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0744377, 0.0367848, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0744377, 0.0367848, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.object.particle_system_add()
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.context.object.particle_systems["TailFlame"].name = "TailFlame"
	bpy.context.object.particle_systems["FrontFlame"].name = "FrontFlame"
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.context.object.particle_systems["FrontFlame"].parent = None
	bpy.data.particles["ParticleSettings.001"].particle_size = 0.01
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.context.object.particle_systems["TailFlame"].name = "TailFlame"
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle2']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle2']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.238332, 0.0829407, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.238332, 0.0829407, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle2']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle2']
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.238929, 0.126561, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.238929, 0.126561, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle2']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle2']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle2']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle2']
	bpy.ops.transform.translate(value=(-4.34337, 8.83473, -2.12731), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.232654, 0.105237, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.232654, 0.105237, 1)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-9.29099, 20.451, -6.01337), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.106712, 0.0709658, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.106712, 0.0709658, 1)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-11.6609, 27.0016, -1.93893), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0480047, 0.0685145, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0480047, 0.0685145, 1)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-6.85847, 20.4598, -4.7285), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.255803, 0.0923772, 1)
	bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.255803, 0.0923772, 1)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.context.object.active_material.name = "Material2"
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.436723, 0.106887, 1)
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.436723, 0.106887, 1)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.context.object.active_material.name = "Material"
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.context.object.active_material.name = "Material"
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.context.object.active_material_index = 0
	bpy.context.object.active_material.name = "Material2"
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.127486, 0.0738354, 1)
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.127486, 0.0738354, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.context.object.particle_systems["FrontFlame"].parent = None
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.particles["ParticleSettings.001"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings.001"].instance_object = None
	bpy.data.particles["ParticleSettings.001"].lifetime = 5
	bpy.data.particles["ParticleSettings.001"].count = 20000
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0570451, 0.044941, 1)
	bpy.data.materials["Material2"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0570451, 0.044941, 1)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.particles["ParticleSettings.001"].particle_size = 0.04
	bpy.data.particles["ParticleSettings.001"].frame_end = 250
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.particles["ParticleSettings"].particle_size = 0.03
	bpy.data.particles["ParticleSettings"].particle_size = 0.05
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.particles["ParticleSettings.001"].normal_factor = 5
	bpy.data.particles["ParticleSettings.001"].normal_factor = -5
	bpy.data.particles["ParticleSettings.001"].normal_factor = 10
	bpy.data.particles["ParticleSettings.001"].normal_factor = 5
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 5
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 0
	bpy.data.particles["ParticleSettings.001"].normal_factor = 1
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 3
	bpy.data.particles["ParticleSettings.001"].object_align_factor[1] = 0
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 5
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 20
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 10
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 5
	bpy.data.particles["ParticleSettings.001"].lifetime = 10
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.27774, 0.0937846, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.381958, 0.100642, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0196885, 0.04105, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.336522, 0.0761968, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.319891, 0.10477, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.198917, 0.0509588, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.198917, 0.0509588, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[1].default_value = 1
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.33522, 0.050262, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.33522, 0.050262, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[1].default_value = 3
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.167518, 0.0344974, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.167518, 0.0344974, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -10
	bpy.ops.anim.keyframe_insert_by_name(type="Location")
	bpy.ops.anim.keyframe_insert_by_name(type="Location")
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.ops.action.interpolation_type(type='CONSTANT')
	bpy.ops.anim.keyframe_insert_by_name(type="Location")
	bpy.ops.action.delete(confirm=False)
	bpy.ops.action.delete(confirm=False)
	bpy.ops.ptcache.bake(bake=True)
	bpy.data.objects["Meteor"].(null) = 1
	bpy.ops.ptcache.bake(bake=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.images["Render Result"].name = "Render Result"
	bpy.data.images["Render Result"].name = "Render Result"
	bpy.ops.render.play_rendered_anim()
	bpy.data.objects["Meteor"].(null) = 1
	bpy.ops.ptcache.free_bake()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.object.editmode_toggle()
	bpy.ops.transform.translate(value=(1.56841, -7.06939, -0.459681), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(1.26431, -3.55504, 2.73576), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 0
	bpy.ops.ptcache.free_bake()
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -40
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -19.9824
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -40
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -40
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -40
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = -20
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor_particle1.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor_particle1.001']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.particles["ParticleSettings.001"].normal_factor = 2
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 0
	bpy.ops.ptcache.bake(bake=True)
	bpy.data.objects["Meteor"].(null) = 1
	bpy.ops.ptcache.bake(bake=True)
	bpy.ops.render.play_rendered_anim()
	bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.context.object.active_material.use_nodes = False
	bpy.context.object.active_material.use_nodes = True
	bpy.ops.texture.new()
	bpy.data.textures["MeteorTexture"].name = "MeteorTexture"
	bpy.data.textures["MeteorTexture"].type = 'VORONOI'
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.textures["MeteorTexture"].minkovsky_exponent = 2.5
	bpy.data.textures["MeteorTexture"].noise_intensity = 3.8
	bpy.data.textures["MeteorTexture"].noise_intensity = 2
	bpy.data.textures["MeteorTexture"].nabla = 0.1
	bpy.ops.transform.translate(value=(0.0280628, 0.400377, 0.273264), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, cursor_transform=True, release_confirm=True)
	bpy.ops.transform.translate(value=(-0.457868, -0.467903, 0.461345), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(3.48537, -2.7766, 1.52164), rotation=(1.47697, -0.0675133, 0.948828), scale=(0.486931, 0.579721, 3.62748))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.context.scene.eevee.use_motion_blur = True
	bpy.context.scene.eevee.use_bloom = True
	bpy.ops.object.modifier_add(type='MESH_DEFORM')
	bpy.context.object.modifiers["MeshDeform"].object = None
	bpy.context.object.modifiers["MeshDeform"].object = None
	bpy.context.object.modifiers["MeshDeform"].object = None
	bpy.ops.object.modifier_add(type='REMESH')
	bpy.ops.object.modifier_remove(modifier="MeshDeform")
	bpy.context.object.modifiers["Remesh"].name = "Remesh"
	bpy.context.object.modifiers["Remesh"].voxel_size = 0.139097
	bpy.ops.object.modifier_add(type='DISPLACE')
	bpy.context.object.modifiers["Displace"].strength = 2.7
	bpy.context.object.modifiers["Displace"].mid_level = 0.626866
	bpy.ops.object.modifier_remove(modifier="Displace")
	bpy.context.object.modifiers["Remesh"].adaptivity = 0.01
	bpy.context.object.modifiers["Remesh"].voxel_size = 0.132313
	bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0.723725, -0.311539, 0.366194), rotation=(1.10871, 0.013265, 1.14827), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.object.modifier_remove(modifier="Remesh")
	bpy.ops.object.modifier_add(type='REMESH')
	bpy.context.object.modifiers["Remesh"].voxel_size = 0.42207
	bpy.ops.object.modifier_set_active(modifier="Remesh")
	bpy.context.object.modifiers["Remesh"].adaptivity = 0.38
	bpy.context.object.modifiers["Remesh"].mode = 'BLOCKS'
	bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
	bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
	bpy.context.object.modifiers["Remesh"].mode = 'SHARP'
	bpy.ops.object.modifier_remove(modifier="Remesh")
	bpy.ops.object.modifier_add(type='CAST')
	bpy.context.object.modifiers["Cast"].factor = -3.23134
	bpy.context.object.modifiers["Cast"].radius = 0.17
	bpy.ops.object.modifier_remove(modifier="Cast")
	bpy.ops.object.modifier_add(type='DISPLACE')
	bpy.context.object.modifiers["Displace"].strength = 1.9
	bpy.ops.object.modifier_remove(modifier="Displace")
	bpy.ops.object.modifier_add(type='LATTICE')
	bpy.ops.object.modifier_remove(modifier="Lattice")
	bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
	bpy.context.object.modifiers["SimpleDeform"].angle = 0.47822
	bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
	bpy.context.object.modifiers["SimpleDeform"].angle = 2.15374
	bpy.ops.object.modifier_remove(modifier="SimpleDeform")
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.ops.object.modifier_remove(modifier="Boolean")
	bpy.ops.object.modifier_add(type='EXPLODE')
	bpy.ops.object.modifier_add(type='LAPLACIANDEFORM')
	bpy.ops.object.modifier_remove(modifier="Explode")
	bpy.context.object.modifiers["LaplacianDeform"].iterations = 1
	bpy.ops.object.modifier_remove(modifier="LaplacianDeform")
	bpy.ops.object.modifier_add(type='DECIMATE')
	bpy.context.object.modifiers["Decimate"].symmetry_axis = 'Y'
	bpy.context.object.modifiers["Decimate"].symmetry_axis = 'X'
	bpy.context.object.modifiers["Decimate"].ratio = 1
	bpy.ops.object.modifier_remove(modifier="Decimate")
	bpy.ops.object.modifier_add(type='HOOK')
	bpy.ops.object.modifier_remove(modifier="Hook")
	bpy.ops.object.modifier_add(type='SURFACE_DEFORM')
	bpy.context.object.modifiers["SurfaceDeform"].falloff = 2
	bpy.context.object.modifiers["SurfaceDeform"].strength = -4.4
	bpy.ops.object.modifier_remove(modifier="SurfaceDeform")
	bpy.ops.object.modifier_add(type='WARP')
	bpy.context.object.modifiers["Warp"].strength = -9.7
	bpy.ops.object.modifier_remove(modifier="Warp")
	bpy.ops.object.modifier_add(type='NORMAL_EDIT')
	bpy.ops.object.modifier_remove(modifier="NormalEdit")
	bpy.ops.object.particle_system_add()
	bpy.data.objects["Icosphere"].(null) = 0
	bpy.context.object.particle_systems["TailParticles"].name = "TailParticles"
	bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0.723725, -0.311539, 0.366194), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.transform.translate(value=(5.02683, 6.75302, -3.7548), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.outliner.item_rename()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.particles["ParticleSettings"].count = 20000
	bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings"].instance_object = None
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesMesh']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesMesh']
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesOject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesOject']
	bpy.ops.outliner.item_rename()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.particles["ParticleSettings"].size_random = 0
	bpy.data.particles["ParticleSettings"].particle_size = 0.02
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesObject']
	bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0.723725, -0.311539, 0.366194), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.transform.translate(value=(4.70689, 4.19928, -5.23888), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.outliner.item_rename()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesObject']
	bpy.ops.outliner.item_rename()
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.context.object.active_material_index = 0
	bpy.context.object.active_material.name = "TailParticleMaterial"
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['FrontParticleObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['FrontParticleObject']
	bpy.ops.material.new()
	bpy.context.object.active_material = bpy.data.materials[-1]
	bpy.context.object.active_material_index = 0
	bpy.context.object.active_material.name = "FrontParticleMaterial"
	bpy.data.materials["FrontParticleMaterial"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.123293, 0.0795421, 1)
	bpy.data.materials["FrontParticleMaterial"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.123293, 0.0795421, 1)
	bpy.data.materials["FrontParticleMaterial"].node_tree.nodes["Emission"].inputs[1].default_value = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesObject']
	bpy.data.materials["TailParticleMaterial"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.521756, 0.0817317, 1)
	bpy.data.materials["TailParticleMaterial"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.521756, 0.0817317, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 2
	bpy.data.particles["ParticleSettings"].object_align_factor[0] = -20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 5
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 20
	bpy.data.particles["ParticleSettings"].object_align_factor[2] = 15
	bpy.data.particles["ParticleSettings"].brownian_factor = 0
	bpy.data.particles["ParticleSettings"].brownian_factor = 0.58
	bpy.data.particles["ParticleSettings"].particle_size = 0.05
	bpy.data.particles["ParticleSettings"].particle_size = 0.03
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesObject']
	bpy.data.materials["TailParticleMaterial"].node_tree.nodes["Emission"].inputs[1].default_value = 1
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['FrontParticleObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['FrontParticleObject']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['TailPraticlesObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['TailPraticlesObject']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['FrontParticleObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['FrontParticleObject']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.data.particles["ParticleSettings"].frame_end = 250
	bpy.data.particles["ParticleSettings"].normal_factor = 2
	bpy.data.particles["ParticleSettings"].normal_factor = 0.1
	bpy.data.particles["ParticleSettings"].tangent_factor = 3
	bpy.data.particles["ParticleSettings"].tangent_factor = -3
	bpy.data.particles["ParticleSettings"].tangent_factor = 0
	bpy.data.particles["ParticleSettings"].tangent_factor = -0.5
	bpy.data.particles["ParticleSettings"].object_factor = 0
	bpy.data.particles["ParticleSettings"].factor_random = 0
	bpy.data.particles["ParticleSettings"].factor_random = 5
	bpy.ops.object.particle_system_add()
	bpy.data.objects["Icosphere"].(null) = 1
	bpy.context.object.particle_systems["TailParticles2"].name = "TailParticles2"
	bpy.data.particles["ParticleSettings.001"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings.001"].instance_object = None
	bpy.data.particles["ParticleSettings.001"].particle_size = 0.03
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = 20
	bpy.data.particles["ParticleSettings.001"].object_align_factor[2] = -6
	bpy.data.particles["ParticleSettings.001"].object_align_factor[0] = -20
	bpy.data.particles["ParticleSettings.001"].object_align_factor[2] = 5
	bpy.context.object.particle_systems["TailParticles2"].seed = 0
	bpy.data.particles["ParticleSettings.001"].count = 20000
	bpy.data.particles["ParticleSettings.001"].factor_random = 5
	bpy.data.objects["Icosphere"].(null) = 0
	bpy.data.objects["Icosphere"].(null) = 1
	bpy.data.particles["ParticleSettings.001"].object_align_factor[2] = 15
	bpy.ops.object.particle_system_add()
	bpy.data.objects["Icosphere"].(null) = 2
	bpy.context.object.particle_systems["FrontParticles"].name = "FrontParticles"
	bpy.data.particles["ParticleSettings.002"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings.002"].instance_object = None
	bpy.data.particles["ParticleSettings.002"].instance_object = None
	bpy.data.particles["ParticleSettings.002"].instance_object = None
	bpy.data.particles["ParticleSettings.002"].lifetime = 5
	bpy.data.particles["ParticleSettings.002"].count = 10000
	bpy.ops.curve.primitive_nurbs_path_add(radius=1, enter_editmode=False, align='WORLD', location=(0.723725, -0.311539, 0.366194), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.object.editmode_toggle()
	bpy.ops.transform.translate(value=(1.66046, 1.75608, 0.865916), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(-8.68764, -3.12584, 2.59544), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.transform.translate(value=(4.96098, 0.764297, -1.04433), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.object.editmode_toggle()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.object.constraint_add(type='FOLLOW_PATH')
	bpy.context.object.constraints["Follow Path"].target = None
	bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Icosphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Icosphere']
	bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_Z'
	bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_X'
	bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_Y'
	bpy.context.object.constraints["Follow Path"].use_curve_follow = True
	bpy.context.object.constraints["Follow Path"].use_curve_follow = False
	bpy.context.object.constraints["Follow Path"].influence = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['FrontParticleObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['FrontParticleObject']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.context.object.constraints["Follow Path"].offset = 0
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	bpy.ops.outliner.item_rename()
	bpy.ops.object.editmode_toggle()
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.objects["Meteor"].(null) = 'KEYS_SELECTED'
	bpy.data.objects["Meteor"].(null) = 0
	bpy.data.objects["Meteor"].(null) = 'KEYS_ALL'
	bpy.data.objects["Meteor"].(null) = 'SCENE'
	bpy.data.objects["Meteor"].(null) = 1
	bpy.data.objects["Meteor"].(null) = 250
	bpy.ops.object.forcefield_toggle()
	bpy.context.object.constraints["Follow Path"].name = "Follow Path"
	bpy.context.object.constraints["Follow Path"].influence = 1
	bpy.context.object.constraints["Follow Path"].influence = 1
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.context.object.data.eval_time = 250
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.context.object.data.path_duration = 250
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.data.particles["ParticleSettings.002"].object_align_factor[0] = 3
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.object.modifier_add(type='DISPLACE')
	bpy.ops.texture.new()
	bpy.context.object.modifiers["Displace"].strength = 2
	bpy.data.textures["Texture"].name = "Texture"
	bpy.ops.object.modifier_set_active(modifier="Displace")
	bpy.context.object.modifiers["Displace"].strength = 2
	bpy.context.object.modifiers["Displace"].strength = -0.5
	bpy.context.object.modifiers["Displace"].texture_coords = 'OBJECT'
	bpy.context.object.modifiers["Displace"].strength = 1.6
	bpy.context.object.modifiers["Displace"].direction = 'Y'
	bpy.context.object.modifiers["Displace"].strength = 0.4
	bpy.context.object.modifiers["Displace"].direction = 'NORMAL'
	bpy.ops.object.modifier_set_active(modifier="Displace")
	bpy.data.textures["Texture"].name = "Texture"
	bpy.context.object.modifiers["Displace"].texture_coords = 'GLOBAL'
	bpy.context.object.modifiers["Displace"].strength = 3.6
	bpy.context.object.modifiers["Displace"].name = "Displace"
	bpy.ops.object.modifier_set_active(modifier="Displace")
	bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
	bpy.context.object.modifiers["Displace"].texture_coords = 'GLOBAL'
	bpy.data.textures["Texture"].name = "Texture"
	bpy.context.object.modifiers["Displace"].texture_coords = 'LOCAL'
	bpy.context.object.modifiers["Displace"].strength = 3.5
	bpy.context.object.modifiers["Displace"].mid_level = 0.425373
	bpy.ops.object.modifier_set_active(modifier="Displace")
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.278995, 0.26519, 1)
	bpy.data.materials["Material.001"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.278995, 0.26519, 1)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['FrontParticleObject']]
	bpy.context.view_layer.objects.active = bpy.data.objects['FrontParticleObject']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.ops.object.modifier_remove(modifier="Displace")
	bpy.data.particles["ParticleSettings.002"].lifetime_random = 0
	bpy.data.particles["ParticleSettings.002"].object_factor = 2
	bpy.data.particles["ParticleSettings.002"].frame_end = 250
	bpy.data.particles["ParticleSettings.002"].drag_factor = 1
	bpy.data.particles["ParticleSettings.002"].object_factor = -2
	bpy.data.particles["ParticleSettings.002"].drag_factor = 1
	bpy.data.particles["ParticleSettings.002"].brownian_factor = 10
	bpy.data.particles["ParticleSettings.002"].brownian_factor = 0
	bpy.data.particles["ParticleSettings.002"].drag_factor = 0
	bpy.data.particles["ParticleSettings.002"].integrator = 'EULER'
	bpy.data.particles["ParticleSettings.002"].integrator = 'MIDPOINT'
	bpy.data.particles["ParticleSettings.002"].use_size_deflect = True
	bpy.data.particles["ParticleSettings.002"].use_size_deflect = False
	bpy.data.particles["ParticleSettings.002"].timestep = 0.01
	bpy.data.particles["ParticleSettings.002"].integrator = 'EULER'
	bpy.data.particles["ParticleSettings.002"].subframes = 0
	bpy.data.particles["ParticleSettings.002"].timestep = 0.01
	bpy.data.particles["ParticleSettings.002"].damping = 0
	bpy.data.particles["ParticleSettings.002"].drag_factor = 0
	bpy.data.particles["ParticleSettings.002"].brownian_factor = 0
	bpy.data.objects["Meteor"].(null) = 2
	bpy.data.particles["ParticleSettings.002"].type = 'HAIR'
	bpy.data.particles["ParticleSettings.002"].type = 'EMITTER'
	bpy.data.particles["ParticleSettings.002"].userjit = 39
	bpy.data.particles["ParticleSettings.002"].userjit = 0
	bpy.data.particles["ParticleSettings.002"].jitter_factor = 1.66667
	bpy.data.particles["ParticleSettings.002"].jitter_factor = 1
	bpy.data.particles["ParticleSettings.002"].emit_from = 'FACE'
	bpy.data.particles["ParticleSettings.002"].use_modifier_stack = True
	bpy.data.particles["ParticleSettings.002"].use_modifier_stack = False
	bpy.data.particles["ParticleSettings.002"].emit_from = 'VERT'
	bpy.data.particles["ParticleSettings.002"].emit_from = 'FACE'
	bpy.data.particles["ParticleSettings.002"].emit_from = 'VOLUME'
	bpy.data.particles["ParticleSettings.002"].emit_from = 'VERT'
	bpy.data.particles["ParticleSettings.002"].emit_from = 'FACE'
	bpy.data.particles["ParticleSettings.002"].distribution = 'GRID'
	bpy.data.particles["ParticleSettings.002"].distribution = 'JIT'
	bpy.data.particles["ParticleSettings.002"].use_emit_random = False
	bpy.data.particles["ParticleSettings.002"].use_even_distribution = False
	bpy.data.particles["ParticleSettings.002"].use_emit_random = True
	bpy.data.particles["ParticleSettings.002"].use_even_distribution = True
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['NurbsPath']]
	bpy.context.view_layer.objects.active = bpy.data.objects['NurbsPath']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Meteor']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Meteor']
	bpy.context.object.constraints["Follow Path"].offset = 0.7
	bpy.context.object.constraints["Follow Path"].offset = 5.4
