# Rosalind Bioinformatics Solutions

This repository contains my solutions to the bioinformatics problems presented on [Rosalind](http://rosalind.info/). The primary aim is to improve my Python programming skills and deepen my understanding of bioinformatics concepts.

## Table of Contents

- [About Rosalind](#about-rosalind)
- [Project Structure](#project-structure)
- [Problems and Solutions](#problems-and-solutions)
- [How to Use](#how-to-use)

## About Rosalind

[Rosalind](http://rosalind.info/) is a platform for learning bioinformatics through problem-solving. It offers a collection of problems of varying difficulty, designed to introduce and reinforce concepts in bioinformatics and computational biology.

## Project Structure
The repository is organized as follows:
```bash
Rosalind/
└── Rosalind_Problems
    ├── Bioinformatics_Stronghold
    │   ├── problem_1
    │   │   ├── README.md
    │   │   ├── problem_1.py
    │   │   └── problem_1_data.txt
    │   ├── problem_2
    │   │   ├── README.md
    │   │   ├── problem_2.py
    │   │   └── problem_2_data.txt
    │   ├── ...
    ├── Python_Village
    │   ├── problem_1
    │   │   ├── README.md
    │   │   ├── problem_1.py
    │   │   └── problem_1_data.txt
    │   ├── ...
    └── README.md
```      
"Python_Village" and "Bioinformatics_Stronghold" are different sections of the Rosalind site, each focused on different topics (introductory Python and bioinformatics). Inside these directories are the problems, and each problem has its own directory containing the solution script, the data used, and a README.md file that describes the problem.

## Problems and Solutions

Below is a list of problems solved so far:

###Bioinformatics_Stronghold
- Counting DNA Nucleotides: [DNA](Rosalind_Problems/Bioinformatics_Stronghold/1_DNA/)
- Transcribing DNA into RNA: [RNA](Rosalind_Problems/Bioinformatics_Stronghold/2_RNA/)
- Complementing a Strand of DNA: [REVC](Rosalind_Problems/Bioinformatics_Stronghold/3_REVC/)
- Rabbits and Recurrence Relations: [FIB](Rosalind_Problems/Bioinformatics_Stronghold/4_FIB/)
- Computing GC Content: [GC](Rosalind_Problems/Bioinformatics_Stronghold/5_GC/)
- Counting Point Mutations: [HAMM](Rosalind_Problems/Bioinformatics_Stronghold/6_HAMM/)
- Mendel's First Law: [IPRB](Rosalind_Problems/Bioinformatics_Stronghold/7_IPRB/)
- Translating RNA into Protein: [FIB](Rosalind_Problems/Bioinformatics_Stronghold/8_PROT/)
- Finding a Motif in DNA: [SUBS](Rosalind_Problems/Bioinformatics_Stronghold/9_SUBS/)

###Python_Village
- Hypotenuse: [INI2](Rosalind_Problems/Python_Village/INI2/)
- Finding Substrings: [INI3](Rosalind_Problems/Python_Village/INI3/)
- Sum of odd numbers: [INI4](Rosalind_Problems/Python_Village/INI4/)
- Even lines: [INI5](Rosalind_Problems/Python_Village/INI5/)
- Word count: [INI6](Rosalind_Problems/Python_Village/INI6/)

## How to Use

1. Clone the repository:
   ```bash
     git clone https://github.com/AlisF42/Rosalind
2. Navigate to a problem directory:
   ```bash
    cd Rosalind_Problems/Bioinformatics_Stronghold/problem1
3. Run the solution script with Python:
  ```bash
     ./problem1.py problem_1_data.txt
