# Position Finder
In this code, the list indicates where the parity bits would go once generated in the Hamming code. It uses a bitwise operator and checks for similarities in the powers of two, based on the message. 
Since the parity bits are meant to go in the positions of powers of two, which, in binary, all have in common that only their first digit from the left is one, a bitwise checker makes sense here. And becausse it is indexed-0, we remove one from the i in the iterated for loop.

## Example
![image](https://github.com/user-attachments/assets/9dc742fa-e0c9-42cf-9df1-f83612f2971f)

<sub>Fig. 1 shows an example of where parity bits would go, denoted as P0, P1...</sub>
