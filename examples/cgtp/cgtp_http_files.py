"""
CGTP - HTTP List & Download Files
===================================
List variable files, TP programs, diagnostic files and other files via HTTP.
Download a file as string. Uses the http sub-client.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: HTTP List & Download Files")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    print("\n--- Variable files ---")
    var_files = robot.cgtp.http.list_variable_files()
    for f in var_files[:10]:
        print(f"  {f}")
    if len(var_files) > 10:
        print(f"  ... ({len(var_files)} total)")

    print("\n--- TP Programs ---")
    programs = robot.cgtp.http.list_tp_programs()
    for f in programs[:10]:
        print(f"  {f}")
    if len(programs) > 10:
        print(f"  ... ({len(programs)} total)")

    print("\n--- Diagnostic files ---")
    diag_files = robot.cgtp.http.list_diagnostic_files()
    for f in diag_files[:10]:
        print(f"  {f.file}")
    if len(diag_files) > 10:
        print(f"  ... ({len(diag_files)} total)")

    print("\n--- Other files ---")
    other_files = robot.cgtp.http.list_other_files()
    for f in other_files[:10]:
        print(f"  {f}")
    if len(other_files) > 10:
        print(f"  ... ({len(other_files)} total)")

    # Download a file
    file_name = input("\nFile name to download as string (leave empty to skip): ").strip()
    if file_name:
        content = robot.cgtp.http.download_as_string(file_name)
        lines = content.splitlines()
        for line in lines[:30]:
            print(f"  {line}")
        if len(lines) > 30:
            print(f"  ... ({len(lines) - 30} more lines)")

finally:
    robot.disconnect()
    print("\nDisconnected.")
