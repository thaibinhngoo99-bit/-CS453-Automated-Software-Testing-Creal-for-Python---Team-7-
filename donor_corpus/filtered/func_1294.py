def compute_overlap(mapping, box1, box2):
    """Computes overlap between the two boxes.

  Overlap is defined as % atoms of box1 in box2. Note that
  overlap is not a symmetric measurement.
  """
    atom1 = set(mapping[box1])
    atom2 = set(mapping[box2])
    return len(atom1.intersection(atom2)) / float(len(atom1))