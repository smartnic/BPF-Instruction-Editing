# python3 bpf_bytecode_to_superopt_pgm
import re
import sys

def read_lines_from_file(file_name):
    file = open(file_name)
    line_arrays = []
    while 1:
        line = file.readline()
        if not line:
            break
        # Remove leading and trailing white space characters
        line = line.strip()
        # Gets a line array from the line by
        # splitting a line at whitespace characters
        line_arrays.append(re.split('\t| |\n', line))
    # print (line_arrays)
    return line_arrays


def hex_str_2_dec_str(hex_str, bits=0):
    if bits > 0 and int(hex_str[0], 16) >= 8:
        sign = 1 << bits
        return str(int(hex_str, 16) - sign)
    return str(int(hex_str, 16))


def process_one_insn(line_array):
    opcode = line_array[1]
    src_reg = line_array[2][0]
    dst_reg = line_array[2][1]
    off = line_array[4] + line_array[3]
    imm = line_array[8] + line_array[7] + line_array[6] + line_array[5]
    str = "{" + \
          hex_str_2_dec_str(opcode) + ", " + \
          hex_str_2_dec_str(dst_reg) + ", " + \
          hex_str_2_dec_str(src_reg) + ", " + \
          hex_str_2_dec_str(off, 2*8) + ", " + \
          hex_str_2_dec_str(imm, 4*8) + "},";
    return str


def bpf_bytecode_2_superopt_pgm(file_in, file_out):
    line_arrays = read_lines_from_file(file_in)
    f = open(file_out, 'w')
    #f.write("{")
    for line_array in line_arrays:
        # If it is not a line representing a bpf instruction then continue
        if len(line_array) < 9:
            continue
        if ":" not in line_array[0]:
            continue
        str = process_one_insn(line_array) + "\n"
        f.write(str)
    #f.write("};")
    f.close()

if __name__ == '__main__':
    #file_in = "xdp.objdump"
    #file_out = "xdp_mod.txt"
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    bpf_bytecode_2_superopt_pgm(file_in, file_out)
