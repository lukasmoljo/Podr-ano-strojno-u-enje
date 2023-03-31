import os
import pandas as pd
import hashlib
import magic
import mimetypes
import time

dir_path = "C:\\Users\\A507\\lsmoljo\\files"

file_names = []
extensions = []
md5s = []
sha1s = []
sha256s = []
magic_numbers = []
extension_matches = []
magic_obj = magic.Magic(mime=True)
extension_matches = []
creation_times = []
modification_times = []
access_times = []

hash = "c15e32d27635f248c1c8b66bb012850e5b342119"

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
                
            creation_times.append(
                time.ctime(os.path.getctime(os.path.join(dir_path, file)))
            )
            modification_times.append(
                time.ctime(os.path.getmtime(os.path.join(dir_path, file)))
            )
            access_times.append(
                time.ctime(os.path.getatime(os.path.join(dir_path, file)))
            )
# create a Pandas dataframe with the file names
df = pd.DataFrame(
    {
        "file_name": file_names,
        "extension": extensions,
        "md5": md5s,
        "sha1": sha1s,
        "sha256": sha256s,
        "magic_number": magic_numbers,
        "extension_match": extension_matches,
        "creation_time": creation_times,
        "modification_time": modification_times,
        "access_time": access_times,
    }
)
# print the dataframe

print(df)