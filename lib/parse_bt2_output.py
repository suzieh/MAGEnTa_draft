# usr/bin/python3
# usage: parse_bt2_output.py [donor_alignment] [pre_alignment] [post_sample_fastq] [out_file]

import os
import sys

# Parse arguments
donor_file = sys.argv[1]
pre_file = sys.argv[2]
post_fastq = sys.argv[3]
out_file = sys.argv[4]

# Load Donor and Pre Tables - get unique values
def get_unique_ids(filename):
    unique_values = set()
    with open(filename, 'r') as file:
        for line in file:
            columns = line.strip().split()  # Assumes whitespace delimiter
            if columns:  # Ensure the line is not empty
                unique_values.add(columns[0])
    return unique_values
d_reads = get_unique_ids(donor_file)
p_reads = get_unique_ids(pre_file)

# Get total counts from the post sample file
total_n = sum(1 for _ in open(post_fastq)) // 4

# Set intersection to get overlap between donor and pre alignment files
intersect = d_reads.intersection(p_reads)

# Unique reads and unknowns
d_uniq = len(d_reads) - len(intersect)  # uniquely donor counts
p_uniq = len(p_reads) - len(intersect)  # uniquely pre counts
ambig = len(intersect)                  # ambiguous - matching both donor and pre
unknown = total_n - len(intersect) - d_uniq - p_uniq  # unknown / unmapped

# Assign ambiguous reads using Bayesian estiamtion
prob_d_p = sum_pre_align / (0.82*8750000) # probability of p given d - get from pre alignment with 0.0 pre simulation
prob_p_d = sum_donor_alignment_' + identity + '.txt')) / (0.82*8750000) # probability of d given p - get from donor alignment with 1.0 pre simulation
prob_d = d_uniq / (d_uniq + p_uniq)
prob_p = p_uniq / (d_uniq + p_uniq)
amb_d = (prob_p_d * prob_d) / ((prob_p_d * prob_d) + (prob_d_p * prob_p))
amb_p = 1 - amb_d
print(f'ambiguous d prob: {round(amb_d,4)}')
print(f'ambiguous p prob: {round(amb_p,4)}')
d_tot = d_uniq + round(amb_d * ambig)  # total donor counts (with ambiguous estimate)
p_tot = p_uniq + round(amb_p * ambig)  # total pre counts (with ambiguous estimate)


# Table Output
## Sample_ID | Donor_ID | Pre_ID | Donor_Total | Pre_Total | Unmapped | Total_Reads | uniq_donor | uniq_pre | ambiguous
## Simulation | Uniquely Match Donor | Uniquely Match Pre | Ambiguous | Total Donor | Total Pre | Unknown/Unique |
if os.path.exists(out_file):
	with open(out_file, 'a') as f:
		f.write(f'{simulation_pre},{d_uniq},{p_uniq},{ambig},{d_tot},{p_tot},{unknown}\n')
else:
	with open(out_file, 'w') as f:
		f.write('Simulation,Uniquely_Donor,Uniquely_Pre,Ambiguous,Total_Donor,Total_Pre,Unmapped\n')
		f.write(f'{simulation_pre},{d_uniq},{p_uniq},{ambig},{d_tot},{p_tot},{unknown}\n')
