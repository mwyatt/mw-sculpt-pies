# mw-sculpt-pies
## What is this?
This addon has been created and developed over time to aid in a faster workflow while sculpting miniatures in Blender.

## Pies Included

### Create
- Quickly create a primitive with the position and rotation set to the currently selected object.

### Flip
- Flip the selected object over the X, Y, or Z axis and applies scale.

### Misc
`Make single user` Convert the selected object to a single user by disconnecting it from any linked duplicate objects.

`Link object data` Links the mesh data of the selected objects to the last selected object so that they become linked duplicates.

`Convert to mesh` Applies all modifiers or transformations on an object and converts it to a mesh.

`Center origin` Centers the origin of the selected object to its geometry.

`Unparent keep transform` Removes the selected object from its parent and maintains its current scale position and rotation.

`Recalculate outside` Repoints any normals that are facing the wrong way.

`Apply scale` Clears any parents, makes object a single user, applies scale and recalculates normals.

### Modifier

`Decimate 05` Halfs the geometry of the selected object.

`Decimate nudge` Slightly reduces the geometry of the selected object. Useful for a tricky boolean.

`Mirror over` Mirrors the selected object over the X axis of the last selected object.

`Sub division 1` Adds a subdivision modifier to the selected object with a level of 1 and applies.

`Bool union` Adds a boolean modifier to the selected object with the last selected object as the target and sets the operation to union.

`Bool diff` Adds a boolean modifier to the selected object with the last selected object as the target and sets the operation to difference.

### Symmetry
- Copies one side of a mesh to another in sculpt mode.

### Align active
- Aligns the camera to the selected object on various axis.

### Mask slice
`Mask slice fill` Removes the masked geometry, fills the hole and clears the mask.

`Mask slice overlap` Duplicates the selected object, flips the mask and removes the masked geometry to leave a new object overlapping the existing. All masks are cleared.

`Mask slice new object` Applies scale to the object then slices the masked area into a new object and clears the masks.
