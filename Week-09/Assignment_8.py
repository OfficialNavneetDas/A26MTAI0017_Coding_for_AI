"""
Program : payload_parser
purpose : Parses sensor payload packets while enforcing strict positional-only
and keyword-only argument passing.
Author : Navneet das
Date : 21-09-2026
"""

import ast
import os
import re

class SourceAuditor:
    def __init__(self,target_path: str) -> None:
        self.target_path = target_path

    @property
    def target_path(self) ->str:
        return self._target_path

    @target_path.setter
    def target_path(self, value: str) -> None:
        if not os.path.exists(value):
            raise FileNotFoundError(f"Target path \"{value}\" does not exist")
        self._target_path = value
        
    def audit_module_stracture(self, file_contents: str, /, *, max_line_length: int=79) -> dict:
        # read code and return the dictonary of voliations in PEP8 rules
        report = {
            "spacing_violations": [],
            "line_length_violations": [],
            "trailing_whitespace_violations": [],
            "colon_spacing_violations": []
        }
        try:
            tree = ast.parse(file_contents)
        except SyntaxError:
            return report
        top_level_functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]


        for i in range(len(top_level_functions) - 1):
            current_func = top_level_functions[i]
            next_func = top_level_functions[i + 1]

            if next_func.decorator_list:
                effective_start = next_func.decorator_list[0].lineno
            else:
                effective_start = next_func.lineno
                
            blank_lines = effective_start - current_func.end_lineno - 1
            if blank_lines < 2:
                report["spacing_violations"].append(next_func.name)

        lines = file_contents.splitlines()
        
        annotated_lines = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.arg) and node.annotation:
                annotated_lines.add((node.lineno, node.arg))
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                annotated_lines.add((node.lineno, node.target.id))

        for idx, raw_line in enumerate(lines, start=1):
            if len(raw_line) > max_line_length:
                report["line_length_violations"].append(idx)

            if raw_line.strip() != "":
                if raw_line.rstrip() != raw_line:
                    report["trailing_whitespace_violations"].append(idx)

            for line_no, item_name in annotated_lines:
                if line_no == idx:
                
                    pattern = rf"\b{re.escape(item_name)}\s*:\s*\S"
                    if re.search(pattern, raw_line):
                        if idx not in report["colon_spacing_violations"]:
                            report["colon_spacing_violations"].append(idx)

        return report

    def verify_sdist_layout(self, directory_path: str, /) -> bool:
        """Verifies if an sdist directory layout has the required setup and module files."""
        setup_py = os.path.join(directory_path, "..\\Week-08\\text_utility_pkg - v2\\setup.py")
        readme_txt = os.path.join(directory_path, "..\\Week-08\\text_utility_pkg - v2\\README.txt")

        if not os.path.isfile(setup_py) or not os.path.isfile(readme_txt):
            return False

        try:
            with open(setup_py, "r", encoding="utf-8") as f:
                setup_tree = ast.parse(f.read())
        except Exception:
            return False

        py_modules = []
        for node in ast.walk(setup_tree):
            if isinstance(node, ast.Keyword) and node.arg == "py_modules":
                if isinstance(node.value, (ast.List, ast.Tuple)):
                    for elt in node.value.elts:
                        if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                            py_modules.append(elt.value)

        for module in py_modules:
            module_file = os.path.join(directory_path, f"{module}.py")
            if os.path.isfile(module_file):
                return True

        return False

if __name__ == "__main__":
    assert not SourceAuditor(__file__).audit_module_stracture(
        open(__file__, encoding="utf-8").read()
        )["spacing_violation"],"self audit failed: spacing voliations found."
    print("Self-audit passed: no top level function spaceing violations.")
    
