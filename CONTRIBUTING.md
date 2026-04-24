# Contributing to LangChain Projects

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes thoroughly
5. Commit with descriptive messages: `git commit -m "Add descriptive message"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Code Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Include type hints where possible
- Test your code before submitting

## Environment Setup

```bash
pip install -r requirements.txt
```

## Committing Changes

- Keep commits atomic and focused on a single feature
- Use descriptive commit messages
- Reference issues in commit messages when applicable
- Example: `git commit -m "Fix chatbot response formatting (fixes #15)"`

## Common Issues

### Line Ending Issues on Windows

If you experience line ending problems:
```bash
git config core.autocrlf true
git rm -rf --cached .
git reset --hard HEAD
```

### API Key Issues

Never commit `.env` files with actual API keys. Always use `.env.example` as reference.

## Questions?

Open an issue with the "question" label or check existing issues for answers.
