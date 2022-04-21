# zlib compress data
import zlib
# base64 encodes data
import base64

# open and read content of file
data = open('demo.txt', 'r').read()
# converts string file 'demo' in to bytes
data_bytes = bytes(data, 'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
# convert back to string
decoded_data = compressed_data.decode('utf-8')
# write compressed data to new file
compressed_file = open('compressed.txt', 'w')
compressed_file.write(decoded_data)

# decompressing the file to make it readable
decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)