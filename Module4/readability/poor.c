// There is a bug in here somehere.  Can you spot it?
// *********************************************************

//hori cyl tank with spherical  ends
void HCT(void) {
    f2 = U16_to_float(SenP.Parm1H, SenP.Parm1L);
    f3 = U16_to_float(SenP.Parm2H, SenP.Parm2L);
    f6 = f2 / 2.0;
    f4 = U16_to_float(SenP.Parm3H, SenP.Parm3L);

    if (f1 > f2) f1=f2;             //limit liquid level within tank
    if (f4 > (3.0*f6)) f4=3.0*f6;   //limit hemisphere ends
    
    VolumeT = (PI*f4*(3*f6-f1)*f1*f1)/(3*f6);   //volume for 2 half spherical ends
    
    f8=sqrt((2*f6-f1)*f1)*(f1-f6) + f6*f6*acos(1-f1/f6); //area of main cly to the liquid level
    VolumeT = f8*f3 + VolumeT;
}
