def wrap_compute_bitserial_dense(topi_compute):
    """wrap bitserial_dense topi compute"""

    def compute_bitserial_dense(attrs, inputs, out_type):
        """Compute definition of bitserial dense"""
        data_bits = attrs.data_bits
        weight_bits = attrs.weight_bits
        pack_dtype = attrs.pack_dtype
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype == '' else out_dtype
        unipolar = attrs.unipolar
        return [topi_compute(inputs[0], inputs[1], data_bits, weight_bits, pack_dtype, out_dtype, unipolar)]
    return compute_bitserial_dense