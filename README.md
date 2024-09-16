# findBlockers.py
Generate putative blocking oligos based on barcoding sequences for use in target enrichment.

Takes an excel file as an input containing two columns 'barcode_name' and 'barcode_sequence', for each of the sequences in this file it prepends sets of random bases until an oligo is found that melts within a set range. The results are then written to another excel file along with the estimated melting temperature.

Default melting temperatures are based on the blockers published in [Scheunert et al. "Nano-Strainer: A workflow for the identification of single-copy nuclear loci for plant systematic studies, using target capture kits and Oxford Nanopore long reads" ](https://doi.org/10.1002/ece3.10190)

## Script requirements
```
- Python 3.X
- pandas
- openpyxl
- Biopython (Bio.SeqUtils)
```

## Script arguments
```
-m, --minMelt     # Minimum oligo melting temperature. Defaults to 63.4
-M, --maxMelt     # Maximim oligo melting temperature. Defaults to 65.6
-n, --nbases      # Number of bases to prepend. Defaults to 8
-b, --barcodes    # Directory and name for input excel file containing barcode sequences and names.
-o, --output      # Directory and name for output excel file. Defaults to ./output.xlsx
```

## Example input excel file strucutre
Based on the barcoding sequences and 5' flanking regions from the [Oxford Nanopore PCR Barcoding Expansion (EXP-PBC0001)](https://store.nanoporetech.com/pcr-barcoding-expansion-1-12.html)
|barcode_name|barcode_sequence|
|------------|----------------|
|BC01|GGTGCTGAAGAAAGTTGTCGGTGTCTTTGTG|
|BC02|GGTGCTGTCGATTCCGTTTGTAGTCGTCTGT|
|BC03|GGTGCTGGAGTCTTGTGTCCCAGTTACCAGG|
|BC04|GGTGCTGTTCGGATTCTATCGTGTTTCCCTA|
|BC05|GGTGCTGCTTGTCCAGGGTTTGTGTAACCTT|
|BC06|GGTGCTGTTCTCGCAAAGGCAGAAAGTAGTC|
|BC07|GGTGCTGGTGTTACCGTGGGAATGAATCCTT|
|BC08|GGTGCTGTTCAGGGAACAAACCAAGTTACGT|
|BC09|GGTGCTGAACTAGGCACAGCGAGTCTTGGTT|
|BC10|GGTGCTGAAGCGTTGAAACCTTTGTCCTCTC|
|BC11|GGTGCTGGTTTCATCTATCGGAGGGAATGGA|
|BC12|GGTGCTGCAGGTAGAAAGAAGCAGAATCGGA|
