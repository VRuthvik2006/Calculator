#!/usr/bin/env python3
"""
Git setup script for the Calculator project
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, cwd=None, check=True):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=check
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None


def check_git_installed():
    """Check if Git is installed"""
    result = run_command("git --version", check=False)
    if result and result.returncode == 0:
        print(f"✅ Git found: {result.stdout.strip()}")
        return True
    else:
        print("❌ Git not found. Please install Git first.")
        return False


def initialize_git_repo():
    """Initialize Git repository"""
    print("\n🔧 Initializing Git repository...")
    
    # Check if already a git repo
    if os.path.exists('.git'):
        print("✅ Git repository already initialized")
        return True
    
    # Initialize git repo
    result = run_command("git init")
    if result and result.returncode == 0:
        print("✅ Git repository initialized")
        return True
    else:
        print("❌ Failed to initialize Git repository")
        return False


def setup_git_config():
    """Setup basic Git configuration"""
    print("\n⚙️ Setting up Git configuration...")
    
    # Check if user.name is set
    result = run_command("git config user.name", check=False)
    if not result or result.returncode != 0 or not result.stdout.strip():
        name = input("Enter your name for Git commits: ")
        run_command(f'git config user.name "{name}"')
    
    # Check if user.email is set
    result = run_command("git config user.email", check=False)
    if not result or result.returncode != 0 or not result.stdout.strip():
        email = input("Enter your email for Git commits: ")
        run_command(f'git config user.email "{email}"')
    
    print("✅ Git configuration complete")


def create_initial_commit():
    """Create initial commit"""
    print("\n📝 Creating initial commit...")
    
    # Add all files
    result = run_command("git add .")
    if not result or result.returncode != 0:
        print("❌ Failed to add files")
        return False
    
    # Check if there are any changes to commit
    result = run_command("git diff --cached --quiet", check=False)
    if result and result.returncode == 0:
        print("ℹ️ No changes to commit")
        return True
    
    # Create initial commit
    result = run_command('git commit -m "Initial commit: Advanced Calculator with CI/CD pipeline"')
    if result and result.returncode == 0:
        print("✅ Initial commit created")
        return True
    else:
        print("❌ Failed to create initial commit")
        return False


def setup_github_remote():
    """Setup GitHub remote (optional)"""
    print("\n🌐 GitHub Remote Setup (Optional)")
    
    setup_remote = input("Do you want to set up a GitHub remote? (y/N): ").lower().strip()
    if setup_remote not in ['y', 'yes']:
        print("ℹ️ Skipping GitHub remote setup")
        return True
    
    repo_url = input("Enter your GitHub repository URL (https://github.com/username/repo.git): ").strip()
    if not repo_url:
        print("ℹ️ No URL provided, skipping remote setup")
        return True
    
    # Add remote
    result = run_command(f'git remote add origin "{repo_url}"')
    if result and result.returncode == 0:
        print("✅ GitHub remote added")
        
        # Optionally push to GitHub
        push_now = input("Push to GitHub now? (y/N): ").lower().strip()
        if push_now in ['y', 'yes']:
            print("📤 Pushing to GitHub...")
            result = run_command("git branch -M main")
            if result and result.returncode == 0:
                result = run_command("git push -u origin main")
                if result and result.returncode == 0:
                    print("✅ Successfully pushed to GitHub")
                    print("🎉 Your CI/CD pipeline will now be active!")
                else:
                    print("❌ Failed to push to GitHub")
                    print("You can try pushing manually later with: git push -u origin main")
        return True
    else:
        print("❌ Failed to add GitHub remote")
        return False


def display_next_steps():
    """Display next steps for the user"""
    print("\n" + "="*60)
    print("🎉 Git Setup Complete!")
    print("="*60)
    print("\n📋 Next Steps:")
    print("1. If you haven't set up GitHub remote yet:")
    print("   - Create a new repository on GitHub")
    print("   - Run: git remote add origin <your-repo-url>")
    print("   - Run: git push -u origin main")
    print("\n2. Your CI/CD pipeline includes:")
    print("   ✅ Automated testing on multiple platforms")
    print("   ✅ Cross-platform executable building")
    print("   ✅ Security scanning")
    print("   ✅ Automated backups")
    print("   ✅ Pull request validation")
    print("\n3. Files created for CI/CD:")
    print("   📁 .github/workflows/ci-cd.yml")
    print("   📁 .github/workflows/maintenance.yml")
    print("   📁 .github/workflows/pr-validation.yml")
    print("   📄 test_calculator.py")
    print("   📄 CI_CD_SETUP.md")
    print("\n4. To trigger the pipeline:")
    print("   - Push code to main/develop branch")
    print("   - Create a pull request")
    print("   - Create a release on GitHub")
    print("\n📚 Read CI_CD_SETUP.md for detailed documentation")
    print("\n🎯 Your calculator project is now ready for professional development!")


def main():
    """Main setup function"""
    print("🚀 Calculator Project Git & CI/CD Setup")
    print("="*60)
    
    # Check prerequisites
    if not check_git_installed():
        sys.exit(1)
    
    # Setup Git
    if not initialize_git_repo():
        sys.exit(1)
    
    setup_git_config()
    
    if not create_initial_commit():
        sys.exit(1)
    
    setup_github_remote()
    
    display_next_steps()


if __name__ == "__main__":
    main()