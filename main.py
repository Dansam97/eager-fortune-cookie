import os

ENTRY = "Your code will compile on the first try. It will not be yours."

# Gate check (kit: /output/entry.txt must be UTF-8 text of 1 to 120
# characters, not only white space) — fail loudly instead of writing
# an entry the sealed scorer would reject.
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate is 1-120"
assert ENTRY.strip(), "entry must not be only whitespace"
ENTRY.encode("utf-8")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
