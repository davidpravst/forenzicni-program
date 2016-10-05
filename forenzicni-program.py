# -*- coding: utf-8 -*-

"""
CSI te je prosil, da narediš za njih foreznični program.
Več navodil si preberi tu:
https://github.com/smartninja/python-exercises/tree/master/challenges/CSI.
"""

filename = "dna.txt"

with open(filename) as file:
    dna = file.read()

hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_blonde = "TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

eye_blue= "TTGTGGTGGC"
eye_green= "GGGAGGTGGC"
eye_brown= "AAGTAGTGAC"

gender_female = "TGAAGGACCTTC"
gender_male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

eva = [gender_female, race_white, hair_blonde, eye_blue, face_oval]
larisa = [gender_female, race_white, eye_brown, face_oval]
matej = [gender_male, race_white, hair_black, eye_blue, face_oval]
miha = [gender_male, race_white, hair_brown, eye_green, face_square]

stevec_eva = 0
stevec_larisa = 0
stevec_matej = 0
stevec_miha = 0

for lastnost in eva:
    if lastnost in dna:
        stevec_eva = stevec_eva + 1
    if stevec_eva == 5:
        print "Sladoled je pojedla Eva!"

for lastnost in larisa:
    if lastnost in dna:
        stevec_larisa = stevec_larisa + 1
    if stevec_larisa == 5:
        print "Sladoled je pojedla Larisa!"

for lastnost in matej:
    if lastnost in dna:
        stevec_matej = stevec_matej + 1
    if stevec_matej == 5:
        print "Sladoled je pojedel Matej!"

for lastnost in miha:
    if lastnost in dna:
        stevec_miha = stevec_miha + 1
    if stevec_miha == 5:
        print "Sladoled je pojedel Miha!"
