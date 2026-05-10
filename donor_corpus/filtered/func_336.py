def _is_int8_hw_support(data_dtype, kernel_dtype):
    """
    Checks to ensure that we can use Intel DLBoost instructions
    1) The datatypes are correct.
    2) LLVM version has support for the instructions.
    3) Target is skylake and above.
    """
    is_dtype_support = data_dtype == 'uint8' and kernel_dtype == 'int8'
    llvm_intrin_fast_int8 = 'llvm.x86.avx512.pmaddubs.w.512'
    llvm_id = tvm.codegen.llvm_lookup_intrinsic_id(llvm_intrin_fast_int8)
    is_llvm_support = llvm_id != 0
    target = tvm.target.current_target()
    is_target_support = False
    for opt in target.options:
        if opt == '-mcpu=skylake-avx512':
            is_target_support = True
    return is_dtype_support and is_llvm_support and is_target_support