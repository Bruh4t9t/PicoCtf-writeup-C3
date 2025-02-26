chars = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
charlist = []
for char in chars:
  charlist.append(lookup2.index(char))
prev = 0
current = 0
plaintext = []
for char in range(len(chars)):
  prev = current
  for i in range(40):
    if ((i - prev) % 40) == charlist[char]:
      current = i
      plaintext.append(lookup1[i])
print("".join(plaintext))
