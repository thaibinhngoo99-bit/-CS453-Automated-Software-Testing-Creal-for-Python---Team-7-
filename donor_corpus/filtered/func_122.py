def canonicalize_shape(shape: List[Vector]) -> List[Vector]:
    """Returns a new shape that's canonicalized.

  A canonicalized shape is in sorted order and its first offset is Vector(0, 0).
  This helps with deduplication, since equivalent shapes will be canonicalized
  identically.

  # Arguments
  shape (List[Vector]): A list of offsets defining a shape.

  # Returns
  (List[Vector]): A list of offsets defining the canonicalized version
      of the shape, i.e., in sorted order and with first offset equal
      to Vector(0, 0).
  """
    shape = sorted(shape)
    first_negated = shape[0].negate()
    return [v.translate(first_negated) for v in shape]