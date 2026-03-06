from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MACRO_PIPELINE = ROOT / 'scripts' / 'macro_pipeline'
OPS = ROOT / 'scripts' / 'ops'
for path in [str(ROOT), str(MACRO_PIPELINE), str(OPS)]:
    if path not in sys.path:
        sys.path.insert(0, path)
