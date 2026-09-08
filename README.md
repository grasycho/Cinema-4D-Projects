# Cinema 4D Projects

A library of **55 Cinema 4D scene files** demonstrating techniques — Python Tags and Effectors, spline generation, MoGraph setups, procedural geometry, camera rigs and Redshift/OSL shading.

GitHub cannot preview `.c4d` files, so this index describes what each scene contains. Download a file and open it in Cinema 4D to inspect the setup.

---

## Spline generation (Python Tag driven)

Scenes where a Python Tag builds a spline procedurally between or around null objects.

| Scene | Technique |
|---|---|
| `Create_B_Spline.c4d` | B-Spline built from control nulls |
| `Create_Bezier_Spline.c4d` | Bezier spline with tangent control |
| `Create_Hermite_Splines_with_Nulls.c4d` | Hermite interpolation between nulls |
| `Create_Hermite_Splines_with_UI.c4d` | The same, with a user-data interface |
| `Create_Free_Spline_with_4_Nulls.c4d` | Free-form spline through four points |
| `Create_Helix_Between_Two_Nulls_Python_Tag.c4d` | Helix spanning two nulls |
| `Create_Spiral_In_Between_Two_Nulls_Python_Tag.c4d` | Spiral between two nulls |
| `Create_Spiral_In_Between_Two_Nulls_Python_Tag_v2.c4d` | Second revision — see *Notes* |
| `Create_S_Curve_Between_Two_Nulls_Python_Tag.c4d` | S-curve between two nulls |
| `Create_Semi_Circle_Between_Two_Nulls_Python_Tag.c4d` | Semi-circle between two nulls |
| `Create_L_Shape_with_Nulls_Python_Tag.c4d` | Right-angled L path |
| `Create_Triangle_with_Nulls_Python_Tag.c4d` | Triangle from three nulls |
| `Multiple_Semi_Circles_From_Center_Python_Tag.c4d` | Radial array of semi-circles |
| `Multiple_Mospline_Semi_Circles_From_Center_Python_Tag2.c4d` | The same driven through MoSpline |
| `Nulls_To_Spline.c4d` | Spline generated through arbitrary nulls |
| `Parametric_Spline_with_Tracer_and_Nulls.c4d` | Tracer-based parametric spline |
| `Start_to_End_Curve_Python_Generator_Script` | Python Generator source (no file extension) |
| `fibonnacci_spiral.c4d` | Fibonacci spiral construction |

## Working with splines

| Scene | Technique |
|---|---|
| `Align_to_Spline_with_Absolute_Length_Xpresso.c4d` | Align to Spline driven by absolute length, via Xpresso |
| `Align_to_Spline_with_Target_and_Offset.c4d` | Align to Spline with target and offset control |
| `Control_Spline_Thickness_with_Fields.c4d` | Spline thickness modulated by Fields |
| `C4D_Python_Offset_Path.c4d` | Path offsetting in Python |

## MoGraph and Effectors

| Scene | Technique |
|---|---|
| `Pile_Up_Python_Effector_for_Cinema_4D.c4d` | Clones stacking into a pile |
| `Quantize_Effector_Cinema_4D_Python_Effector_by_Arttu_Rautio.c4d` | Quantized clone transforms |
| `Randomize_Index_Python_Effector_for_Cinema_4D.c4d` | Randomized clone index |
| `Reverse_Index_Python_Effector_for_Cinema_4D.py` | Reverses clone index — standalone `.py` |
| `Fade_Clones_by_Arttu_Rautio.c4d` | Progressive clone fade |
| `Scale_Position_Rotation_Effector7.c4d` | Combined SPR effector setup |
| `Sequence_Formula.c4d` | Sequential formula-driven animation |
| `Trigger_Formula_Effector.c4d` | Formula Effector used as a trigger |
| `Cinema 4D Formula Effector Examples` | Formula Effector snippets (text, no extension) |
| `Null_on_Random_Cloner_ID.c4d` | Null constrained to a random clone |
| `Partition Modifier.c4d` | Partitioning clones into groups |
| `Python_Range_Mapper.c4d` | Range remapping in Python |

## Paper and bend setups

| Scene | Technique |
|---|---|
| `PAPER_OPENING_MS_BEND.c4d` | Paper unfolding via MoSpline and Bend |
| `PAPER_OPENING_MS_BEND_TWO_SIDED.c4d` | Two-sided variant |
| `PAPER_OPENING_MS_BEND_TWO_SIDED_WITH_MOSPLINE.c4d` | Two-sided, MoSpline driven |
| `Roll_Unroll_Paper.c4d` | Paper roll and unroll |
| `Python_Effector_Roll_Unroll_Paper.c4d` | The same driven by a Python Effector |

## Procedural geometry

| Scene | Technique |
|---|---|
| `Maze_Generator3.c4d` | Procedural maze generation |
| `AutoSlice2.c4d` | Automated slicing |
| `Polydivider_Native_01.c4d` / `_02.c4d` | Native polygon subdivision setups |
| `Fracture_Technique2.c4d` | Fracturing technique |
| `Thickness_with_Vertex_Map_Procedural.c4d` | Thickness driven by a vertex map |
| `Scale_From_Custom_Axis_v2.c4d` | Scaling around an arbitrary axis |
| `Procedural_Shader_Driven_Plane.c4d` | Plane displaced by a shader |
| `Pie_Chart_Example.c4d` | Procedural pie chart |
| `CountDown_Method.c4d` | Countdown animation setup |

## Cameras

| Scene | Technique |
|---|---|
| `Orbital_Camera_Look_at_Target.c4d` | Orbiting camera locked to a target |
| `Smart_Camera_2.c4d` | Camera rig with automated behaviour |

## Shading and lighting

| Scene | Technique |
|---|---|
| `OSL_Shader_for_Cinema_4D_Redshift_Multi_Color_Shader.c4d` | Redshift OSL multi-colour shader |
| `Redshift_Pulsing_OSL_Shader.c4d` | Pulsing OSL shader |
| `COLORED_LIGHT_01.c4d` | Coloured lighting setup |

## Particles

| Scene | Technique |
|---|---|
| `Emitter_Follows_Spline_Pulsating_v2.c4d` | Emitter following a spline with pulsing output |

---

## Notes

- **Possible mislabelling.** `Create_Spiral_In_Between_Two_Nulls_Python_Tag_v2.c4d` is **139,658 bytes** — byte-for-byte the same size as `Create_Semi_Circle_Between_Two_Nulls_Python_Tag.c4d`. It may be a copy of the semi-circle scene saved under the spiral name rather than a genuine second revision. Worth opening both to confirm before relying on it.
- **Typo in a filename:** `fibonnacci_spiral.c4d` (should be *fibonacci*). Left as-is so existing links keep working.
- **Missing extensions.** `Cinema 4D Formula Effector Examples` and `Start_to_End_Curve_Python_Generator_Script` have no file extension, so GitHub shows them without syntax highlighting. Both are text.
- **Third-party scenes.** `Fade_Clones_by_Arttu_Rautio.c4d` and `Quantize_Effector_Cinema_4D_Python_Effector_by_Arttu_Rautio.c4d` are credited to Arttu Rautio.
- Several scenes use **Redshift**; those will not render on the standard renderer without substitution.
- Scene files are large (100 KB – 2.4 MB). Cloning the full repository pulls roughly 15 MB.

## Related

- [Cinema_4D_Scripts](https://github.com/grasycho/Cinema_4D_Scripts) — Script Manager scripts
- [Cinema-4D-Python-Effectors](https://github.com/grasycho/Cinema-4D-Python-Effectors) — MoGraph Python Effector scripts
- [c4dpl-container-object](https://github.com/grasycho/c4dpl-container-object) — Container Object plugin (C++)

## License

See [LICENSE](LICENSE).
