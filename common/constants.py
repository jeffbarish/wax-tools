from pathlib import Path

DATABASE = 'recordings'
METADATA = Path(DATABASE, 'metadata')
CONFIG = Path(METADATA, 'config')
SHORT = Path(METADATA, 'short')
LONG = Path(METADATA, 'long')
