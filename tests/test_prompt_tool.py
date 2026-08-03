import tempfile
import unittest
from pathlib import Path

from prompt_tool import find_prompt, load_prompts, render_prompt


class PromptToolTests(unittest.TestCase):
    def test_loads_fenced_prompt_with_heading(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.md"
            path.write_text("# Demo\n\n## 1. Moj prompt\n\n```text\nPozdrav [IME].\n```\n", encoding="utf-8")
            prompts = load_prompts(Path(tmp))
        self.assertEqual(len(prompts), 1)
        self.assertEqual(prompts[0].title, "Moj prompt")
        self.assertEqual(prompts[0].text, "Pozdrav [IME].")

    def test_find_by_unique_slug_part_and_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "demo.md").write_text("## Test\n```text\nBok [IME], [IME]!\n```\n", encoding="utf-8")
            prompts = load_prompts(Path(tmp))
        prompt = find_prompt(prompts, "test")
        self.assertEqual(render_prompt(prompt, {"IME": "Jeka"}), "Bok Jeka, Jeka!")


if __name__ == "__main__":
    unittest.main()
