# Advanced Calculator CI/CD Documentation

## 🚀 GitHub Actions CI/CD Pipeline

This project includes a comprehensive CI/CD pipeline using GitHub Actions for automated building, testing, security scanning, and backup management.

## 📋 Workflow Overview

### 1. Main CI/CD Pipeline (`ci-cd.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main`
- Manual workflow dispatch
- Release creation

**Jobs:**
- **Test**: Cross-platform testing (Ubuntu, Windows, macOS) with Python 3.11, 3.12, 3.13
- **Build Console**: Create console calculator executables for all platforms
- **Build GUI**: Create GUI calculator executables for all platforms
- **Security Scan**: Bandit and Safety security analysis
- **Backup**: Automated source code backup (main branch only)
- **Release**: Create GitHub releases with all artifacts
- **Notify**: Pipeline status notifications

### 2. Scheduled Maintenance (`maintenance.yml`)

**Triggers:**
- Daily backup at 2 AM UTC
- Weekly dependency check on Sundays at 3 AM UTC
- Manual workflow dispatch

**Jobs:**
- **Scheduled Backup**: Daily/weekly/full backups with configurable retention
- **Dependency Check**: Security vulnerability scanning of dependencies
- **Cleanup**: Remove old workflow runs and artifacts
- **Health Check**: Repository health and code quality metrics

### 3. Pull Request Validation (`pr-validation.yml`)

**Triggers:**
- Pull request creation/updates

**Jobs:**
- **Validate PR**: Code formatting, linting, quick tests
- **Build Test**: Test executable creation
- **Comment PR**: Automated PR status comments

## 🔧 Setup Instructions

### 1. Repository Setup

1. **Initialize Git Repository:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit with CI/CD pipeline"
   ```

2. **Create GitHub Repository:**
   ```powershell
   # Create repository on GitHub, then:
   git remote add origin https://github.com/yourusername/calculator.git
   git branch -M main
   git push -u origin main
   ```

### 2. GitHub Actions Configuration

The workflows are automatically activated when you push to GitHub. No additional configuration required for basic functionality.

**Optional Configurations:**
- **Codecov**: Add `CODECOV_TOKEN` secret for coverage reporting
- **Slack/Discord**: Add webhook URLs for notifications
- **Custom retention**: Modify artifact retention days in workflows

### 3. Branch Protection Rules

Recommended branch protection for `main`:
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Require pull request reviews before merging
- Dismiss stale reviews when new commits are pushed

## 📊 Artifacts and Reports

### Build Artifacts
- **Console Executables**: `Calculator-Console-{OS}`
- **GUI Executables**: `Calculator-GUI-{OS}`
- **Release Packages**: Combined executables with documentation

### Testing Reports
- **Coverage Reports**: XML format, uploaded to Codecov
- **Test Results**: Detailed pytest output
- **Security Reports**: Bandit and Safety JSON reports

### Backup Artifacts
- **Daily Backups**: Source code only (30-day retention)
- **Weekly Backups**: Full project backup (90-day retention)
- **Release Backups**: Complete archives (1-year retention)

## 🔒 Security Features

### Static Analysis
- **Bandit**: Security vulnerability scanning
- **Safety**: Known security vulnerabilities in dependencies
- **pip-audit**: Package vulnerability auditing

### Code Quality
- **Flake8**: Code linting and style checking
- **Black**: Code formatting validation
- **isort**: Import sorting validation

### Dependency Management
- Automated security updates via Dependabot (if enabled)
- Weekly dependency vulnerability checks
- Automated pip-audit scanning

## 📈 Monitoring and Notifications

### Pipeline Status
- ✅ Success: All tests pass, builds complete
- ⚠️ Warning: Non-critical issues (style violations, minor security issues)
- ❌ Failure: Test failures, build errors, critical security issues

### Automated Reports
- **Daily**: Health check and backup status
- **Weekly**: Dependency security report
- **Per PR**: Validation status and build test results
- **Per Release**: Complete artifact package

## 🛠 Local Development

### Running Tests Locally
```powershell
# Install test dependencies
pip install -r requirements.txt

# Run tests
python -m pytest test_calculator.py -v

# Run with coverage
python -m pytest test_calculator.py -v --cov=calculator_gui --cov-report=html
```

### Code Quality Checks
```powershell
# Formatting
black calculator.py calculator_gui.py

# Import sorting
isort calculator.py calculator_gui.py

# Linting
flake8 calculator.py calculator_gui.py

# Security scan
bandit -r calculator.py calculator_gui.py
```

### Manual Build Test
```powershell
# Test GUI build
pyinstaller --onefile --windowed calculator_gui.py --name "TestBuild"

# Test console build
pyinstaller --onefile calculator.py --name "TestConsole"
```

## 📂 File Structure

```
CALCULATOR/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml              # Main CI/CD pipeline
│       ├── maintenance.yml        # Scheduled maintenance
│       └── pr-validation.yml      # PR validation
├── calculator.py                  # Console calculator
├── calculator_gui.py             # GUI calculator
├── test_calculator.py            # Test suite
├── requirements.txt              # Dependencies
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
└── CI_CD_SETUP.md                # This file
```

## 🔄 Workflow Triggers Summary

| Workflow | Push | PR | Schedule | Manual | Release |
|----------|------|----|---------|---------| --------|
| CI/CD    | ✅    | ✅  | ❌       | ✅       | ✅       |
| Maintenance | ❌ | ❌  | ✅       | ✅       | ❌       |
| PR Validation | ❌ | ✅ | ❌       | ❌       | ❌       |

## 🎯 Best Practices

### Development Workflow
1. Create feature branch from `develop`
2. Make changes and test locally
3. Push to feature branch
4. Create PR to `develop`
5. Review PR validation results
6. Merge after approval
7. Merge `develop` to `main` for releases

### Release Process
1. Ensure all tests pass on `main`
2. Create GitHub release with semantic versioning
3. CI/CD automatically builds and attaches executables
4. Download release artifacts for distribution

### Security Maintenance
- Review security scan reports weekly
- Update dependencies promptly when vulnerabilities are found
- Monitor backup integrity monthly
- Review and rotate any secrets annually

## 🆘 Troubleshooting

### Common Issues

**Build Failures:**
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Ensure PyInstaller compatibility with packages

**Test Failures:**
- Run tests locally first
- Check for platform-specific issues
- Verify test data and expected results

**Security Alerts:**
- Review Bandit/Safety reports in artifacts
- Update vulnerable dependencies
- Add security exceptions if false positives

**Backup Issues:**
- Check artifact retention settings
- Verify backup content in workflow logs
- Ensure adequate repository storage

## 📝 Customization

To customize the pipeline for your needs:

1. **Modify Python versions** in `ci-cd.yml` matrix
2. **Adjust retention periods** in artifact upload steps
3. **Add notification channels** in notify job
4. **Configure additional security tools** in security-scan job
5. **Modify backup schedules** in `maintenance.yml`

## 📞 Support

For issues with the CI/CD pipeline:
1. Check workflow run logs in GitHub Actions tab
2. Review artifact contents for error details
3. Consult GitHub Actions documentation
4. Create issue with workflow logs attached