This repository allows one to add/modify bytecode instructions to test if certain modifications to a verifier rejected bpf bytecode could make it safe.

Command to convert an objdump file to a series of bpf instructions:
python3 bpf_bytcode_to_bpf_insn_prog.py <path to objdump file> <output bpf instructions file>

Command to modify existing lines of this file:
python3 bpf_insns_orig_2_new.py <bpf instructions file> <output updated bpf instructions file> MODIFY <modifications-specification-file>

Command to add lines to this file:
python3 bpf_insns_orig_2_new.py <bpf instructions file> <output updated bpf instructions file> ADD <additions-specification-file>

Format of modifications-specification-file:
Each line of this file specifies the modification of an instruction. 
Format of a line: <line-number>|<updated instruction>
Here the line number is the line that needs to be modified assuming line numbers of a file start from 1.

Format of additions-specification-file:
Each line of this file specifies the addition of an instruction. 
Format of a line: <line-number>|<instruction to add>
Here the line number is the line before which the instruction should be added assuming the line numbers of a file start from 1.

Example:
An example involving modification and addition of instructions has been provided in the 'example' folder. Here 'unboundedLoop.objdump' represents the object dump file of the bpf bytecode which fails the verifier safety check due to the presence of an unbounded loop.

Command for converting obect dump to a sequence of bpf instructions:
python3 bpf_bytcode_to_bpf_insn_prog.py example/unboundedLoop.objdump example/unboundedLoop.txt

Command for adding one branch condition right before the loop termination condition check (the logic of this added instruction is to bound loop variable by some constant):
python3 bpf_insns_orig_2_new.py example/unboundedLoop.txt example/imt.txt ADD example/add-op.txt

Command for updating jump/branch instructions' operands due to addition of instruction above:
python3 bpf_insns_orig_2_new.py example/imt.txt example/boundedLoop.txt MODIFY example/modify-op.txt

Running the final output bpf instruction sequence and thereby confirming it is safe:
Copy the final instruction sequence (boundedLoop.txt) into Input.txt of Independent-bpf-execution github repository. Then follow the instructions in README.md in that repository.






