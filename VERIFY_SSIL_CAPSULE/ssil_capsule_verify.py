import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_ARGS = 2
EXIT_MISSING = 3


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_clean_dir(p: Path) -> None:
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)


def require_file(p: Path) -> None:
    if not p.exists():
        raise FileNotFoundError(str(p))


def build_env():
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = "0"
    env["LC_ALL"] = "C"
    env["LANG"] = "C"
    env["TZ"] = "UTC"
    return env


def run_py(args_list, env):
    cp = subprocess.run(
        [sys.executable] + args_list,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if cp.returncode != 0:
        if cp.stdout:
            sys.stderr.write(cp.stdout)
        if cp.stderr:
            sys.stderr.write(cp.stderr)
        raise RuntimeError("subprocess failed: " + " ".join(args_list))
    return cp.stdout


def find_expected_hash(expected_file: Path) -> str:
    txt = expected_file.read_text(encoding="utf-8", errors="replace")
    for line in txt.splitlines():
        s = line.strip()
        if not s:
            continue
        low = s.lower()
        if all(c in "0123456789abcdef" for c in low) and len(low) == 64:
            return low
    return ""


def parse_args():
    ap = argparse.ArgumentParser(prog="ssil_capsule_verify.py")
    ap.add_argument("--repo_root", default="..")
    ap.add_argument("--case", default="recover", choices=["recover"])
    ap.add_argument("--pin_fingerprint", action="store_true")
    return ap.parse_args()


def main():
    try:
        args = parse_args()
    except SystemExit:
        return EXIT_ARGS

    repo_root = Path(args.repo_root).resolve()
    env = build_env()

    try:
        engine = repo_root / "scripts" / "ssil_engine_v1_2.py"
        trace = repo_root / "traces" / "trace_recover.csv"
        require_file(engine)
        require_file(trace)

        capsule_dir = repo_root / "VERIFY_SSIL_CAPSULE"
        out_root = capsule_dir / "OUT"
        ensure_clean_dir(out_root)

        out_a = out_root / "REPLAY_A"
        out_b = out_root / "REPLAY_B"
        ensure_clean_dir(out_a)
        ensure_clean_dir(out_b)

        out_csv_a = out_a / "ssil_out.csv"
        out_csv_b = out_b / "ssil_out.csv"

        locked_args = [
            "--H", "8",
            "--delta-max", "0.05",
            "--s-max", "10.0",
            "--rho", "1.0",
            "--beta", "0.5",
            "--gamma", "0.5",
            "--wA", "0.6",
            "--wB", "0.2",
            "--wS", "0.2",
        ]

        run_py([str(engine), "--in", str(trace), "--out", str(out_csv_a)] + locked_args, env)
        run_py([str(engine), "--in", str(trace), "--out", str(out_csv_b)] + locked_args, env)

        if out_csv_a.stat().st_size != out_csv_b.stat().st_size:
            sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
            return EXIT_FAIL

        h_a = sha256_file(out_csv_a)
        h_b = sha256_file(out_csv_b)
        if h_a != h_b:
            sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
            return EXIT_FAIL

        expected_path = capsule_dir / "EXPECTED_SHA256.txt"

        if args.pin_fingerprint:
            expected_path.write_text(
                "SSIL CORE CASESET REPLAY OUTPUT HASH\n"
                "Profile: public\n"
                "Caseset: recover\n\n"
                "Expected SHA256 (ssil_out.csv):\n"
                f"{h_a}\n\n"
                "Verification Rule:\n"
                "B_A = B_B\n"
                "and\n"
                "SHA256(ssil_out.csv) must match the expected hash above.\n\n"
                "No tolerance.\n"
                "No partial acceptance.\n"
                "Byte identity required.\n",
                encoding="utf-8",
                newline="\n",
            )
            sys.stdout.write("SSIL_CAPSULE_RESULT: PASS\n")
            return EXIT_OK

        require_file(expected_path)
        exp = find_expected_hash(expected_path)
        if not exp:
            sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
            return EXIT_FAIL

        if h_a != exp or h_b != exp:
            sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
            return EXIT_FAIL

        sys.stdout.write("SSIL_CAPSULE_RESULT: PASS\n")
        return EXIT_OK

    except FileNotFoundError as e:
        sys.stderr.write("MISSING: " + str(e) + "\n")
        sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
        return EXIT_MISSING
    except Exception as e:
        sys.stderr.write("FAIL: " + repr(e) + "\n")
        sys.stdout.write("SSIL_CAPSULE_RESULT: FAIL\n")
        return EXIT_FAIL


if __name__ == "__main__":
    raise SystemExit(main())
