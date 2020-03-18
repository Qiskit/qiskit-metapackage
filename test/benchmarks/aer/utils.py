import sys
import os
from pathlib import Path
dir_path = Path(os.path.relpath(__file__))
sys.path.append(str(dir_path.parent.parent))

from common import *