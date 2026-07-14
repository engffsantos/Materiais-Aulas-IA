from pathlib import Path
import csv
import sys

COURSE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = COURSE_ROOT / "manifesto-laboratorios.csv"


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.exists():
        errors.append("manifesto-laboratorios.csv não encontrado")
    else:
        with MANIFEST.open(encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        if len(rows) != 30:
            errors.append(f"Esperados 30 laboratórios; encontrados {len(rows)}")
        modules = {row["modulo"] for row in rows}
        if len(modules) != 15:
            errors.append(f"Esperados 15 módulos; encontrados {len(modules)}")
        for row in rows:
            lab_dir = COURSE_ROOT.parents[1] / row["pasta"]
            for required in ("README.md", "starter/README.md", "entrega/README.md"):
                if not (lab_dir / required).exists():
                    errors.append(f"Ausente: {lab_dir / required}")

    if errors:
        print("Estrutura inválida:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Estrutura válida: 15 módulos e 30 laboratórios organizados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
