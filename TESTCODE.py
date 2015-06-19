#!/usr/bin/python
import sys



##This Program gets two input sequences from the user. Using the sequence, matrices are initialized and filled. After the matrices are filled, the second matrix is used as a trace back tool. 


class ED:




    def __init__(self,seq1,seq2,match,mism,gap):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mism = mism
        self.gap = gap
		
	#Initialize matrix using length of seq1 and seq2. Fill the first row and column of the matrix with gap penalty.
    def make_matrix(self):
        self.seq1 = '-' + self.seq1 #column
        self.seq2 = '-' + self.seq2 #row
        n = len(self.seq2) #row
        m = len(self.seq1) #column


        matrix = [[0 for j in range(m)] for i in range(n)]
        matrix2 = [[0 for j in range(m)] for i in range(n)]

        for i in range(0, n):
            matrix[i][0] = i * self.gap
            matrix2[i][0] = i * self.gap
        for j in range(0, m):
            matrix[0][j] = j * self.gap
            matrix2[0][j] = j * self.gap



        self.matrix = matrix

        self.matrix2 = matrix2



        return self.matrix, self.matrix2, self.seq1, self.seq2

	#Fill matrix, column-wise. Assign match/mismatch score of the previous cell into m_mm and if sequence matches, add match score to m_mm. Vice versa. Then compare m_mm score with scores to the left and above. Choose the largest number and assign the number into the current cell. If max number was from above, mark the second matrix with 2; if from the left, mark the second matrix with 1; if from topleft, mark the second matrix with 0.
    def fill_matrix(self):
        n = len(self.seq2) #row
        m = len(self.seq1) #column
        for i in range(1, n):
            for j in range(1, m):
                m_mm = self.matrix[i-1][j-1]
                if self.seq2[i] != self.seq1[j]:
                    m_mm += self.mism
                else:
                    m_mm += self.match
                horizontal = self.matrix[i-1][j] + self.gap
                vertical = self.matrix[i][j-1] + self.gap

                self.matrix[i][j] = max([m_mm, horizontal, vertical])
                if self.matrix[i][j] == m_mm:
                    self.matrix2[i][j] = 0
                elif self.matrix[i][j] == horizontal:
                    self.matrix2[i][j] = 1
                elif self.matrix[i][j] == vertical:
                    self.matrix2[i][j] = 2


        return self.matrix, self.matrix2
	
	#Using numbers filled in the second matrix, create alignment score. Start with the bottom right cell. If the number is 0, add the corresponding nucleotide of the matrix to each alignment sequences. If the number is 1, add a dash to indicate that there is a gap to one of the sequences. If the number is 2, add a dash to the other sequence. Calculate alignment score. 
    def tracebacking(self):


        alig1 = ''
        alig2 = ''

        j = len(self.seq1)-1
        i = len(self.seq2)-1

        alig1 += self.seq1[j]
        alig2 += self.seq2[i]

        score = 0




        while i>0 or j > 0:
            pos = self.matrix2[i][j]
            if pos == 0:
                alig1 += self.seq1[j]
                alig2 += self.seq2[i]
                i -= 1
                j -= 1
            elif pos == 1:
                alig1 += '-'
                alig2 += self.seq2[i]
                i -= 1
            elif pos == 2:
                alig1 += self.seq1[j]
                alig2 += '-'
                j -= 1




        alig1 = alig1[::-1]
        alig2 = alig2[::-1]

        alig1 = alig1[0:-1]
        alig2 = alig2[0:-1]




        for i in range(0, len(alig1)):
            if alig1[i] == alig2[i]:
                score += self.match
            elif alig1[i] == '-' or alig2[i] == '-':
                score += self.gap
            else:
                score += self.mism




        self.alig1 = alig1
        self.alig2 = alig2
        self.score = score


        return self.alig1, self.alig2, self.score


	#Print alignment score, aligned sequence 1 and 2
    def printing_result(self):
        print
        print "***Brian & Kyuwon's Sequence Alignment***"
        print "Optimal alignment score: " + str(self.score) + '\n'
        print "Alignment 1: \n\n" + self.alig1 + '\n\n'
        print "Alignment 2: \n\n" + self.alig2
        print "*****************************************"





seq1 = "GCTATGCGTAGCATCG"
seq2 = "GCAATGCTGGCATCG"
match = 2
mism = 0
gap = -1

example = ED(seq1,seq2,match,mism,gap)

example.make_matrix()
example.fill_matrix()
example.tracebacking()
example.printing_result()
