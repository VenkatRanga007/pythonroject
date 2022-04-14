import glob, os

def convert_bytes(size, unit=None):
    if unit == "KB":
        return 'File size: ' + str(round(size / 1024, 3)) + ' Kilobytes'
    elif unit == "MB":
        return 'File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes'
    elif unit == "GB":
        return 'File size: ' + str(round(size / (1024 * 1024 * 1024), 3)) + ' Gigabytes'
    else:
        return 'File size: ' + str(size) + ' bytes'

for f in glob.glob('C://Users/ADMIN/Desktop/AWS/**/*', recursive=True):
    if os.path.isfile(f):
        size = convert_bytes(os.path.getsize(f))
        print(f, " - ", size)