from libcrypto import hamming_distance
from libcrypto import split_blocks
from libcrypto import xor
from libcrypto import freq_score

from base64 import b64decode
from operator import itemgetter


def main():

    file64 = ""
    for line in open("../assets/inputS1C6.txt","r"):
        file64 += line.rstrip()

    file = bytearray(b64decode(file64))

    distances = []
    for keysize in range(2,40):
        dist = 0
        sample_size = 10
        for ctr in range(0, sample_size):
            b1 = bytearray(file[(keysize*ctr):(keysize*(ctr+1))])
            b2 = bytearray(file[(keysize*(ctr+1)):(keysize*(ctr+2))])

            dist += hamming_distance(b1, b2) / float(keysize)
        dist /= sample_size
        distances.append([keysize, dist])

    distances = sorted(distances,key=itemgetter(1))[:1]


    print("Possible Solutions...\n")
    for key in distances:
        passphrase = ""
        key = key[0]
        blocks = split_blocks(key,file)

        transposed_blocks = []
        for idx in range(0,key):
            tblock = bytearray()
            for block in blocks:
                try:
                    tblock.append(block[idx])
                except IndexError:
                    pass
            transposed_blocks.append(tblock)

        for block in transposed_blocks:
            bytekeys = []
            for i in range(1,int("ff",16)):

                xor_bytes = xor(bytearray(bytes({i})),block)

                try:
                    xor_string = xor_bytes.decode("ascii")
                    bytekeys.append([i,xor_string,freq_score(xor_string)])
                except UnicodeDecodeError:
                    next

            bytekeys.sort(key=lambda x: x[2], reverse=True)
            bkey = bytekeys[:1][0]
            passphrase += chr(bkey[0])

        print("Key:{0}\n".format(passphrase))

        print(xor(bytearray(passphrase.encode()),bytearray(file)).decode())

if __name__ == "__main__":
    main()