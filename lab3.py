import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = "C:\\Users\\A507\\lsmoljo\\files"

# create an empty list to store the file names
file_names = []
extensions = []
md5s = []
sha1s = []
sha256s = []
magic_numbers = []
extension_matches = []
magic_obj = magic.Magic(mime=True)

# iterate through all files in the directory
for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file)):
        file_names.append(file)

        name, ext = os.path.splitext(file)
        extensions.append(ext)

        # open the file in binary mode and read its contents
        with open(os.path.join(dir_path, file), "rb") as f:
            file_data = f.read()

            # calculate the MD5 hash value
            md5_hash = hashlib.md5(file_data).hexdigest()
            md5s.append(md5_hash)

            # calculate the SHA1 hash value
            sha1_hash = hashlib.sha1(file_data).hexdigest()
            sha1s.append(sha1_hash)

            # calculate the SHA256 hash value
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            sha256s.append(sha256_hash)

            magic_number = magic_obj.from_buffer(file_data)
            magic_numbers.append(magic_number)
            
            # check if the magic number contains the file extension
            if ext.lower() == "":
                extension_matches.append(False)
            elif mimetypes.guess_type("test" + ext.lower())[0] in magic_number.lower():
                extension_matches.append(True)
            else:
                extension_matches.append(False)


# create a Pandas dataframe with the file names
df = pd.DataFrame(
    {
        "file_name": file_names,
        "extension": extensions,
        "md5s": md5s,
        "sha1s": sha1s,
        "sha256s": sha256s,
        "magic_numbers": magic_numbers,
        "extension_matches": extension_matches,
    }
)

# print the dataframe
print(df)
