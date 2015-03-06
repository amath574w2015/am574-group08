  
 --------------------------------------------
 Physics Parameters:
 -------------------
    gravity:   9.8100000000000005     
    earth_radius:   6367500.0000000000     
    coordinate_system:           1
    sea_level:   0.0000000000000000     
  
    coriolis_forcing: F
    theta_0:   0.0000000000000000     
    friction_forcing: T
    manning_coefficient:   1.4999999999999999E-002
    friction_depth:   5.0000000000000003E-002
  
    dry_tolerance:   1.0000000000000000E-003
  
 --------------------------------------------
 Refinement Control Parameters:
 ------------------------------
    wave_tolerance:   1.0000000000000000E-002
    speed_tolerance:   1000000000000.0000        1000000000000.0000        1000000000000.0000        1000000000000.0000        1000000000000.0000        1000000000000.0000     
    maxleveldeep:           3
    depthdeep:   100.00000000000000     
    Variable dt Refinement Ratios: T
 
  
 --------------------------------------------
 SETDTOPO:
 -------------
    num dtopo files =            0
  
 --------------------------------------------
 SETTOPO:
 ---------
    mtopofiles =            2
    
    /home/kasparm/Studies/ConservationLawsAndHyperbolicEquaitons/am574-group08/dambreak/domain_Zero.tt1                                                   
   itopotype =            1
   minlevel, maxlevel =            1           1
   tlow, thi =    0.0000000000000000        10000000000.000000     
   mx =          830   x = (   0.0000000000000000      ,   16.600000000000001      )
   my =           30   y = (   0.0000000000000000      ,  0.59999999999999998      )
   dx, dy (meters/degrees) =    2.0024125452352232E-002   2.0689655172413793E-002
    
    /home/kasparm/Studies/ConservationLawsAndHyperbolicEquaitons/am574-group08/dambreak/columnCylinder.tt1                                                
   itopotype =            1
   minlevel, maxlevel =            1           1
   tlow, thi =    0.0000000000000000        10000000000.000000     
   mx =         1660   x = (   11.039999999999999      ,   11.160000000000000      )
   my =           60   y = (  0.23999999999999999      ,  0.35999999999999999      )
   dx, dy (meters/degrees) =    7.2332730560579261E-005   2.0338983050847458E-003
  
   Ranking of topography files  finest to coarsest:            2           1
  
  
 --------------------------------------------
 SETQINIT:
 -------------
   qinit_type = 0, no perturbation
