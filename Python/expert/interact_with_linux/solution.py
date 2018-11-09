#!/usr/bin/env python3
import os
import shutil
import sys
import pathlib

# I will NEVER EVER use subproccess again
# At least not for something like Popen
try:
    from sh import wget
except Exception:
    print('[!] Just install sh right now!(pip install --user sh)')
    sys.exit(0)

# Dumb Python2 support
if sys.version_info[0] == 2:
    input = raw_input


# Errors do annoy sh
# Weird printing else
# So just render these errors useless! :D
exit_codes = (i for i in range(0, 9))

# Path where this python script is located when it's run
curr_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

# The URL
url = input('[$] Url(none for ema.perfact.de): ')
url = url if url else 'ema.perfact.de'
print('[*] Url: {}\n'.format(url))

# Get name of the directory where the whole page should be saved
dir_name = input('[$] Directory name for the page(none for "1337"): ')
dir_name = dir_name if dir_name else '1337'
page_dir = curr_dir / dir_name
if page_dir.is_dir():
    print('[!] {} is already a directory and will be overwritten!'.format(page_dir))
    choice = input('[!] Continue?(y/n):').lower()
    if choice != 'y':
        sys.exit(0)
print('[*] Directory to save the page: {}\n'.format(dir_name))

# Get name of directory where the files will be saved we actually want to save
save_name = input('[$] Directory name to save findings(none for "saved"): ')
save_name = save_name if save_name else 'saved'
save_dir = curr_dir / save_name
if save_dir.is_dir():
    print('[!] {} is already a directory!'.format(save_dir))
    choice = input('[!] Delete it?(y/n): '.format(save_dir)).lower()
    if choice == 'y':
        shutil.rmtree(save_dir)
    else:
        sys.exit(0)
os.makedirs(save_dir)
print('[*] Directory to save findings: {}\n'.format(save_name))

# The searchterm (which files we want to copy)
print('[*] Everything with the following substring will be copied')
search_term = input('[$] Files to copy to that directory(none for ".png"): ')
search_term = search_term if search_term else '.png'
print('[*] Searchterm: {}\n'.format(search_term))

input('\n[$] Press any key to continue...')

# Sets off the wget -m <url> -P <directory> commande
# It's written so weird, so we can see the output of the program
try:
    for line in wget('-m', url, '-P', dir_name,  _iter=True, _err_to_out=True,
                     _out_bufsize=1, _ok_code=exit_codes):
        print(line)
except Exception:
    pass

# Copying the files we want to save
try:
    files = list(page_dir.glob("**/*{}".format(search_term)))
    if not files:
        print("[!] No matching files found")
    else:
        print("[*] Copying {} *{} files...".format(len(files), search_term))
        for f in page_dir.glob("**/*{}".format(search_term)):
            shutil.copy(f, save_dir)
except Exception as e:
    print('[!] Something went wrong while copying data')
    print(e)

# Deleting the saved webpage, cause we don't need it anymore
print('\n[*] Cleaning up...\n')
if page_dir.is_dir():
    shutil.rmtree(page_dir)

print('[*] All done!')
