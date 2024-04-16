import glob
import os


def findAllFilesWithSuffixInDir(suffix: str, directory: str):
    pattern = os.path.join(directory, '**', suffix)

    # Find all files matching the pattern
    jar_files = glob.glob(pattern, recursive=True)

    return jar_files


if __name__ == '__main__':
    jar_files = findAllFilesWithSuffixInDir("*.jar", os.getcwd())
    print(f"jar_files=[{jar_files}]")
