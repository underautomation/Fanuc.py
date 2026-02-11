"""
Helper for Fanuc.py examples
- Automatic sys.path setup
- Persistent robot configuration management
- License management
"""
from enum import Enum
import sys
import json
from pathlib import Path

# ==============================================================================
# Path setup for imports
# ==============================================================================
def setup_path():
    root = Path(__file__).parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

setup_path()

# ==============================================================================
# Configuration file management
# ==============================================================================
_config_file = Path(__file__).parent / "robot_config.json"

def _load_config():
    """Load saved configuration from file."""
    if _config_file.exists():
        try:
            with open(_config_file, 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

def _save_config(config):
    """Save configuration to file."""
    with open(_config_file, 'w') as f:
        json.dump(config, f, indent=2)

def _get_setting(key, prompt, default=None, hide_default=False):
    """
    Generic helper to get a setting from the user.
    If already saved, proposes it as default. Otherwise, asks the user and saves it.
    
    Args:
        key: Config key to load/save
        prompt: Display prompt for the user
        default: Default value if none saved
        hide_default: If True, shows '****' instead of the saved value (for passwords)
    
    Returns:
        str: The setting value
    """
    config = _load_config()
    saved = config.get(key, default)

    if saved is not None:
        display = "****" if hide_default and saved else saved
        user_input = input(f"{prompt} [{display}]: ").strip()
        value = user_input if user_input else saved
    else:
        value = input(f"{prompt}: ").strip()

    # Save if value has changed or is new
    if value != config.get(key):
        config[key] = value
        _save_config(config)

    return value

# ==============================================================================
# Robot IP / Connection
# ==============================================================================
def get_robot_ip():
    """
    Gets the robot IP address or RoboGuide path.
    If already saved, proposes it as default.
    
    For a real robot, enter the IP address (e.g. 192.168.1.10).
    For RoboGuide on local machine, enter the workcell path (e.g. C:\\Users\\...\\Robot_1).
    For RoboGuide on remote machine, use UNC path (e.g. \\\\192.168.8.129\\Users\\...\\Robot_1).
    
    Returns:
        str: Robot IP address or RoboGuide path
    """
    return _get_setting("robot_ip", "Robot IP address or RoboGuide path")

# ==============================================================================
# Telnet settings
# ==============================================================================
def get_telnet_password():
    """
    Gets the telnet KCL password.
    Default Fanuc password is usually empty or 'ADMIN'.
    
    Returns:
        str: Telnet password
    """
    return _get_setting("telnet_password", "Telnet KCL password", default="")

# ==============================================================================
# FTP settings
# ==============================================================================
def get_ftp_user():
    """
    Gets the FTP username.
    Default Fanuc FTP user is usually empty.
    
    Returns:
        str: FTP username
    """
    return _get_setting("ftp_user", "FTP username", default="")

def get_ftp_password():
    """
    Gets the FTP password.
    Default Fanuc FTP password is usually empty.
    
    Returns:
        str: FTP password
    """
    return _get_setting("ftp_password", "FTP password", default="")

# ==============================================================================
# Language setting
# ==============================================================================
def get_language():
    """
    Gets the controller language.
    Supported languages: English, Japanese, Chinese.
    Default is English.
    
    Returns:
        str: Language name
    """
    return _get_setting("language", "Controller language (English/Japanese/Chinese)", default="English")

# ==============================================================================
# License management
# ==============================================================================
def setup_license():
    """
    Checks the current license state and handles registration.
    
    - If already licensed or in trial: prints license info
    - If expired or invalid: asks user for licensee/key and registers
    - If user has no key: shows URL to request a free trial
    
    Returns:
        LicenseInfo: The current license information
    """
    from underautomation.fanuc.fanuc_robot import FanucRobot
    from underautomation.fanuc.license.license_state import LicenseState

    # Try loading saved license credentials
    config = _load_config()
    saved_licensee = config.get("licensee", "")
    saved_key = config.get("license_key", "")

    # Register saved license if available
    if saved_licensee and saved_key:
        license_info = FanucRobot.register_license(saved_licensee, saved_key)
    else:
        # Create a temporary robot to check the default license state
        robot = FanucRobot()
        license_info = robot.license_info

    state = license_info.state

    # If license is valid (Licensed, Trial, or ExtraTrial), just display info
    if state == LicenseState.Licensed or state == LicenseState.Trial or state == LicenseState.ExtraTrial:
        print("=" * 60)
        print("LICENSE INFO")
        print("=" * 60)
        print(license_info)
        print("=" * 60)
        return license_info

    # License is invalid, expired, or needs maintenance
    print("=" * 60)
    print("LICENSE REGISTRATION REQUIRED")
    print("=" * 60)
    print(f"Current license state: {license_info}")
    print()
    print("If you don't have a license key, you can request a free")
    print("trial license immediately by email from:")
    print("  https://underautomation.com/license")
    print()

    licensee = input("Enter licensee (company/name) [leave empty to skip]: ").strip()
    if not licensee:
        print("Skipping license registration. Running in current mode.")
        return license_info

    key = input("Enter license key: ").strip()
    if not key:
        print("No key provided. Skipping registration.")
        return license_info

    # Register the license
    license_info = FanucRobot.register_license(licensee, key)

    # Save credentials
    config["licensee"] = licensee
    config["license_key"] = key
    _save_config(config)

    print()
    print("LICENSE REGISTERED:")
    print(license_info)
    print("=" * 60)

    return license_info

# ==============================================================================
# Helper: Connect to robot with selected protocols
# ==============================================================================
def connect_robot(enable_telnet=False, enable_ftp=False, enable_snpx=False):
    """
    Creates a FanucRobot, sets up license, asks for connection settings,
    and connects with the specified protocols enabled.
    
    Args:
        enable_telnet: Enable Telnet/KCL protocol
        enable_ftp: Enable FTP protocol
        enable_snpx: Enable SNPX protocol
    
    Returns:
        FanucRobot: Connected robot instance
    """
    from underautomation.fanuc.fanuc_robot import FanucRobot
    from underautomation.fanuc.connection_parameters import ConnectionParameters
    from underautomation.fanuc.common.languages import Languages

    # Setup license first
    setup_license()

    # Get robot address
    robot_ip = get_robot_ip()

    # Create robot and connection parameters
    robot = FanucRobot()
    params = ConnectionParameters(robot_ip)

    # Configure protocols
    params.telnet.enable = enable_telnet
    params.ftp.enable = enable_ftp
    params.snpx.enable = enable_snpx

    # Set controller language
    language_name = get_language()
    language_map = {"english": Languages.English, "japanese": Languages.Japanese, "chinese": Languages.Chinese}
    params.language = language_map.get(language_name.lower(), Languages.English)

    # Disable unused protocols
    params.rmi.enable = False
    params.stream_motion.enable = False

    # Set credentials if protocols are enabled
    if enable_telnet:
        password = get_telnet_password()
        params.telnet.telnet_kcl_password = password

    if enable_ftp:
        user = get_ftp_user()
        pwd = get_ftp_password()
        params.ftp.ftp_user = user
        params.ftp.ftp_password = pwd

    # Connect
    protocols = []
    if enable_telnet: protocols.append("Telnet")
    if enable_ftp: protocols.append("FTP")
    if enable_snpx: protocols.append("SNPX")
    print(f"\nConnecting to {robot_ip} ({', '.join(protocols)})...")

    try:
        robot.connect(params)
    except Exception as e:
        error_msg = str(e)
        if "license" in error_msg.lower() or "trial" in error_msg.lower() or "expired" in error_msg.lower() or "InvalidLicenseException" in type(e).__name__:
            # Extract just the human-readable part (before .NET stack trace)
            readable = error_msg.split("\n")[0].strip() if "\n" in error_msg else error_msg
            # Safely print (some .NET exceptions contain Unicode chars that fail on Windows console)
            safe_msg = readable.encode("ascii", errors="replace").decode("ascii")
            print(f"\nLicense error: {safe_msg}")
            print("\nPlease register a valid license first.")
            print("Get a free trial at: https://underautomation.com/license")
            raise SystemExit(1)
        raise

    print("Connected successfully!\n")

    return robot
