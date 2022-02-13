from sys import stderr
from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import subprocess


TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"
STYLES_TEMPLATE_PATH = TEMPLATES_DIR / "styles.css"
CONFIG_TEMPLATE_PATH = TEMPLATES_DIR / "tailwind.config.js"

STYLES_SRC_PATH = Path(
    getattr(settings, "TAILWIND_STYLES_SRC_PATH", "static/src/styles.css")
)
CONFIG_PATH = Path(getattr(settings, "TAILWIND_CONFIG_PATH", "tailwind.config.js"))

TEMPLATE_PATHS = [STYLES_TEMPLATE_PATH, CONFIG_TEMPLATE_PATH]
OUTPUT_PATHS = [STYLES_SRC_PATH, CONFIG_PATH]

STYLES_DIST_PATH = Path(
    getattr(settings, "TAILWIND_STYLES_DIST_PATH", "static/dist/styles.css")
)


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):

        parser.add_argument(
            "--init",
            action="store_true",
            help="Initiate required Tailwind files",
        )

    def handle(self, *args, **options):

        if options["init"]:
            for path in OUTPUT_PATHS:
                # Ensure directories exist
                path.parent.mkdir(parents=True, exist_ok=True)

            for fpath_in, fpath_out in zip(TEMPLATE_PATHS, OUTPUT_PATHS):
                with open(fpath_in) as f_in, open(fpath_out, "w") as f_out:
                    f_out.write(f_in.read())

        else:
            STYLES_DIST_PATH.parent.mkdir(parents=True, exist_ok=True)

            p = subprocess.Popen(
                [
                    "tailwindcss",
                    "-i",
                    str(STYLES_SRC_PATH),
                    "-o",
                    str(STYLES_DIST_PATH),
                    "-c",
                    str(CONFIG_PATH),
                    "--watch",
                ],
                start_new_session=True,
            )

            try:
                p.wait()
            except KeyboardInterrupt:
                try:
                    p.terminate()
                except OSError:
                    pass
                p.wait()
