"""
Define a function called is_valid_parity. It accepts two strings. The first is called codeword
and the second is called parity.

The is_valid_parity function returns True if codeword is parity-encoded correctly. If it
is not, the function returns False.

A parity-encoded codeword is a string of binary digits (zeros and ones) where the
left-most digit is actually an extra digit that has been prepended to some original
number. The left-most digit we prepend is either a zero or one depending on the type
of parity being used (EVEN or ODD).

If a word is encoded with EVEN parity the total number of 1 bits in the final codeword
must be an even number.

If a word is encoded with ODD parity the total number of 1 bits in the final codeword
must be an odd number.

For example if the original word is 1001:

   an EVEN codeword is 01001 (There are two 1s, 1 + 1 = 2 which is even,
   so we prepend a 0 to the original 1001 to keep the total number of 1s even)

   an ODD codeword is 11001 (There are two 1s, 1 + 1 = 2 which is even,
   so we prepend a 1 to the original 1001 to keep the total number of 1s odd)

Your function must accept a string codeword (the original value with the parity bit
prepended to it) and a parity (EVEN or ODD) as parameters and return True if the
codeword has been correctly parity-encoded, else False.

You must provide a full docstring for this function including all pre- and post-conditions.

Prove your function works in the docstring with these doctests:

           is_valid_parity("101", "EVEN") returns True
           is_valid_parity("11", "EVEN") returns True
           is_valid_parity("111111111100000000001010110101", "EVEN") returns True
           is_valid_parity("10", "ODD") returns True
           is_valid_parity("111", "ODD") returns True
           is_valid_parity("1111111111000011111000001010110101", "ODD") returns True
           is_valid_parity("111", "EVEN") returns False
           is_valid_parity("11111111100000000001010110101", "EVEN") returns False
           is_valid_parity("11", "ODD") returns False
           is_valid_parity("101", "ODD") returns False
           is_valid_parity("11111111111000011111000001010110101", "ODD") returns False

No main function is required.
"""
