***Brian & Kyuwon’s Sequence Alignment***
Made by: 류영재 Brian Youngjae Ryu (2014-22454) and 심규원 Kyuwon Shim (2015-20508)

This python program implements dynamic programming algorithm which returns a global alignment of two input sequences. This program gets two input sequences from the user. Using the sequence, matrices are initialized and filled. After the matrices are filled, the second matrix is used as a trace back tool. 

There are four functions aside from the init function.

The first function, make_matrix, initializes matrix using length of seq1 and seq2. By initializing the matrix, it fills the first row and column of the matrix with gap penalty.

The second function, fill_matrix, fills the matrix, column-wise. It assigns match/mismatch score of the previous cell into m_mm and if sequence matches, add match score to m_mm. Vice versa. Then compares m_mm score with scores to the left and above. It next chooses the largest number and assign the number into the current cell. If max number was from above, mark the second matrix with 2; if from the left, mark the second matrix with 1; if from topleft, mark the second matrix with 0.

The third function, tracebacking, uses numbers filled in the second matrix, calculating the alignment score. Calculation starts with the bottom right cell. If the number is 0, add the corresponding nucleotide of the matrix to each alignment sequences. If the number is 1, a dash is added to indicate that there is a gap to one of the sequences. If the number is 2, a dash is added to the other sequence. The alignment score is then calculated. 

The fourth function, print_result, prints alignment score, signed sequences 1 and 2.

To run this program:
	type: ~/yourProgramPath/python/Edit_distance.py
	
	Example: /storage/home/brian/python Edit_distance.py
	
Output Example:

***Brian & Kyuwon's Sequence Alignment***
Optimal alignment score: 25

Alignment 1: 

GCTATGCGTAGCATCG


Alignment 2: 

GCAATGC-TGGCATCG
*****************************************