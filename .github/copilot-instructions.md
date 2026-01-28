# AI Coding Instructions for comp7940-lab

## Project Overview
**comp7940-lab** is a minimal Python project containing basic demonstrations. Currently contains a simple "Hello World" program as an entry point.

## Architecture & Structure
- **Single module approach**: [hello.py](../hello.py) serves as the main module
- **Entry point**: `main()` function is the conventional entry point
- **Guard clause**: Uses `if __name__ == '__main__'` pattern for script execution

## Python Conventions
- **Style**: Follow PEP 8 standards (4-space indentation, function naming with lowercase_with_underscores)
- **Structure**: Keep functions as the primary organizational unit for this lab project
- **Main pattern**: Always use the `if __name__ == '__main__':` guard when code needs to execute as a script

## Development Workflows
- **Running code**: Execute via `python hello.py` from the project directory
- **Testing approach**: Add unit tests in separate test files when extending functionality
- **Repo context**: Project tracked in git (`.git/` directory present)

## Integration Points
- This is a lab environment (COMP7940) - suitable for educational demonstrations and iterative experimentation
- No external dependencies currently required beyond Python standard library

## When Extending
- Create new modules in the project root alongside [hello.py](../hello.py)
- Follow the established main() + guard clause pattern
- Document any new dependencies added to the project
