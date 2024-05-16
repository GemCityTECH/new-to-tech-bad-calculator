# New To Tech Refactoring

A downselect of [python-code-disasters](https://github.com/sobolevn/python-code-disasters) to support a New To Tech session on refactoring and code review for [Gem City Tech](https://gemcity.tech/).

## How to run

### Prerequisites

You must have Python installed.

### Execution

```bash
python calculator.py
```

## Tasks

- Extract the addition, subtraction, multiplication, and division functionality to their own function(s)
- Deduplicate the codebase
- Add exception handling and protection against the user entering invalid symbols or letters
- Add support for typing `2 * 5` instead of inputting the numbers and operators in separate stages
- Migrate the codebase to a CLI library like [click](https://click.palletsprojects.com/en/8.1.x/)
- Add support for exponents and square roots
- Begin developing a unit test suite using [pytest](https://docs.pytest.org/en/8.2.x/)