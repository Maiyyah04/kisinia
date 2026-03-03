from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Print current Postgres database/schema details and public table list."

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("select current_database(), current_schema()")
            current_db, current_schema = cursor.fetchone()

            cursor.execute(
                "select count(*) from information_schema.tables where table_schema = 'public'"
            )
            public_count = cursor.fetchone()[0]

            cursor.execute(
                """
                select table_name
                from information_schema.tables
                where table_schema = 'public'
                order by table_name
                """
            )
            tables = [row[0] for row in cursor.fetchall()]

            cursor.execute("select count(*) from django_migrations")
            migration_count = cursor.fetchone()[0]

        self.stdout.write(self.style.SUCCESS(f"database: {current_db}"))
        self.stdout.write(self.style.SUCCESS(f"schema: {current_schema}"))
        self.stdout.write(self.style.SUCCESS(f"public table count: {public_count}"))
        self.stdout.write(self.style.SUCCESS(f"django_migrations rows: {migration_count}"))

        if tables:
            self.stdout.write("tables:")
            for name in tables:
                self.stdout.write(f"- {name}")
        else:
            self.stdout.write(self.style.WARNING("No tables found in public schema."))
