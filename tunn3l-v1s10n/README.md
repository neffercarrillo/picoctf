# tunn3l v1s10n

## Description

We found this file. Recover the flag.

## Status

In Progress

## Notes

1. Downloaded file.
2. Ran strings command on the file: strings tunn3l_v1s10n.
3. Grepped results of the strings command for "pico" or "flag". Did not find anything. 
4. Calculated md5 hash of the file - 1e852a0190a00b7a092932224373bb02.
5. Searched in virus total and found out the file was a BMP image.
5. Fixed the bmp header and opened the bmp. The flag was not in the image as expected.
6. 

## Flag

TBD

## References

- https://www.youtube.com/watch?v=rvpvY8yRTK8 (CTF - Image Forensics 101)
- http://www.fastgraph.com/help/bmp_header_format.html
- https://opensource.com/article/20/4/linux-binary-analysis
- https://opensource.com/article/19/10/gnu-binutils
- https://opensource.com/article/21/1/linux-radare2
- https://kb.hostperl.com/knowledgebase/steps-to-analyze-binary-files-in-linux/

