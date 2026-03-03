#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    project_dir = base_dir / "project_kisinia"
    sys.path.insert(0, str(project_dir))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kisinia_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
