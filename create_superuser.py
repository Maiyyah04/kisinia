#!/usr/bin/env python
import os
import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent
project_dir = base_dir / "project_kisinia"
sys.path.insert(0, str(project_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kisinia_project.settings")

import django

django.setup()

from django.contrib.auth import get_user_model

username = os.getenv("ADMIN_USERNAME", "")
password = os.getenv("ADMIN_PASSWORD", "")
email = os.getenv("ADMIN_EMAIL", "admin@example.com")

if not username or not password:
    print("Skipping superuser creation: ADMIN_USERNAME or ADMIN_PASSWORD not set")
    raise SystemExit(0)

User = get_user_model()
if User.objects.filter(username=username).exists():
    print(f"Superuser '{username}' already exists")
    raise SystemExit(0)

User.objects.create_superuser(username=username, email=email, password=password)
print(f"Superuser '{username}' created")
