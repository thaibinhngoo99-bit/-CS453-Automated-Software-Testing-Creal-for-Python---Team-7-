def main():
    platform = nereid.Platform()
    soc = NereidSoC(platform)
    builder = Builder(soc, output_dir='../build/nereid', csr_csv='../build/nereid/csr.csv', compile_gateware=not 'no-compile' in sys.argv[1:])
    vns = builder.build(build_name='nereid')
    soc.generate_software_header('../software/kernel/csr.h')