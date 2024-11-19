# Verify

## Description

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

Additional details will be available after launching your challenge instance.

## Status

Done

## Notes

1. created a perl pipeline to find the file that matched the checksum provided.
````ls -1 | perl -ne 'system("sha256sum $_");' | perl -ne 'print $_ if $_ =~ /03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8/'``

## Flag

picoCTF{trust_but_verify_00011a60}

## References
