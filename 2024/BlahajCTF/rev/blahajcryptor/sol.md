key is generated by applying RC4 onto the system name (NOKOTAN) with the current timestamp (you can fuzz a range from the date modified value of flag.SMILE)
figure out that you can pull a copy of the decryptor by looking at the transaction history of the blahajcoin and plucking any address that has transferred to the ransomware address
figure out where to place the key in the binary (you can compare diffs) and patch a copy
run the patched decryptor

machine name: NOKOTAN, timestamp: 1726291110, key: 48-BB-C7-82-72-91-93-F2-D4-15-EB-EF-F1-B1-F4-1E

flag: `blahaj{I_WANNA_CRY_SO_BAD}`