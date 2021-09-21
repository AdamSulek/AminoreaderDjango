# AminoreaderDjango

**AminoReader** is a open-source project written in Django.  
It provides operations on files cotains sequence of nucleotides or aminoacids.


AminoReader provides flexible, three options for loading a file.  
For instance, the row file contains the sequence of codons that can be uploaded. Moreover, it also allows to
load a file consisting of aminoacids sequence in one-character and three-character notation.

AminoReader also provides mass calculation and isoelectric point (pI) of investigated protein.
Isoelectric point (pI) is a pH in which the net charge of the protein is zero.
In the case of proteins, the isoelectric point mostly depends on seven charged amino acids:
glutamate, aspartate, cysteine, tyrosine, histidine, lysine, and arginine.


## Running docker container

To run docker container use docker-compose file  with command:  
`docker-compose up -d `
