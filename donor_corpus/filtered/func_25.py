def TensorRTCompileSpec(compile_spec: Dict[str, Any]):
    """
    Utility to create a formated spec dictionary for using the PyTorch TensorRT backend

    Args:
        compile_spec (dict): Compilation settings including operating precision, target device, etc.
            One key is required which is ``input_shapes``, describing the input sizes or ranges for inputs
            to the graph. All other keys are optional. Entries for each method to be compiled.

            .. code-block:: py

                CompileSpec = {
                    "forward" : trtorch.TensorRTCompileSpec({
                        "input_shapes": [
                            (1, 3, 224, 224), # Static input shape for input #1
                            {
                                "min": (1, 3, 224, 224),
                                "opt": (1, 3, 512, 512),
                                "max": (1, 3, 1024, 1024)
                            } # Dynamic input shape for input #2
                        ],
                        "op_precision": torch.half, # Operating precision set to FP16
                        "refit": False, # enable refit
                        "debug": False, # enable debuggable engine
                        "strict_types": False, # kernels should strictly run in operating precision
                        "allow_gpu_fallback": True, # (DLA only) Allow layers unsupported on DLA to run on GPU
                        "device": torch.device("cuda"), # Type of device to run engine on (for DLA use trtorch.DeviceType.DLA)
                        "capability": trtorch.EngineCapability.DEFAULT, # Restrict kernel selection to safe gpu kernels or safe dla kernels
                        "num_min_timing_iters": 2, # Number of minimization timing iterations used to select kernels
                        "num_avg_timing_iters": 1, # Number of averaging timing iterations used to select kernels
                        "workspace_size": 0, # Maximum size of workspace given to TensorRT
                        "max_batch_size": 0, # Maximum batch size (must be >= 1 to be set, 0 means not set)
                    })
                }

            Input Sizes can be specified as torch sizes, tuples or lists. Op precisions can be specified using
            torch datatypes or trtorch datatypes and you can use either torch devices or the trtorch device type enum
            to select device type.

    Returns:
        torch.classes.tensorrt.CompileSpec: List of methods and formated spec objects to be provided to ``torch._C._jit_to_tensorrt``
    """
    parsed_spec = _parse_compile_spec(compile_spec)
    backend_spec = torch.classes.tensorrt.CompileSpec()
    for i in parsed_spec.input_ranges:
        ir = torch.classes.tensorrt.InputRange()
        ir.set_min(i.min)
        ir.set_opt(i.opt)
        ir.set_max(i.max)
        backend_spec.append_input_range(ir)
    backend_spec.set_op_precision(int(parsed_spec.op_precision))
    backend_spec.set_refit(parsed_spec.refit)
    backend_spec.set_debug(parsed_spec.debug)
    backend_spec.set_refit(parsed_spec.refit)
    backend_spec.set_strict_types(parsed_spec.strict_types)
    backend_spec.set_allow_gpu_fallback(parsed_spec.allow_gpu_fallback)
    backend_spec.set_device(int(parsed_spec.device))
    backend_spec.set_capability(int(parsed_spec.capability))
    backend_spec.set_num_min_timing_iters(parsed_spec.num_min_timing_iters)
    backend_spec.set_num_avg_timing_iters(parsed_spec.num_avg_timing_iters)
    backend_spec.set_workspace_size(parsed_spec.workspace_size)
    backend_spec.set_max_batch_size(parsed_spec.max_batch_size)
    return backend_spec