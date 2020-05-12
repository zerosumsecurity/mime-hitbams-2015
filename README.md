# mime

## description

We have recovered an encrypted mail and the certificate of the recipient. Fortunately we have also recovered the method used to generate the RSA parameters, which was something like gen_rsa.py. Can you read the mail and recover the flag?

## hint (1)
This RSA parameter generation algorithm was actually published in 2003 in a paper called "An algorithm to obtain an RSA modulus with a large private key" by L. Hernández Encinas, J. Muñoz Masqué and A. Queiruga Dios

## hint (2)
The proposed algorithm has been analyzed in a.o. a 2011 paper called "Security Analysis of an RSA Key Generation Algorithm with a Large Private Key" by Fanyu Kong, Jia Yu and Lei Wu. We have used the easy case by choosing a rather large e. 


