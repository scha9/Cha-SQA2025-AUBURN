### Report

## Activities Completed

### 1. Project Setup
- Unpacked and explored the provided `KubeSec` Python project.
- Uploaded the project to GitHub under the name `Cha-SQA2025-AUBURN`.
- Created and updated `README.md` with team information.

### 2. Git Hook Implementation
- Created a `pre-commit` Git hook located in `.git/hooks/pre-commit`.
- Hook runs `bandit` to scan all Python files for security vulnerabilities.
- Results are automatically saved to `security_report.csv` on every commit.
- ![image](https://github.com/user-attachments/assets/7f9569f4-3e26-41cf-8f4b-1ef62fea2ccb)


### 3. Fuzz Testing (`fuzz.py`)
- Developed `fuzz.py` to randomly test 5 critical Python methods:
  - `checkIfWeirdYAML`
  - `keyMiner`
  - `getKeyRecursively`
  - `checkIfValidK8SYaml`
  - `getValsFromKey`
- Captured and logged all errors and exceptions.
- Integrated into GitHub Actions with `.github/workflows/fuzz.yml` for automatic execution on each push.
- ![image](https://github.com/user-attachments/assets/c0236d09-d74e-4af3-b630-47d779a12ed4)


### 4. Forensics Logging
- Modified 5 Python methods to include forensic logs:
  - Timestamps, usernames, input parameters, and exceptions.
  - Logs written to `forensics.log` using Python’s logging module.
- Useful for debugging, audit trails, and identifying misuse.
- ![image](https://github.com/user-attachments/assets/fc0ff805-a49f-46ab-8b66-361e689bdd61)


### 5. GitHub Actions Integration
- Created a workflow file to run `fuzz.py` automatically.
- Ensured project security and stability checks are run on every push to `main`.

---

## Lessons Learned

### Git and GitHub
- Gained deep experience in managing Git conflicts, remote errors, and history rewrites (e.g., removing secrets from commit history).
- Learned how GitHub protects repositories from accidental secret exposure with push protection.

### Security Automation
- Understood how to integrate tools like `bandit` into Git workflows using pre-commit hooks.
- Automated security scanning provides fast feedback without needing manual execution.

### Fuzzing
- Learned how fuzz testing helps discover hidden bugs and edge cases by providing randomized inputs.
- Validated that functions handled exceptions gracefully and did not crash the program.

### Forensic Integration
- Realized the value of adding runtime logging to critical functions.
- Learned to use Python’s built-in logging for visibility and traceability of code execution.

### GitHub Actions
- Discovered how GitHub Actions can automate testing and validation with every code change.


## Team
- Team name: Cha
- Member: Soyeong Cha
