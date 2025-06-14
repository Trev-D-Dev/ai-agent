import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.join(abs_working_dir, file_path)
        print(target_dir)
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_dir):
        print("Directory doesn't exist")
        os.makedirs(target_dir)

write_file(".", "/test", "")