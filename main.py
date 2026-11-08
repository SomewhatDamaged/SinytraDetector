import glob
import os
import zipfile


def get_cwd():
    return glob.glob(r"./jars/*.jar")


def find_sinytra():
    if not os.path.exists('./jars/'):
        os.makedirs('./jars/')
        print("Created 'jars' folder. Put jar files in there to test.")
        return
    for path in get_cwd():
        with zipfile.ZipFile(path, 'r') as zip_ref:
            if "META-INF/jarjar/metadata.json" in zip_ref.namelist():
                with zip_ref.open(name="META-INF/jarjar/metadata.json", mode="r") as zip_file:
                    if "org.sinytra.forgified-fabric-api" in zip_file.read().decode("utf-8"):
                        print(f"File: '{str(path).rsplit('\\', 1)[-1]}' has Sinytra")


if __name__ == '__main__':
    find_sinytra()
