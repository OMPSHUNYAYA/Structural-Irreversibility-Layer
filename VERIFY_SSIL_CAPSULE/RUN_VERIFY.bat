@echo off
cd /d "%~dp0\.."
python VERIFY_SSIL_CAPSULE\ssil_capsule_verify.py --repo_root . --case recover
exit /b %ERRORLEVEL%