# Easy Peasy

## Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 41934 otp.py

## Status

Done

## Done

1. Downlaoded otp.py.
2. Connected to server: nc mercury.picoctf.net 41934
3. Documented the encrypted flag: 0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d.
4. Port updated for the challenge: 11188.
5. Wrote a script to interact with otp.py. The script uses the fact that the inverse of xor is xor itself. 

## Flag

picoCTF{7904ff830f1c5bba8f763707247ba3e1}

## References

- https://realpython.com/python-lambda/
- https://florian.github.io/xor-trick/
- https://www.mathworks.com/matlabcentral/answers/120624-opposite-operation-of-xor
