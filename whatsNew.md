## More robot models in ArmKinematicModels

The following models have been added to the `ArmKinematicModels` enum:

- `ARCMate100iDDC`, `ARCMate100iDFG`, `ARCMate100iD16SB441`
- `ARCMate120iDFG`
- `CR35iB`, `CR7iAL_2`
- `CRX3iA`, `CRX5iA`, `CRX20iAL`, `CRX30iA`, `CRX10iALPaint`
- `LR10iA10`, `LRMate1011AFoodClean`, `LRMate200iD7WE`
- `M710iC20L`, `M710iD50M`, `M710iD70`
- `M800iB60`, `M8006020B`, `M81019020B`, `M81027027B`
- `M900iB700E`, `M910400F37B`, `M950iA500`, `M950iA500SE`, `M950500F28A`
- `M1000iA`, `M1000550F46A`, `M410800F32C`
- `R2000iC190S`, `R2000iC190SSE`, `R2000iC270FSE`
- `R2000125F31E`, `R2000210F31E`, `R2000300F27E`, `R2000180F27E`

> **Note:** do not rely on the implicit integer values of `ArmKinematicModels` members. The enum is sorted alphabetically and new models may be inserted at any position in future releases, shifting the integer values of existing members. Always use the named members, not their numeric equivalents.

## CRX inverse kinematics: analytical solver, no seed required

The CRX cobot inverse kinematics solver has been rewritten using a closed-form geometric approach. It now computes all valid joint solutions for a given Cartesian pose without requiring a seed position.

The `seed_joints` parameter has been removed from `CrxKinematicsUtils.inverse_kinematics`. If your code was passing a seed, remove that argument.

The solver is now around 3x faster. The `include_duals` parameter remains available to control whether dual solutions are included.

```python
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from underautomation.fanuc.kinematics.kinematics_utils import KinematicsUtils
from underautomation.fanuc.common.cartesian_position import CartesianPosition

dh = DhParameters.from_arm_kinematic_model("CRX10iA")
target = CartesianPosition(x=400, y=250, z=650, w=0, p=90, r=0, configuration=None)

# All solutions are returned, no seed needed
solutions = KinematicsUtils.inverse_kinematics(target, dh)

# Or call the CRX-specific method directly
from underautomation.fanuc.kinematics.crx.crx_kinematics_utils import CrxKinematicsUtils
solutions = CrxKinematicsUtils.inverse_kinematics(target, dh, include_duals=True)
```

