// Compute the volume of a horizontal cylinder tank with spherical ends
//
//      _||___________   
//     /              \
//    (~~~~~~~~~~~~~~~~) 
//    (                ) 
//     \______________/  
//       /\        /\
//
// Inputs: Sensor parameters 1, 2 and 3 (SenP)
//         Distance_f1 reading in millimeters (f1)
//         PI
// Output: VolumeT


void HCT(void) {
    float tank_length_f2 = U16_to_float(SenP.Parm1H, SenP.Parm1L);
    float tank_diameter_f3 = U16_to_float(SenP.Parm2H, SenP.Parm2L);
    float tank_radius_f6 = tank_diameter_f3 / 2.0;
    float tank_hemi_radius_f4 = U16_to_float(SenP.Parm3H, SenP.Parm3L);
    float distance_f1 = f1;

    // clamp liquid level within tank to tank diam.
    if (distance_f1 > tank_diameter_f3)
        distance_f1 = tank_diameter_f3;

    // clamp radius of hemisphere ends to tank radius
    if (tank_hemi_radius_f4 > PI * tank_radius_f6)
        tank_hemi_radius_f4 = PI * tank_radius_f6;

    // The volume of liquid within the 2 half-spherical ends
    float hemiVol =
        (PI * tank_hemi_radius_f4 * (3.0 * tank_radius_f6 - distance_f1) * distance_f1 * distance_f1)
        /
        (3.0 * tank_radius_f6);

    // cross-section area of horiz. cylinder from bottom to the liquid level
    float crossSection =
        sqrt((2.0 * tank_radius_f6 - distance_f1) * distance_f1) * (distance_f1 - tank_radius_f6)
        + 
        (tank_radius_f6 * tank_radius_f6 * acos(1.0 - distance_f1 / tank_radius_f6));

    // The bug was that the variable `f3` was used instead of `f2`
    VolumeT = crossSection * tank_length_f2 + hemiVol;
}
