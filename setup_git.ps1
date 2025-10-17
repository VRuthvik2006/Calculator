# PowerShell script for Git setup on Windows
# Calculator Project CI/CD Setup

Write-Host "🚀 Calculator Project Git & CI/CD Setup" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# Check if Git is installed
Write-Host "`n🔍 Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git not found. Please install Git first." -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if already a Git repository
Write-Host "`n🔧 Checking Git repository status..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "✅ Git repository already initialized" -ForegroundColor Green
} else {
    Write-Host "📝 Initializing Git repository..." -ForegroundColor Yellow
    git init
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Git repository initialized" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to initialize Git repository" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Setup Git configuration
Write-Host "`n⚙️ Setting up Git configuration..." -ForegroundColor Yellow

# Check user.name
$userName = git config user.name 2>$null
if (-not $userName) {
    $name = Read-Host "Enter your name for Git commits"
    git config user.name "$name"
}

# Check user.email
$userEmail = git config user.email 2>$null
if (-not $userEmail) {
    $email = Read-Host "Enter your email for Git commits"
    git config user.email "$email"
}

Write-Host "✅ Git configuration complete" -ForegroundColor Green

# Create initial commit
Write-Host "`n📝 Creating initial commit..." -ForegroundColor Yellow

# Add all files
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to add files" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if there are changes to commit
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "ℹ️ No changes to commit" -ForegroundColor Cyan
} else {
    git commit -m "Initial commit: Advanced Calculator with CI/CD pipeline"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Initial commit created" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to create initial commit" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# GitHub remote setup
Write-Host "`n🌐 GitHub Remote Setup (Optional)" -ForegroundColor Yellow
$setupRemote = Read-Host "Do you want to set up a GitHub remote? (y/N)"

if ($setupRemote -match "^[Yy]") {
    $repoUrl = Read-Host "Enter your GitHub repository URL (https://github.com/username/repo.git)"
    
    if ($repoUrl) {
        git remote add origin "$repoUrl"
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ GitHub remote added" -ForegroundColor Green
            
            $pushNow = Read-Host "Push to GitHub now? (y/N)"
            if ($pushNow -match "^[Yy]") {
                Write-Host "📤 Pushing to GitHub..." -ForegroundColor Yellow
                git branch -M main
                git push -u origin main
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ Successfully pushed to GitHub" -ForegroundColor Green
                    Write-Host "🎉 Your CI/CD pipeline will now be active!" -ForegroundColor Green
                } else {
                    Write-Host "❌ Failed to push to GitHub" -ForegroundColor Red
                    Write-Host "You can try pushing manually later with: git push -u origin main" -ForegroundColor Yellow
                }
            }
        } else {
            Write-Host "❌ Failed to add GitHub remote" -ForegroundColor Red
        }
    } else {
        Write-Host "ℹ️ No URL provided, skipping remote setup" -ForegroundColor Cyan
    }
} else {
    Write-Host "ℹ️ Skipping GitHub remote setup" -ForegroundColor Cyan
}

# Display next steps
Write-Host "`n=============================================" -ForegroundColor Cyan
Write-Host "🎉 Git Setup Complete!" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan

Write-Host "`n📋 Next Steps:" -ForegroundColor Yellow
Write-Host "1. If you haven't set up GitHub remote yet:" -ForegroundColor White
Write-Host "   - Create a new repository on GitHub" -ForegroundColor Gray
Write-Host "   - Run: git remote add origin <your-repo-url>" -ForegroundColor Gray
Write-Host "   - Run: git push -u origin main" -ForegroundColor Gray

Write-Host "`n2. Your CI/CD pipeline includes:" -ForegroundColor White
Write-Host "   ✅ Automated testing on multiple platforms" -ForegroundColor Green
Write-Host "   ✅ Cross-platform executable building" -ForegroundColor Green
Write-Host "   ✅ Security scanning" -ForegroundColor Green
Write-Host "   ✅ Automated backups" -ForegroundColor Green
Write-Host "   ✅ Pull request validation" -ForegroundColor Green

Write-Host "`n3. Files created for CI/CD:" -ForegroundColor White
Write-Host "   📁 .github/workflows/ci-cd.yml" -ForegroundColor Gray
Write-Host "   📁 .github/workflows/maintenance.yml" -ForegroundColor Gray
Write-Host "   📁 .github/workflows/pr-validation.yml" -ForegroundColor Gray
Write-Host "   📄 test_calculator.py" -ForegroundColor Gray
Write-Host "   📄 CI_CD_SETUP.md" -ForegroundColor Gray

Write-Host "`n4. To trigger the pipeline:" -ForegroundColor White
Write-Host "   - Push code to main/develop branch" -ForegroundColor Gray
Write-Host "   - Create a pull request" -ForegroundColor Gray
Write-Host "   - Create a release on GitHub" -ForegroundColor Gray

Write-Host "`n📚 Read CI_CD_SETUP.md for detailed documentation" -ForegroundColor Cyan
Write-Host "`n🎯 Your calculator project is now ready for professional development!" -ForegroundColor Green

Read-Host "`nPress Enter to finish"