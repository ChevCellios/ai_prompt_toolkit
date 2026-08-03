#!/usr/bin/env python3
"""CLI for browsing and filling Markdown prompts in this repository."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
HEADING_RE = re.compile(r"^##\s+(?:\d+\.\s*)?(.+?)\s*$")
FENCE_RE = re.compile(r"^```(?:text)?\s*$", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\[([^\[\]\n]+)\]")


@dataclass(frozen=True)
class Prompt:
    slug: str
    title: str
    category: str
    text: str


def slugify(value: str) -> str:
    value = value.lower().strip()
    return re.sub(r"[^a-z0-9čćžšđ]+", "-", value).strip("-")


def load_prompts(directory: Path = PROMPTS_DIR) -> list[Prompt]:
    prompts: list[Prompt] = []
    if not directory.exists():
        return prompts
    for path in sorted(directory.glob("*.md")):
        category = path.stem.replace("-", " ").title()
        title: str | None = None
        block: list[str] = []
        in_fence = False
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            heading = HEADING_RE.match(line)
            if heading and not in_fence:
                title = heading.group(1).strip()
                continue
            if FENCE_RE.match(line):
                if in_fence and title and block:
                    slug = f"{path.stem}-{slugify(title)}"
                    prompts.append(Prompt(slug, title, category, "\n".join(block).strip()))
                    block, title = [], None
                in_fence = not in_fence
                continue
            if in_fence:
                block.append(line)
    return prompts


def find_prompt(prompts: list[Prompt], selector: str) -> Prompt:
    exact = [p for p in prompts if p.slug == selector]
    if exact:
        return exact[0]
    matches = [p for p in prompts if selector.lower() in p.slug.lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError(f"Prompt nije pronađen: {selector}")
    choices = "\n".join(f"  {p.slug}" for p in matches)
    raise ValueError(f"Odabir nije jednoznačan. Pokušaj s:\n{choices}")


def render_prompt(prompt: Prompt, values: dict[str, str]) -> str:
    return PLACEHOLDER_RE.sub(lambda m: values.get(m.group(1), m.group(0)), prompt.text)


def interactive_values(prompt: Prompt) -> dict[str, str]:
    values: dict[str, str] = {}
    for name in dict.fromkeys(PLACEHOLDER_RE.findall(prompt.text)):
        value = input(f"{name}: ").strip()
        if value:
            values[name] = value
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Pregledaj, pretraži i popuni promptove.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="Izlistaj sve promptove")
    search = sub.add_parser("search", help="Pretraži naslove i sadržaj")
    search.add_argument("query")
    show = sub.add_parser("show", help="Prikaži prompt")
    show.add_argument("selector", help="Puni slug ili njegov jedinstveni dio")
    fill = sub.add_parser("fill", help="Interaktivno popuni oznake u promptu")
    fill.add_argument("selector")
    fill.add_argument("--output", "-o", type=Path, help="Spremi rezultat u datoteku")
    return parser


def print_catalog(prompts: list[Prompt]) -> None:
    for prompt in prompts:
        print(f"{prompt.slug}\n  {prompt.title} · {prompt.category}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    prompts = load_prompts()
    if not prompts:
        print(f"Nema promptova u {PROMPTS_DIR}", file=sys.stderr)
        return 1
    try:
        if args.command == "list":
            print_catalog(prompts)
        elif args.command == "search":
            query = args.query.casefold()
            print_catalog([p for p in prompts if query in f"{p.title} {p.category} {p.text}".casefold()])
        elif args.command == "show":
            print(find_prompt(prompts, args.selector).text)
        elif args.command == "fill":
            prompt = find_prompt(prompts, args.selector)
            result = render_prompt(prompt, interactive_values(prompt))
            if args.output:
                args.output.write_text(result + "\n", encoding="utf-8")
                print(f"Spremljeno: {args.output}")
            else:
                print("\n--- Gotov prompt ---\n")
                print(result)
    except (ValueError, OSError) as exc:
        print(exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
