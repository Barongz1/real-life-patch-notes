"""Real-Life Patch Notes: The Comedy Changelog — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a one-line patch note, 160 characters at most, for a bug in real life or human biology.
"""
import os

LINE = "v2.4.1: fixed a bug where yawning in meetings caused the entire room to yawn, including the boss."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
