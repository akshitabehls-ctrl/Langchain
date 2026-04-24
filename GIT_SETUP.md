# Git Troubleshooting Guide

## Common Issues and Solutions

### Issue: "warning: LF will be replaced by CRLF"

**Cause**: Line ending differences between Windows and Unix systems.

**Solution**:
```bash
git config core.autocrlf true
```

### Issue: .env file accidentally committed

**Solution**:
```bash
git rm --cached .env
git commit -m "Remove .env file from tracking"
# Make sure .env is in .gitignore
```

### Issue: Virtual environment files committed

**Cause**: .venv folder not properly ignored.

**Solution**: Run `git status` to verify `.venv/` is in `.gitignore`, then:
```bash
git rm -r --cached .venv/
git commit -m "Remove virtual environment from git tracking"
```

### Issue: Accidentally tracking __pycache__ folders

**Solution**:
```bash
find . -type d -name __pycache__ -exec git rm -r --cached {} +
git commit -m "Remove __pycache__ directories"
```

### Issue: Large files or binaries tracked

**Solution**: Use `.gitignore` to exclude them before committing, or use Git LFS for large files.

## Before First Push

1. Verify `.gitignore` is properly configured:
   ```bash
   git status
   ```

2. Verify no API keys are in committed files:
   ```bash
   grep -r "OPENAI_API_KEY" --include="*.py" .
   ```

3. Clean up any unwanted tracked files:
   ```bash
   git rm --cached <file-name>
   ```

## Quick Setup Checklist

- [ ] `.gitignore` created and configured
- [ ] `.env.example` created with placeholder values
- [ ] `.env` is in `.gitignore`
- [ ] No `.venv/` tracked
- [ ] No `__pycache__/` tracked
- [ ] No API keys in any committed files
- [ ] `.gitattributes` configured for line endings
- [ ] README.md updated with project info
- [ ] requirements.txt complete and up-to-date
