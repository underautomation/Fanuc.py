"""
Kinematics - Forward & Inverse Kinematics
===========================================
Compute forward kinematics (FK) from joint angles and inverse kinematics (IK)
from a cartesian position, entirely offline — no robot connection or license required.

Steps:
  1. Select a robot model from the built-in catalogue
  2. Display the Denavit-Hartenberg (DH) parameters for that model
  3. Enter joint angles (degrees) and compute FK → cartesian pose
  4. Optionally adjust the cartesian pose, then compute all IK solutions
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.fanuc.kinematics.arm_kinematic_models import ArmKinematicModels
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from underautomation.fanuc.kinematics.kinematics_utils import KinematicsUtils
from underautomation.fanuc.common.cartesian_position import CartesianPosition

# ─── ANSI colors ──────────────────────────────────────────────────────────────
GREEN = "\033[92m"
RESET = "\033[0m"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_all_models():
    """Return a sorted list of (name, int_value) for every robot model."""
    models = []
    for name, value in vars(ArmKinematicModels).items():
        if not name.startswith("_") and isinstance(value, int) and name != "mro":
            models.append((name, value))
    models.sort(key=lambda m: m[0])
    return models


def format_model_name(name):
    """Return the model name, colored green if it starts with CRX."""
    if name.startswith("CRX"):
        return f"{GREEN}{name}{RESET}"
    return name


def ask_float(prompt, default=None):
    """Ask the user for a float value; press Enter to accept the default."""
    if default is not None:
        suffix = f" ({default:.4f})"
    else:
        suffix = ""
    raw = input(f"  {prompt}{suffix}: ").strip()
    if raw == "" and default is not None:
        return default
    return float(raw)


# ─── 1. Select robot model ───────────────────────────────────────────────────

print("=" * 60)
print("  FANUC SDK - Forward & Inverse Kinematics (offline)")
print("=" * 60)

models = get_all_models()

# Display models in columns for compact listing
COLS = 3
col_width = 28
print(f"\nAvailable robot models ({len(models)}):\n")
for i in range(0, len(models), COLS):
    row_parts = []
    for j in range(COLS):
        idx = i + j
        if idx < len(models):
            name = models[idx][0]
            colored = format_model_name(name)
            # Padding must account for ANSI escape length (not visible chars)
            pad = col_width - len(f"  {idx + 1:>3}. {name}")
            entry = f"  {idx + 1:>3}. {colored}{' ' * pad}"
            row_parts.append(entry)
    print("".join(row_parts))

print()
choice_str = input(f"Select a model number [1-{len(models)}] (default 1): ").strip()
choice_idx = (int(choice_str) - 1) if choice_str else 0
if choice_idx < 0 or choice_idx >= len(models):
    print("Invalid selection.")
    sys.exit(1)

model_name, model_value = models[choice_idx]
print(f"\n→ Selected model: {model_name}")

# ─── 2. Show DH parameters ──────────────────────────────────────────────────

dh = DhParameters.from_arm_kinematic_model(ArmKinematicModels(model_value))

print(f"\nDenavit-Hartenberg parameters for {model_name}:")
print("-" * 40)
print(f"  a1 = {dh.a1:>10.4f} mm")
print(f"  a2 = {dh.a2:>10.4f} mm")
print(f"  a3 = {dh.a3:>10.4f} mm")
print(f"  d4 = {dh.d4:>10.4f} mm")
print(f"  d5 = {dh.d5:>10.4f} mm")
print(f"  d6 = {dh.d6:>10.4f} mm")
print(f"  Category: {repr(dh.kinematics_category)}")

# ─── 3. Enter joint angles & compute FK ─────────────────────────────────────

print("\nEnter joint angles in degrees (press Enter for 0):")

j1 = ask_float("J1", 0)
j2 = ask_float("J2", 0)
j3 = ask_float("J3", 0)
j4 = ask_float("J4", 0)
j5 = ask_float("J5", 0)
j6 = ask_float("J6", 0)

# Convert degrees → radians for the FK function
joints_rad = [math.radians(j) for j in [j1, j2, j3, j4, j5, j6]]

print(f"\nComputing forward kinematics for J=[{j1:.2f}, {j2:.2f}, {j3:.2f}, {j4:.2f}, {j5:.2f}, {j6:.2f}] deg ...")

fk_pos = KinematicsUtils.forward_kinematics(joints_rad, dh)

print(f"\nFK result — Cartesian position:")
print("-" * 40)
print(f"  X = {fk_pos.x:>12.4f} mm")
print(f"  Y = {fk_pos.y:>12.4f} mm")
print(f"  Z = {fk_pos.z:>12.4f} mm")
print(f"  W = {fk_pos.w:>12.4f} deg")
print(f"  P = {fk_pos.p:>12.4f} deg")
print(f"  R = {fk_pos.r:>12.4f} deg")
print(f"  Conf = {fk_pos.configuration}")

# ─── 4. Adjust cartesian pose & compute IK ──────────────────────────────────

print("\nEnter cartesian position for IK (press Enter to keep FK value):")

ik_x = ask_float("X [mm]", fk_pos.x)
ik_y = ask_float("Y [mm]", fk_pos.y)
ik_z = ask_float("Z [mm]", fk_pos.z)
ik_w = ask_float("W [deg]", fk_pos.w)
ik_p = ask_float("P [deg]", fk_pos.p)
ik_r = ask_float("R [deg]", fk_pos.r)

ik_target = CartesianPosition(ik_x, ik_y, ik_z, ik_w, ik_p, ik_r, None)

print(f"\nComputing inverse kinematics for X={ik_x:.4f}, Y={ik_y:.4f}, Z={ik_z:.4f}, W={ik_w:.4f}, P={ik_p:.4f}, R={ik_r:.4f} ...")

solutions = KinematicsUtils.inverse_kinematics(ik_target, dh)

if not solutions:
    print("\n⚠  No IK solution found for the given cartesian position.")
else:
    print(f"\n{len(solutions)} IK solution(s) found:")
    print("-" * 100)
    print(f"  {'#':<4} {'J1':>10} {'J2':>10} {'J3':>10} {'J4':>10} {'J5':>10} {'J6':>10}   Configuration")
    print("-" * 100)
    for i, sol in enumerate(solutions, 1):
        # Perform FK on this solution to obtain the configuration
        sol_rad = [math.radians(j) for j in [sol.j1, sol.j2, sol.j3, sol.j4, sol.j5, sol.j6]]
        sol_fk = KinematicsUtils.forward_kinematics(sol_rad, dh)
        conf = sol_fk.configuration
        print(f"  {i:<4} {sol.j1:>10.4f} {sol.j2:>10.4f} {sol.j3:>10.4f} {sol.j4:>10.4f} {sol.j5:>10.4f} {sol.j6:>10.4f}   {conf}")
    print("-" * 100)

print("\nDone.")
