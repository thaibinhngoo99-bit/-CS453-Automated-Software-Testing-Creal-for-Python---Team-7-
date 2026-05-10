def extract_active_site(protein_file, ligand_file, cutoff=4):
    """Extracts a box for the active site."""
    protein_coords = rdkit_util.load_molecule(protein_file, add_hydrogens=False)[0]
    ligand_coords = rdkit_util.load_molecule(ligand_file, add_hydrogens=True, calc_charges=True)[0]
    num_ligand_atoms = len(ligand_coords)
    num_protein_atoms = len(protein_coords)
    pocket_inds = []
    pocket_atoms = set([])
    for lig_atom_ind in range(num_ligand_atoms):
        lig_atom = ligand_coords[lig_atom_ind]
        for protein_atom_ind in range(num_protein_atoms):
            protein_atom = protein_coords[protein_atom_ind]
            if np.linalg.norm(lig_atom - protein_atom) < cutoff:
                if protein_atom_ind not in pocket_atoms:
                    pocket_atoms = pocket_atoms.union(set([protein_atom_ind]))
    pocket_atoms = list(pocket_atoms)
    n_pocket_atoms = len(pocket_atoms)
    pocket_coords = np.zeros((n_pocket_atoms, 3))
    for ind, pocket_ind in enumerate(pocket_atoms):
        pocket_coords[ind] = protein_coords[pocket_ind]
    x_min = int(np.floor(np.amin(pocket_coords[:, 0])))
    x_max = int(np.ceil(np.amax(pocket_coords[:, 0])))
    y_min = int(np.floor(np.amin(pocket_coords[:, 1])))
    y_max = int(np.ceil(np.amax(pocket_coords[:, 1])))
    z_min = int(np.floor(np.amin(pocket_coords[:, 2])))
    z_max = int(np.ceil(np.amax(pocket_coords[:, 2])))
    return (((x_min, x_max), (y_min, y_max), (z_min, z_max)), pocket_atoms, pocket_coords)