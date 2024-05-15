'''Module for ntupling.'''

import uproot

import copy
import os
import pyslha
import numpy as np

import structlog
log = structlog.get_logger()
structlog.stdlib.recreate_defaults()  # so we have logger names

import Run3ModelGen.csvReader as csvReader

softsusy_blocks={
    'MINPAR':  {3: "tanb_min"},
    'EXTPAR':  {
         1   : "M_1",
         2   : "M_2",             
         3   : "M_3",             
        11   : "At",              
        12   : "Ab",              
        13   : "Atau",            
        23   : "mu",
        25   : "tanb_ext",
        26   : "mA",        
        31   : "meL",             
        32   : "mmuL",            
        33   : "mtauL",           
        34   : "meR",             
        35   : "mmuR",           
        36   : "mtauR",           
        41   : "mqL1",            
        42   : "mqL2",            
        43   : "mqL3",            
        44   : "muR",            
        45   : "mcR",            
        46   : "mtR",            
        47   : "mdR",            
        48   : "msR",            
        49   : "mbR"},
    'MASS': {
        24    : "m_W",
        25    : "m_h",
        35    : "m_H",
        36    : "m_A",
        37    : "m_Hp",
#         5    : "m_b",
   1000001    : "m_d_L",
   2000001    : "m_d_R",
   1000002    : "m_u_L",
   2000002    : "m_u_R",
   1000003    : "m_s_L",
   2000003    : "m_s_R",
   1000004    : "m_c_L",
   2000004    : "m_c_R",
   1000005    : "m_b_1",
   2000005    : "m_b_2",
   1000006    : "m_t_1",
   2000006    : "m_t_2",
   1000011    : "m_e_L",
   2000011    : "m_e_R",
   1000012    : "m_nu_eL",
   1000013    : "m_mu_L",
   2000013    : "m_mu_R",
   1000014    : "m_nu_muL",
   1000015    : "m_tau_1",
   2000015    : "m_tau_2",
   1000016    : "m_nu_tauL",
   1000021    : "m_gl",
   1000022    : "m_chi_10",
   1000023    : "m_chi_20",
   1000025    : "m_chi_30",
   1000035    : "m_chi_40",
   1000024    : "m_chi_1p",
   1000037    : "m_chi_2p",
   1000039    : "m_G",
        },
    "NMIX": {
  (1 , 1   ): "N_11",
  (1 , 2   ): "N_12",
  (1 , 3   ): "N_13",
  (1 , 4   ): "N_14",
  (2 , 1   ): "N_21",
  (2 , 2   ): "N_22",
  (2 , 3   ): "N_23",
  (2 , 4   ): "N_24",
  (3 , 1   ): "N_31",
  (3 , 2   ): "N_32",
  (3 , 3   ): "N_33",
  (3 , 4   ): "N_34",
  (4 , 1   ): "N_41",
  (4 , 2   ): "N_42",
  (4 , 3   ): "N_43",
  (4 , 4   ): "N_44",
  },
    'UMIX': { 
  (1 , 1   ): "U_11",
  (1 , 2   ): "U_12",
  (2 , 1   ): "U_21",
  (2 , 2   ): "U_22",
  },
    'VMIX': { 
  (1 , 1   ): "V_11",
  (1 , 2   ): "V_12",
  (2 , 1   ): "V_21",
  (2 , 2   ): "V_22",
  },
    'STOPMIX': { (1,1): "cos_t"},
    'SBOTMIX': { (1,1): "cos_b"},
    'STAUMIX': { (1,1): "cos_tau"},
    
    }

feynhiggs_blocks = {
    'MASS': {25:"m_h"},
    'DMASS' : {25:"Delta_m_h"},
}

feynhiggs_Wmass_blocks = {
    'PRECOBS': {3:"m_w_mssm",
                4:"m_w_sm",  },
}

spheno_blocks = copy.deepcopy(softsusy_blocks)
spheno_blocks['SPHENOLOWENERGY']={1: 'BR_b_to_sgamma',
                                  8: 'BR_Bs_to_mumu',
                                  10: 'BR_Bu_to_taunu',
                                  11: 'BR_Bu_to_taunu_dev_by_SM',
                                  21: 'gmuon',
                                  26: 'BR_mu_to_egamma',
                                  27: 'BR_tau_to_egamma',
                                  28: 'BR_tau_to_mugamma',
                                  29: 'BR_mu_to_3e',
                                  30: 'BR_tau_to_3e',
                                  31: 'BR_tau_to_3mu',
                                  39: 'deltarho',
                                  }

softsusy_decays={ 1000021: #gluino
         [ (1000001,),
           (1000002,),
           (1000003,),
           (1000004,),
           (2000001,),
           (2000002,),
           (2000003,),
           (2000004,),
           (1000005,),
           (1000006,),
           (1000012,), #nu_e_L
           (1000014,), #nu_mu_L
           (1000016,), #nu_tau_L
           (1000039,), #gravitino
           (21,), #g
           ],
         1000006: #stop_1
         [ (1000022,6,), #chi_10 t
           (1000022,5,24), #chi_10 b
           (1000022,5,), #chi_10 b
           (1000022,4,), #chi_10 c
           (1000022,), #chi_10
           (1000023,), #chi_20
           (1000025,), #chi_30
           (1000035,), #chi_40
           (1000024,5,), #chi_1+ b
           (1000024,), #chi_1+
           (1000037,), #chi_2+
           (1000021,), #gluino
           (1000011,), #e_L
           (1000012,), #nu_e_L
           (1000013,), #mu_L
           (1000014,), #nu_mu_L
           (1000015,), #tau_L
           (1000016,), #nu_tau_L
           (1000039,), #gravitino
           ],
         1000005: #sbottom_1
         [ (1000022,5,), #chi_10 b
           (1000022,), #chi_10
           (1000023,), #chi_20
           (1000025,), #chi_30
           (1000035,), #chi_40
           (1000024,6), #chi_1+ t
           (1000024,), #chi_1+
           (1000037,), #chi_2+
           (1000021,), #gluino
           (1000011,), #e_L
           (1000012,), #nu_e_L
           (1000013,), #mu_L
           (1000014,), #nu_mu_L
           (1000015,), #tau_L
           (1000016,), #nu_tau_L
           (1000039,), #gravitino
           ],
         2000006: #stop_2
         [ (1000022,6,), #chi_10 t
           (1000022,), #chi_10
           (1000023,), #chi_20
           (1000025,), #chi_30
           (1000035,), #chi_40
           (1000024,5,), #chi_1+ b
           (1000024,), #chi_1+
           (1000037,), #chi_2+
           (1000021,), #gluino
           (1000039,), #gravitino
           ],
         2000005: #sbottom_2
         [ (1000022,5,), #chi_10 b
           (1000022,), #chi_10
           (1000023,), #chi_20
           (1000025,), #chi_30
           (1000035,), #chi_40
           (1000024,6), #chi_1+ t
           (1000024,), #chi_1+
           (1000037,), #chi_2+
           (1000021,), #gluino
           (1000039,), #gravitino
           ],
         1000001: [(1000022,), #chi_10
                   (1000023,), #chi_20
                   (1000025,), #chi_30
                   (1000035,), #chi_40
                   (1000024,), #chi_1+
                   (1000037,), #chi_2+
                   (1000021,), #gluino  
                   (1000039,), #gravitino 
                   ],
         2000001: [(1000022,), #chi_10
                   (1000023,), #chi_20
                   (1000025,), #chi_30
                   (1000035,), #chi_40
                   (1000024,), #chi_1+
                   (1000037,), #chi_2+
                   (1000021,), #gluino 
                   (1000039,), #gravitino  
                   ],
         1000002: [(1000022,), #chi_10
                   (1000023,), #chi_20
                   (1000025,), #chi_30
                   (1000035,), #chi_40
                   (1000024,), #chi_1+
                   (1000037,), #chi_2+
                   (1000021,), #gluino   
                   (1000039,), #gravitino
                   ],
         2000002: [(1000022,), #chi_10
                   (1000023,), #chi_20
                   (1000025,), #chi_30
                   (1000035,), #chi_40
                   (1000024,), #chi_1+
                   (1000037,), #chi_2+
                   (1000021,), #gluino   
                   (1000039,), #gravitino
                   ],
         1000003: [],
         2000003: [],
         1000004: [],
         2000004: [], 
         1000011: # LH selectron
	[ (1000022,11), # chi_10, ele
	  (1000023,11), # chi_20, ele
	  (1000025,11), # chi_30, ele
	  (1000035,11), # chi_40, ele
	  (1000024,12), # chi_1p, nu_ele
	  (1000037,12), # chi_2p, nu_ele
      (1000039,), #gravitino
	  (11,),
	  (12,),
	],
	1000012: # LH ele sneutrino
	[
	  (1000022,12), # chi_10, nu_e
	  (1000023,12), # chi_20, nu_e
	  (1000025,12), # chi_30, nu_e
	  (1000035,12), # chi_40, nu_e
	  (1000024,11), # chi_1p, ele
	  (1000037,11), # chi_2p, ele
      (1000039,), #gravitino
	  (12,),
	  (11,),
	],
         2000011: # RH selectron
	[ (1000022,11), # chi_10, ele
	  (1000023,11), # chi_20, ele
	  (1000025,11), # chi_30, ele
	  (1000035,11), # chi_40, ele
	  (1000024,12), # chi_1p, nu_ele
	  (1000037,12), # chi_2p, nu_ele
      (1000039,), #gravitino
	  (11,),
	  (12,),
	],
         1000013: # LH smuon
	[ (1000022,13), # chi_10, mu
	  (1000023,13), # chi_20, mu
	  (1000025,13), # chi_30, mu
	  (1000035,13), # chi_40, mu
	  (1000024,14), # chi_1p, nu_mu
	  (1000037,14), # chi_2p, nu_mu
      (1000039,), #gravitino
	  (13,),
	  (14,),
	],
	1000014: # LH mu sneutrino
	[
	  (1000022,14), # chi_10, nu_mu
	  (1000023,14), # chi_20, nu_mu
	  (1000025,14), # chi_30, nu_mu
	  (1000035,14), # chi_40, nu_mu
	  (1000024,13), # chi_1p, mu
	  (1000037,13), # chi_2p, mu
      (1000039,), #gravitino
	  (13,),
	  (14,),
	],
         2000013: # RH smuon
	[ (1000022,13), # chi_10, mu
	  (1000023,13), # chi_20, mu
	  (1000025,13), # chi_30, mu
	  (1000035,13), # chi_40, mu
	  (1000024,14), # chi_1p, nu_mu
	  (1000037,14), # chi_2p, nu_mu
      (1000039,), #gravitino
	  (13,),
	  (14,),
	],
         1000015: # LH stau
	[ (1000022,15), # chi_10, tau
	  (1000023,15), # chi_20, tau
	  (1000025,15), # chi_30, tau
	  (1000035,15), # chi_40, tau
	  (1000024,16), # chi_1p, nu_tau
	  (1000037,16), # chi_2p, nu_tau
      (1000039,), #gravitino
	  (15,),
	  (16,),
	],
	1000016: # LH tau sneutrino
	[
	  (1000022,16), # chi_10, nu_tau
	  (1000023,16), # chi_20, nu_tau
	  (1000025,16), # chi_30, nu_tau
	  (1000035,16), # chi_40, nu_tau
	  (1000024,15), # chi_1p, tau
	  (1000037,15), # chi_2p, tau
      (1000039,), #gravitino
	  (15,),
	  (16,),
	],
         2000015: # RH stau
	[ (1000022,15), # chi_10, tau
	  (1000023,15), # chi_20, tau
	  (1000025,15), # chi_30, tau
	  (1000035,15), # chi_40, tau
	  (1000024,16), # chi_1p, nu_tau
	  (1000037,16), # chi_2p, nu_tau
      (1000039,), #gravitino
	  (15,),
	  (16,),
	],
         1000022: #chi_10
         [ (1000039, 22), #G, gamma
           (1000039, 23), #G, Z
           (1000039, 25), #G, h
           (1000011,), #e_L
           (1000012,), #nu_e_L
           (1000013,), #mu_L
           (1000014,), #nu_mu_L
           (1000015,), #tau_L
           (1000016,), #nu_tau_L
           ],
         1000023: #chi_20
         [ (1000022, 23), #chi_10,Z
           (1000022, 25), #chi_10,h
           (1000022, ), #chi_10,
           (1000024, 24), #chi_1+,W
           (1000024, ), #chi_1+,W
           (1000037, 24), #chi_2+,W
           (1000037, ), #chi_2+,W
           (1000039,),  # gravitino
           ],
         1000025: #chi_30
         [ (1000022, 23), #chi_10,Z
           (1000022, 25), #chi_10,h
           (1000022, ),   #chi_10,
           (1000023, 23), #chi_20,Z
           (1000023, 25), #chi_20,h
           (1000023, ),    #chi_20,
           (1000024, 24), #chi_1+,W
           (1000024, ), #chi_1+,
           (1000037, 24), #chi_2+,W
           (1000037, ), #chi_2+,
           (1000039,),  # gravitino
           ],
         1000035: #chi_40
         [ (1000022, 23), #chi_10,Z
           (1000022, 25), #chi_10,h
           (1000022, ), #chi_10,
           (1000023, 23), #chi_20,Z
           (1000023, 25), #chi_20,h
           (1000023, ), #chi_20,
           (1000025, 23), #chi_30,Z
           (1000025, 25), #chi_30,h
           (1000025, ), #chi_30,
           (1000024, 24), #chi_1+,W
           (1000024, ), #chi_1+,
           (1000037, 24), #chi_2+,W
           (1000037, ), #chi_2+,
           (1000039,),  # gravitino
           ],
         1000024: #chi_1+
         [ (1000022,),  # chi_10
           (1000023,),  # chi_20
           (1000025,),  # chi_30
           (1000039,),  # gravitino
           ],
         1000037: #chi_2+
         [ (1000022,),  # chi_10
           (1000023,),  # chi_20
           (1000025,),  # chi_30
           (1000024,23), #chi_1+,Z
           (1000024,25), #chi_1+,h
           (1000024,), #chi_1+,
           (1000039,),  # gravitino
           ],
         25: #higgs
         [ (3,3),  #s
           (4,4),  #c
           (5,5),  #b
           (13,13),  #mu
           (15,15),  #tau
           (21,21),  #gluon gluon
           (23,22),  #Z gamma
           (22,22),  #gamma gamma
           (23,23),  #ZZ
           (24,24),  #WW
           (1000022,1000022), #chi0 chi0
           ],
         35: #H
         [ (3,3),  #s
           (4,4),  #c
           (5,5),  #b
           (6,6),  #t
           (13,13),  #mu
           (15,15),  #tau
           (21,21),  #gluon gluon
           (23,22),  #Z gamma
           (22,22),  #gamma gamma
           (23,25),  #Zh
           (23,23),  #ZZ
           (24,24),  #WW
           (1000022,1000022), #chi0 chi0           
           ],
         36: #A
         [ (3,3),  #s
           (4,4),  #c
           (5,5),  #b
           (6,6),  #t
           (13,13),  #mu
           (15,15),  #tau
           (21,21),  #gluon gluon
           (23,22),  #Z gamma
           (22,22),  #gamma gamma
           (23,25),  #Zh
           (23,23),  #ZZ
           (24,24),  #WW
           (1000022,1000022), #chi0 chi0       
           ],
         37: #H+
         [ (4,5),
           (15,16),
           (13,14),
           (2,5),
           (2,3),
           (4,3),
           (6,5), #top
           (24,25),
           (24,36),
           ],

      }

superiso_blocks = {
    'FOBS': { 
        (5,1)  : "BR_b_to_sgamma",
        (531,1): "BR_Bs_to_mumu",
        (521,4): "Delta0_B_to_Kshgamma",
        #(521,1): "BR_Bu_to_taunu",
        (521,2): "R_Bu_to_taunu",
        #(431,1): "BR_Ds_to_taunu",
        #(431,1): "BR_Ds_to_munu",
        #(521,1): "BR_Bp_to_D0taunu",
        (521,11): "BR_Bp_to_D0taunu_dev_by_BR_Bp_to_D0enu",
        (321,11): "BR_K_to_munu_dev_by_BR_pi_to_munu",
        (321,12): "R_mu23",
        },
    'FOBSSM': { 
        (5,1)  : "BR_b_to_sgamma_SM",
        (531,1): "BR_Bs_to_mumu_SM",
        (521,4): "Delta0_B_to_Kshgamma_SM",
        #(521,1): "BR_Bu_to_taunu_SM",
        (521,2): "R_Bu_to_taunu_SM",
        #(431,1): "BR_Ds_to_taunu_SM",
        #(431,1): "BR_Ds_to_munu_SM",
        #(521,1): "BR_Bp_to_D0taunu_SM",
        (521,11): "BR_Bp_to_D0taunu_SM_dev_by_BR_Bp_to_D0enu_SM",
        (321,11): "BR_K_to_munu_SM_dev_by_BR_pi_to_munu_SM",
        (321,12): "R_mu23_SM",
        }
    }

input_blocks = {
    'EXTPAR':  {
         1   : "M_1",
         2   : "M_2",
         3   : "M_3",
        11   : "At",
        12   : "Ab",
        13   : "Atau",
        23   : "mu",
        25   : "tanb",
        26   : "mA",
        31   : "meL",
        32   : "mmuL",
        33   : "mtauL",
        34   : "meR",
        35   : "mmuR",
        36   : "mtauR",
        41   : "mqL1",
        42   : "mqL2",
        43   : "mqL3",
        44   : "muR",
        45   : "mcR",
        46   : "mtR",
        47   : "mdR",
        48   : "msR",
        49   : "mbR"},
}

gm2calc_blocks = {
    'GM2CALCOUTPUT' : {
        0 : "gmuon",
        1 : "Delta_gmuon"
    }
}

PDG={
    2: "d",
    3: "s",
    4: "c",
    5: "b",
    6: "t",
    11: "ele",
    12: "nu_ele",
    13: "mu",
    14: "nu_mu",
    15: "tau",
    16: "nu_tau",
    21: "g",
    22: "gam",
    23: "Z",
    24: "W",
    25: "h",
    35: "H",
    36: "A",
    37: "Hp",
    1000001: "d_L",
    2000001: "d_R",
    1000002: "u_L",
    2000002: "u_R",
    1000003: "s_L",
    2000003: "s_R",
    1000004: "c_L",
    2000004: "c_R",
    1000005: "b_1",
    1000006: "t_1",
    2000005: "b_2",
    2000006: "t_2",
    1000011: "e_L",
    1000012: "nu_e_L",
    2000011: "e_R",
    1000013: "mu_L",
    1000014: "nu_mu_L",
    2000013: "mu_R",
    1000015: "tau_1",
    1000016: "nu_tau_1",
    2000015: "tau_2",
    1000021: "gl",
    1000022: "chi_10",
    1000023    : "chi_20",
    1000025    : "chi_30",
    1000035    : "chi_40",
    1000024    : "chi_1p",
    1000037    : "chi_2p",
    1000039    : "gravitino",
   }

def readSLHA(name: str, data: dict, prefix: str, blocks: dict, decays: dict, needsMass: bool, isGMSB: bool) -> None:
    '''Function for reading .slha file into data dict. This needs separate handling to capture some exceptions etc.'''
    
    # Read raw text of file to catch errors
    with open(name) as rawfile: rawtext=rawfile.read()
    
    skip=False
    if "problem:" in rawtext:
        log.warning(f"problem in {name}")
        skip=True
    if "-inf" in rawtext:
        log.warning(f"-inf ERROR! in {name}")
        skip=True
        
    foundmassblock = False
    for line in rawtext.upper().split('\n'):
        if not "WARNING" in line and "BLOCK MASS" in line:
            foundmassblock = True
    if not foundmassblock and needsMass:
        skip=True

    #setting up potential errors:
    data["Maywarning"]=0
    data[prefix+"err_tachyon"]=0
    data[prefix+"err_tachyon_sbottom"]=0
    data[prefix+"err_tachyon_stop"]=0
    data[prefix+"err_tachyon_snutau"]=0
    data[prefix+"err_tachyon_A0"]=0
    data[prefix+"err_tachyon_stau"]=0
    data[prefix+"err_tachyon_hpm"]=0
    data[prefix+"err_tachyon_m3sq_problem"]=0
    data[prefix+"err_tachyon_other"]=0
    data[prefix+"err_m3sq_problem"]=0
    data[prefix+"err_stop_LSP"]=0
    data[prefix+"err_higgs_potential"]=0
    data[prefix+"err_num"]=0
    data[prefix+"err_other"]=0

    # If we found an error, dive deeper into what's wrong:
    if skip:
        errfound=False
        if "May" in rawtext:
            data["Maywarning"]=1
            errfoud=True
        if "tachyon" in rawtext:
            tachfound=False
            errfound=True
            data[prefix+"err_tachyon"]=1
            if "sbottom is tree level tachyon" in rawtext or "sbottom tachyon" in rawtext:
                data[prefix+"err_tachyon_sbottom"]=1
                tachfound=True
            if "stop is tree level tachyon" in rawtext or "stop tachyon" in rawtext:
                data[prefix+"err_tachyon_stop"]=1
                tachfound=True
            if "snutau is tree-level tachyon" in rawtext or "snutau tachyon" in rawtext:
                data[prefix+"err_tachyon_snutau"]=1
                tachfound=True
            if "A0 tachyon" in rawtext:
                data[prefix+"err_tachyon_A0"]=1
                tachfound=True
            if "stau tachyon" in rawtext:
                data[prefix+"err_tachyon_stau"]=1
                tachfound=True
            if "hpm tachyon" in rawtext:
                data[prefix+"err_tachyon_hpm"]=1
                tachfound=True
            if "m3sq-problem" in rawtext:
                data[prefix+"err_tachyon_m3sq_problem"]=1
                tachfound=True
            if not tachfound:
                data[prefix+"err_tachyon_other"]=1
        if "m3sq-problem" in rawtext:#Tachyon error??
            data[prefix+"err_m3sq_problem"]=1
            errfound=True
        if "stop LSP" in rawtext:
            errfound=True
            data[prefix+"err_stop_LSP"]=1
        if "Higgs potential ufb" in rawtext:
            data[prefix+"err_higgs_potential"]=1
            errfound=True
        if "Numerical problemThrown" in rawtext:
            data[prefix+"err_num"]=1
            errfound=True
        if not errfound:
            data[prefix+"err_other"]=1
        return

    # Finally read the slha file and assign blocks
    results=pyslha.readSLHAFile(name,ignorenomass=True)
    BLOCKS=results.blocks
    DECAYS=results.decays
    if needsMass:
        massv = []
        qmass = []
        for pid in BLOCKS['MASS'].entries.keys():
            if pid>1000:
                massv.append([abs(BLOCKS['MASS'].entries[pid]),pid])
            if((pid>1000000 and pid<=1000006) or (pid>2000000 and pid<=2000006)):
                qmass.append([abs(BLOCKS['MASS'].entries[pid]),pid])
        data[prefix+"LSP_type"]=min(massv)[1]
        data[prefix+"LSP_mass"]=min(massv)[0]
        data[prefix+"LSQ_type"]=min(qmass)[1]
        data[prefix+"LSQ_mass"]=min(qmass)[0]

    # Loop over non-decay blocks
    for block,vars in blocks.items():
        try: slha=BLOCKS[block]
        except:
            log.warning(f"no {block} in {name}")
            #SBOT/STOPMIX blocks can be missing if FHss_m_h=NaN in previous iteration. These models are filtered with FHss_m_h!=-1.
            if "softsusy_FH" in name:
                continue
        slha=BLOCKS[block]
        for var,vName in vars.items():
            try:
                value=slha.entries[var]
                if type(value)==tuple: value=value[0]
                if np.isnan(value):
                    log.warning(f"Found NaN value for var {vName} ({var}) in block {block} for model: {name}; Saving -1.")
                    data[prefix+vName]=-1.
                else:
                    data[prefix+vName]=value
            except KeyError:
                if vName == 'm_G' and isGMSB: log.exception(f"Failed to get {vName} ({var}) in {block} for {name}")
   
    # Now loop over decays
    for part,decay in decays.items():
        if part in DECAYS:
            slha=DECAYS[part]
        else:
            class dummy:
                pass
            slha=dummy()
            slha.totalwidth=-1
            slha.decays=[]
        pName=PDG[part]
        data[prefix+'w_%s' % pName]=slha.totalwidth
        BFs=[0]*(len(decay)+1)
        for sDecay in slha.decays:
            idx=0
            ids=set([abs(id) for id in sDecay.ids])
            for mm in decay:
                match=set(mm)
                if match.issubset(ids): break
                idx+=1
            BFs[idx]+=sDecay.br
        for idx in range(len(decay)):
            finalState=[PDG[id] for id in decay[idx]]
            dName='BF_%s_to_%s' % (pName, '_'.join(finalState))
            data[prefix+dName]=BFs[idx]
        data[prefix+"BF_%s_other" % pName]=BFs[-1]
    
    # Assign extra variables if a mass block exists
    if needsMass:
        if data[prefix+"LSP_type"]==1000022:
            data[prefix+"LSP_Bino_frac"] = data[prefix+"N_11"]**2
            data[prefix+"LSP_Wino_frac"] = data[prefix+"N_12"]**2
            data[prefix+"LSP_Higgsino_frac"] = (data[prefix+"N_13"]**2+data[prefix+"N_14"]**2)
            if data[prefix+"N_11"]**2 > max(data[prefix+"N_12"]**2,data[prefix+"N_13"]**2+data[prefix+"N_14"]**2):
                data[prefix+"LSP_type"]=1  #Bino-like
            elif data[prefix+"N_12"]**2 > max(data[prefix+"N_11"]**2,data[prefix+"N_13"]**2+data[prefix+"N_14"]**2):
                data[prefix+"LSP_type"]=2  #Wino-like
            elif (data[prefix+"N_13"]**2+data[prefix+"N_14"]**2) > max(data[prefix+"N_11"]**2,data[prefix+"N_12"]**2):
                data[prefix+"LSP_type"]=3  #Higgsino-like
        
        # always calculate neutralino and chargino fractions
        data[prefix+"chi_10_Bino_frac"] = data[prefix+"N_11"]**2
        data[prefix+"chi_10_Wino_frac"] = data[prefix+"N_12"]**2
        data[prefix+"chi_10_Higgsino_frac"] = (data[prefix+"N_13"]**2+data[prefix+"N_14"]**2)
        data[prefix+"chi_20_Bino_frac"] = data[prefix+"N_21"]**2
        data[prefix+"chi_20_Wino_frac"] = data[prefix+"N_22"]**2
        data[prefix+"chi_20_Higgsino_frac"] = (data[prefix+"N_23"]**2+data[prefix+"N_24"]**2)
        data[prefix+"chi_30_Bino_frac"] = data[prefix+"N_31"]**2
        data[prefix+"chi_30_Wino_frac"] = data[prefix+"N_32"]**2
        data[prefix+"chi_30_Higgsino_frac"] = (data[prefix+"N_33"]**2+data[prefix+"N_34"]**2)
        data[prefix+"chi_40_Bino_frac"] = data[prefix+"N_41"]**2
        data[prefix+"chi_40_Wino_frac"] = data[prefix+"N_42"]**2
        data[prefix+"chi_40_Higgsino_frac"] = (data[prefix+"N_43"]**2+data[prefix+"N_44"]**2)

        data[prefix+"chi_1p_Wino_frac"] = data[prefix+"V_11"]**2
        data[prefix+"chi_1p_Higgsino_frac"] = data[prefix+"V_12"]**2
        data[prefix+"chi_2p_Wino_frac"] = data[prefix+"V_21"]**2
        data[prefix+"chi_2p_Higgsino_frac"] = data[prefix+"V_22"]**2
        data[prefix+"chi_1m_Wino_frac"] = data[prefix+"U_11"]**2
        data[prefix+"chi_1m_Higgsino_frac"] = data[prefix+"U_12"]**2
        data[prefix+"chi_2m_Wino_frac"] = data[prefix+"U_21"]**2
        data[prefix+"chi_2m_Higgsino_frac"] = data[prefix+"U_22"]**2
        
    return None

def readModel(inputDefinitions: list[tuple], num: int, scanDir: str, outName: str, isGMSB: bool) -> dict:
    '''Function for reading model files, looping over input definitions. Returns model info in dict.'''
    data={}
    #data['model']=num
    data['model']=int(outName.split('.')[-2]+'00000')+num

    # inputDefinitions = [
    # # directory, filetype, prefix, slha blocks, slha decays)
    # ("softsusy/", ".slha", "SS_", softsusy_blocks, softsusy_decays,True),
    # ("input/", ".slha", "IN_", input_blocks, {}, False),
    # ("SPheno/", ".slha", "SP_", spheno_blocks, softsusy_decays, True),
    # # ("feynhiggs_SP/spheno.out.fh-001","FHsp_",feynhiggs_blocks,softsusy_decays,False),
    # # ("spheno_FH/spheno_FH.out","SPfh_",spheno_blocks,softsusy_decays,True),
    # ("micromegas/", ".csv", "", None, None, None),
    # ("superiso/", ".flha", "SI_", superiso_blocks, {} , False),
    # ("gm2calc/", ".slha", "GM2_", gm2calc_blocks, {}, False),
    # # ("feynhiggs_SP_FHsp/spheno_FH.out.fh-001","FHspfh_",feynhiggs_Wmass_blocks,{},False),
    # ("evade/", ".tsv", "EV_", None, None, None)
    # ]
    # Loop over inputDefinitions:
    for inputDef in inputDefinitions:
        (directory, filetype, prefix, blocks, decays, needsMass) = inputDef
        
        fileName=os.path.join(scanDir,directory)+str(num)+filetype

        # read file using csv reader or readSLHA depending on inputDef
        if not os.access(fileName,os.R_OK): continue
        if inputDef[3] is not None: 
            readSLHA(fileName, data, prefix, blocks, decays, needsMass, isGMSB)
        else: 
            myData=csvReader.read(fileName)
            prefix = inputDef[2]
            for col in myData:
                for row in myData[col]:
                    try:
                        val=float(myData[col][row])
                        # Small fix for evade: filter out row = 0
                        if row == "0":
                            data[prefix+col]=val
                        else:
                            data[prefix+col+"_"+row.replace(':','_').replace("-","_")]=val
                    except ValueError:
                        pass
    return data

def mkntuple(steps: dict, scan_dir: str, num_models: int, isGMSB: bool) -> None:
    '''Function for generating ntuple for directory scan_dir with num_models using uproot.'''
    log.info(f"Will make NTuple for: {scan_dir}, with {num_models} models")
    
    outName = f"{scan_dir}/example.0.0.root"
    file = uproot.recreate(outName)
    
    # Build inputDefinitions from steps dict
    inputDefinitions = []
    for step in steps:
        if "input" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".slha", "IN_", input_blocks, {}, False), ]
        elif "softsusy" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".slha", "SS_", softsusy_blocks, softsusy_decays,True),]
        elif "SPheno" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".slha", "SP_", spheno_blocks, softsusy_decays, True), ]
        elif "micromegas" in step['name']:
            print(f"{step['output_dir']}/")
            inputDefinitions += [ (f"{step['output_dir']}/", ".csv", "", None, None, None), ]
        elif "superiso" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".flha", "SI_", superiso_blocks, {}, False), ]
        elif "gm2calc" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".slha", "GM2_", gm2calc_blocks, {}, False), ]
        elif "evade" in step['name']:
            inputDefinitions += [ (f"{step['output_dir']}/", ".tsv", "EV_", None, None, None) ]
        else:
            raise KeyError(f"Step name {step['name']} not recognised!")
    
    treedict = {}
    # Loop over models and keys and treedict accordingly
    for modid in range(num_models):
        if modid%100==0: log.info(f"\tFilling values for model: {modid}")
        
        fileData=readModel(inputDefinitions, modid, scan_dir, outName, isGMSB)
        
        for key in fileData:
            value = fileData[key]
            # Initialise empty array with -1 if the key is not yet included
            if key not in treedict: treedict[key] = np.full(num_models, -1.)
            
            # Save value for key at specific modid index
            treedict[key][modid] = value
    
    # Save treedict in file using uproot
    log.info(f"Saving NTuple in {outName} ...")
    file["susy"] = treedict
