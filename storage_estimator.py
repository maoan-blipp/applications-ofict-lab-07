def estimate_storage(num_files, size_mb):
    return num_files * size_mb

files = int(input("Number of files: "))
size = float(input("Average size of each file (MB): "))
total = estimate_storage(files, size)
print(f"Total storage needed: {total} MB")