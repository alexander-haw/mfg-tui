from pathlib import Path
import sys
from tomlkit.toml_file import TOMLFile

PY_PROJECT = "pyproject.toml"
LICENSE_DIR = "/usr/share/common-licenses"

system_licenses = {
    lic.stem: lic
    for lic in Path(LICENSE_DIR).glob("*") if lic.is_file()
}

try:
    for p_dir in (Path(__file__)).parents:
        for p_file in p_dir.glob(f"**/{PY_PROJECT}"):
            poetry_tool = TOMLFile(p_file).read()['tool']['poetry']
            raise StopIteration
except StopIteration: pass
else: poetry_tool = None

__version__ = poetry_tool['version']
__doc__     = poetry_tool['description']
__license   = poetry_tool['license']
def license():
    sys.stdout.write(system_licenses[__license].read_text('ascii'))

del poetry_tool

__all__ = ('__version__', '__doc__', 'license')