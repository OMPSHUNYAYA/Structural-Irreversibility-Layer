#!/usr/bin/env sh
set -eu

# Move to repository root (one level above this script)
cd "$(dirname "$0")/.."

# Execute capsule verification
python3 VERIFY_SSIL_CAPSULE/ssil_capsule_verify.py --repo_root . --case recover

exit $?