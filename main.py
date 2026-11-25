"""Write the one-line review to /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides)."""

import os

LINE = (
    "This doorstop has held the same door open for six years and has never "
    "once been thanked, promoted, or even noticed - five stars, would ignore again."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip check: what we wrote is exactly what the judge will read.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read().strip() == text


if __name__ == "__main__":
    main()
