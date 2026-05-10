def boxes_to_atoms(atom_coords, boxes):
    """Maps each box to a list of atoms in that box.

  TODO(rbharath): This does a num_atoms x num_boxes computations. Is
  there a reasonable heuristic we can use to speed this up?
  """
    mapping = {}
    for box_ind, box in enumerate(boxes):
        box_atoms = []
        (x_min, x_max), (y_min, y_max), (z_min, z_max) = box
        print('Handing box %d/%d' % (box_ind, len(boxes)))
        for atom_ind in range(len(atom_coords)):
            atom = atom_coords[atom_ind]
            x_cont = x_min <= atom[0] and atom[0] <= x_max
            y_cont = y_min <= atom[1] and atom[1] <= y_max
            z_cont = z_min <= atom[2] and atom[2] <= z_max
            if x_cont and y_cont and z_cont:
                box_atoms.append(atom_ind)
        mapping[box] = box_atoms
    return mapping