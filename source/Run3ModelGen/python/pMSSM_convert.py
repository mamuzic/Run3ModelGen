'''Module for converting .slha file into input used by EVADE.'''

import numpy as np
import pandas as pd
import sys
import pyslha

"""
def index():
    from pandaslha import slhakey_to_index
    blocks = ['MINPAR'] + ['SMINPUTS'] * 7 + ['GAUGE'] * 4 + ['HMIX'] * 9 + [
        'MSOFT'
    ] * 6 + ['YU'] * 10 + ['YD'] * 10 + ['YE'] * 10 + ['TU'] * 10 + [
        'TD'
    ] * 10 + ['TE'] * 10 + ['AU'] * 10 + ['AD'] * 10 + ['AE'] * 10 + [
        'MSQ2'
    ] * 10 + ['MSL2'] * 10 + ['MSD2'] * 10 + ['MSU2'] * 10 + ['MSE2'] * 10

    keys = [
        3, 1, 2, 3, 4, 5, 6, 7, 'Q', 1, 2, 3, 'Q', 1, 2, 3, 4, 10, 101, 102,
        103, 'Q', 1, 2, 3, 21, 22
    ] + [
        'Q', (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2),
        (3, 3)
    ] * 14

    return [slhakey_to_index(x) for x in zip(blocks, keys)]
"""

def createpoint(tbeta,
                mu,
                mAsq=None,
                mHcsq=None,
                Tu3=None,
                Td3=None,
                Te3=None,
                At=None,
                Ab=None,
                Al=None,
                msusy=None,
                M1=None,
                M2=None,
                M3=None,
                msq2=None,
                msl2=None,
                msd2=None,
                msu2=None,
                mse2=None):
    import math as m
    if msusy == None:
        msusy = (msq2[2] * msu2[2])**(1 / 4.)
    if M1 == None:
        M1 = msusy
    if M2 == None:
        M2 = msusy
    if M3 == None:
        M3 = msusy
    if msq2 == None:
        msq2 = [msusy**2] * 3
    if msl2 == None:
        msl2 = [msusy**2] * 3
    if msd2 == None:
        msd2 = [msusy**2] * 3
    if msu2 == None:
        msu2 = [msusy**2] * 3
    if mse2 == None:
        mse2 = [msusy**2] * 3
    if (Tu3 == None and At == None) or (Tu3 and At):
        raise TypeError("You have to specify either Tu3 or At.")
    if (Td3 == None and Ab == None) or (Td3 and Ab):
        raise TypeError("You have to specify either Td3 or Ab.")
    if (Te3 == None and Al == None) or (Te3 and Al):
        raise TypeError("You have to specify either Te3 or Al.")
    if (mAsq == None and mHcsq == None) or (mAsq and mHcsq):
        raise TypeError("You have to specify either mAsq or mHcsq.")

    beta = np.arctan(tbeta)
    v_ew = 246.21845810181634
    Mt = 173.1
    mbmb = 4.18
    Mtau = 1.776
    Mz = 91.1876
    asMz = 0.119
    g1 = 3.61519199E-01
    g2 = 6.36751450E-01
    g3 = m.sqrt(high_scale_aS(msusy, asmZ=asMz, mZ=Mz, mt=Mt) * 4 * m.pi)
    mtmsusy = high_scale_mT(msusy, mtOS=Mt)
    mbmsusy = high_scale_mB(msusy, mbmb=mbmb, mt=Mt, asmZ=asMz, mZ=Mz)

    Yt = mtmsusy / v_ew * np.sqrt(2) / np.sin(beta)
    Yb = mbmsusy / v_ew * np.sqrt(2) / np.cos(beta)
    Ytau = Mtau / v_ew * np.sqrt(2) / np.cos(beta)

    if Tu3 == None:
        Tu3 = At * Yt
    if At == None:
        At = Tu3 / Yt
    if Td3 == None:
        Td3 = Ab * Yb
    if Ab == None:
        Ab = Td3 / Yb
    if Te3 == None:
        Te3 = Al * Ytau
    if Al == None:
        Al = Te3 / Ytau
    if mAsq == None:
        mAsq = mHcsq - 80.385**2

    return np.array([
        # MINPAR
        tbeta,
        # SMINPUTS
        1.27931489E+02,  # alpha_em^-1(MZ)^MSbar
        1.16639000E-05,  # G_mu [GeV^-2]
        asMz,  # alpha_s(MZ)^MSbar
        Mz,  # m_Z(pole)
        mbmb,  # m_b(m_b), MSbar
        Mt,  # m_t(pole)
        Mtau,  # m_tau(pole)
        # GAUGE
        msusy,
        g1,  # g1
        g2,  # g2
        g3,  # g3
        # HMIX
        msusy,
        mu,
        tbeta,
        v_ew,
        mAsq,
        beta,
        mAsq * np.sin(beta) * np.cos(beta),
        np.cos(beta) * v_ew,
        np.sin(beta) * v_ew,
        # MSOFT
        msusy,
        M1,
        M2,
        M3,
        (4 * (-2 * mu**2 + mAsq) - np.cos(2 * beta) * (
            (g1**2 + g2**2) * v_ew**2 + 4 * mAsq)) / 8.,
        (4 * (-2 * mu**2 + mAsq) + np.cos(2 * beta) * (
            (g1**2 + g2**2) * v_ew**2 + 4 * mAsq)) / 8.,

        # YU
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Yt,
        # YD
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Yb,
        # YE
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Ytau,
        # TU
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Tu3,
        # TD
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Td3,
        # TE
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Te3,
        # AU
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        At,
        # AD
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Ab,
        # AE
        msusy,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        0.,
        Al,
        # MSQ2
        msusy,
        msq2[0],
        0.,
        0.,
        0.,
        msq2[1],
        0.,
        0.,
        0.,
        msq2[2],
        # MSL2
        msusy,
        msl2[0],
        0.,
        0.,
        0.,
        msl2[1],
        0.,
        0.,
        0.,
        msl2[2],
        # MSD2
        msusy,
        msd2[0],
        0.,
        0.,
        0.,
        msd2[1],
        0.,
        0.,
        0.,
        msd2[2],
        # MSU2
        msusy,
        msu2[0],
        0.,
        0.,
        0.,
        msu2[1],
        0.,
        0.,
        0.,
        msu2[2],
        # MSE2
        msusy,
        mse2[0],
        0.,
        0.,
        0.,
        mse2[1],
        0.,
        0.,
        0.,
        mse2[2]
    ])


#%%
def high_scale_mB(scale, mbmb=4.18, mt=173.1, asmZ=0.119, mZ=91.1876):
    import rundec
    crd = rundec.CRunDec()
    dec = crd.nfMmu
    dec.nf = 6
    dec.Mth = mt
    dec.muth = mt
    return crd.mL2mH(mbmb, crd.AlphasExact(asmZ, mZ, mbmb, 5, 4), mbmb, dec,
                     scale, 4)


def high_scale_mT(scale, mtOS=173.1, asmZ=0.1181, mZ=91.1876):
    import rundec
    crd = rundec.CRunDec()
    as6Mt = high_scale_aS(mtOS, mt=mtOS, asmZ=asmZ, mZ=mZ)
    mtMt = crd.mOS2mMS(mtOS, crd.mq, as6Mt, mtOS, 3)
    return crd.mMS2mMS(mtMt, as6Mt, high_scale_aS(scale, mt=mtOS), 6, 4)


def high_scale_aS(scale, asmZ=0.1181, mZ=91.1876, mt=173.1):
    import rundec
    crd = rundec.CRunDec()
    dec = crd.nfMmu
    dec.nf = 6
    dec.Mth = mt
    dec.muth = mt
    return crd.AlL2AlH(asmZ, mZ, dec, scale, 4)


#%%
def tree_masssq(s):
    """
    Calculates the masses squared at the ew minimum. These are not normalized correctly! Only use to check for positivity.
    """
    import scipy.sparse
    import scipy.sparse.linalg
    import math as m
    massM = scipy.sparse.coo_matrix(
        ((s['HMIX_1']**2 - (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (3 * s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (3 * s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_22'],
          -(s['GAUGE_1']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 - (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_22'],
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          -(s['GAUGE_1']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 + (3 * s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (3 * s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_21'],
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 + (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_21'],
          s['HMIX_1']**2 - (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_22'],
          (s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. +
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 - (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_22'],
          -(s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          (s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. +
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 + (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_21'],
          -(s['GAUGE_2']**2 * s['HMIX_102'] * s['HMIX_103']) / 4. -
          (s['HMIX_4'] * s['HMIX_102'] * s['HMIX_103']) / s['HMIX_3']**2,
          s['HMIX_1']**2 + (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSOFT_21'],
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. -
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
          (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.,
          (s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. -
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
          (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.,
          (s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2),
          (s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2),
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 6. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 6. + s['MSU2_3_3'] +
          (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.,
          (s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2),
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 6. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 6. + s['MSU2_3_3'] +
          (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.,
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
          (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
          (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2),
          (s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 12. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 12. + s['MSD2_3_3'] +
          (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 12. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 12. + s['MSD2_3_3'] +
          (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.,
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSL2_3_3'] +
          (s['HMIX_102']**2 * s['YE_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TE_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YE_3_3']) / m.sqrt(2),
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSL2_3_3'] +
          (s['HMIX_102']**2 * s['YE_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TE_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YE_3_3']) / m.sqrt(2),
          (s['HMIX_102'] * s['TE_3_3']) / m.sqrt(2) -
          (s['HMIX_1'] * s['HMIX_103'] * s['YE_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 4. +
          (s['GAUGE_1']**2 * s['HMIX_103']**2) / 4. + s['MSE2_3_3'] + (
              s['HMIX_102']**2 * s['YE_3_3']**2) / 2.,
          (s['HMIX_102'] * s['TE_3_3']) / m.sqrt(2) - (
              s['HMIX_1'] * s['HMIX_103'] * s['YE_3_3']) / m.sqrt(2),
          -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 4. + (
              s['GAUGE_1']**2 * s['HMIX_103']**2) / 4. + s['MSE2_3_3'] + (
                  s['HMIX_102']**2 * s['YE_3_3']**2) / 2.,
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. + (
              s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. - (
                  s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. - (
                      s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSL2_3_3'],
          (s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. +
          (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. - (
              s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. - (
                  s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSL2_3_3']),
         ((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11,
           11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19,
           20, 20, 21, 22),
          (1, 3, 2, 4, 1, 3, 2, 4, 5, 7, 6, 8, 5, 7, 6, 8, 9, 11, 10, 12, 9,
           11, 10, 12, 13, 15, 14, 16, 13, 15, 14, 16, 17, 19, 18, 20, 17, 19,
           18, 20, 21, 22)))).tocsr()
    eigvals = scipy.sparse.linalg.eigsh(massM, k=22, return_eigenvectors=False)
    return eigvals


def check_tree_masssq(s):
    from numpy import min
    if 'stable' in list(s):
        if s['stable'] == False:
            return s['stable']
    return min(tree_masssq(s)) > -1e-3


def stop_masssq(s):
    from numpy.linalg import eigvalsh
    import math as m
    return eigvalsh([[
        -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. +
        (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
        (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. -
        (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
        (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.,
        (s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
        (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2)
    ], [(s['HMIX_103'] * s['TU_3_3']) / m.sqrt(2) -
        (s['HMIX_1'] * s['HMIX_102'] * s['YU_3_3']) / m.sqrt(2),
        (s['GAUGE_1']**2 * s['HMIX_102']**2) / 6. -
        (s['GAUGE_1']**2 * s['HMIX_103']**2) / 6. + s['MSU2_3_3'] +
        (s['HMIX_103']**2 * s['YU_3_3']**2) / 2.]])


def sbot_masssq(s):
    from numpy.linalg import eigvalsh
    import math as m
    return eigvalsh([[
        -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 24. -
        (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. +
        (s['GAUGE_1']**2 * s['HMIX_103']**2) / 24. +
        (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSQ2_3_3'] +
        (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.,
        (s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
        (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2)
    ], [(s['HMIX_102'] * s['TD_3_3']) / m.sqrt(2) -
        (s['HMIX_1'] * s['HMIX_103'] * s['YD_3_3']) / m.sqrt(2),
        -(s['GAUGE_1']**2 * s['HMIX_102']**2) / 12. +
        (s['GAUGE_1']**2 * s['HMIX_103']**2) / 12. + s['MSD2_3_3'] +
        (s['HMIX_102']**2 * s['YD_3_3']**2) / 2.]])


def stau_masssq_and_mixing(s):
    from math import sqrt, atan
    L = ((s['GAUGE_1']**2 * s['HMIX_102']**2) / 8. -
         (s['GAUGE_2']**2 * s['HMIX_102']**2) / 8. -
         (s['GAUGE_1']**2 * s['HMIX_103']**2) / 8. +
         (s['GAUGE_2']**2 * s['HMIX_103']**2) / 8. + s['MSL2_3_3'] +
         (s['HMIX_102']**2 * s['YE_3_3']**2) / 2.)
    R = (-(s['GAUGE_1']**2 * s['HMIX_102']**2) / 4. +
         (s['GAUGE_1']**2 * s['HMIX_103']**2) / 4. + s['MSE2_3_3'] +
         (s['HMIX_102']**2 * s['YE_3_3']**2) / 2.)
    eps = ((s['HMIX_102'] * s['TE_3_3']) / sqrt(2) -
           (s['HMIX_1'] * s['HMIX_103'] * s['YE_3_3']) / sqrt(2))
    m1sq = 1 / 2. * (L + R) + 1 / 2. * sqrt((L - R)**2 + 4 * eps**2)
    m2sq = 1 / 2. * (L + R) - 1 / 2. * sqrt((L - R)**2 + 4 * eps**2)
    phi = atan(2 * eps / (L - R)) / 2
    return (m1sq, m2sq), phi


def resum_delta_b(s):
    """
    Performs a resummation of the bottom Yukawa coupling. 
    Returns false if the required squark masses are negative.
    Formula from hep-ph/9402253.
    """
    from math import log, pi
    import numpy as np

    def Ii(a, b, c):
        if abs(c) < 1e-10:
            return log(a**2 / b**2) / (a**2 - b**2)
        else:
            return (a**2 * b**2 * log(a**2 / b**2) + b**2 * c**2 * log(
                b**2 / c**2) + c**2 * a**2 * log(c**2 / a**2)) / (
                    (a**2 - b**2) * (b**2 - c**2) * (a**2 - c**2))

    mst2 = stop_masssq(s)
    if np.min(mst2) < 0:
        return False
    mst = np.sqrt(mst2)

    msb2 = sbot_masssq(s)
    if np.min(msb2) < 0:
        return False
    msb = np.sqrt(msb2)
    corrfac = 1
    # take care of limits where the squarks are degenerate
    if abs(s['HMIX_1']) > 1e-3 or abs(s['TD_3_3']) > 1e-3:
        # alpha_3 = g_3^2/4pi
        corrfac += s['GAUGE_3']**2 / (
            6 * pi**2) * s['MSOFT_3'] * s['HMIX_1'] * s['MINPAR_3'] * Ii(
                msb[0], msb[1], s['MSOFT_3'])
    if abs(s['HMIX_1']) > 1e-3 or abs(s['TU_3_3']) > 1e-3:
        # y_t^1 because an additional power is in T_t
        # the Y_t from the reference is y_t^2/4pi
        corrfac += s['YU_3_3'] / (
            16 * pi**2) * s['HMIX_1'] * s['TU_3_3'] * s['MINPAR_3'] * Ii(
                mst[0], mst[1], s['HMIX_1'])
    return s['YD_3_3'] / corrfac


#%%


def resum_delta_tau(s):
    """
    Performs a resummation of the tau Yukawa coupling. 
    Returns false if the required stau masses are negative.
    Formula from hep-ph/0106027.
    """
    from math import log, pi, sin, cos
    import numpy as np

    def Ii(a, b, c):
        if abs(c) < 1e-10:
            return log(a**2 / b**2) / (a**2 - b**2)
        if abs(b) < 1e-10:
            return -(log(c**2 / a**2) / (a**2 - c**2))
        if abs(a) < 1e-10:
            return log(b**2 / c**2) / (b**2 - c**2)
        if abs(b - c) < 1e-10:
            return (-a**2 + c**2 + a**2 * log(a**2 / c**2)) / (a**2 - c**2)**2
        else:
            return (a**2 * b**2 * log(a**2 / b**2) + b**2 * c**2 * log(
                b**2 / c**2) + c**2 * a**2 * log(c**2 / a**2)) / (
                    (a**2 - b**2) * (b**2 - c**2) * (a**2 - c**2))

    mst2, mix = stau_masssq_and_mixing(s)
    if np.min(mst2) < 0:
        return False
    mst = np.sqrt(mst2)
    ctau = cos(mix)
    stau = sin(mix)
    msnutau = (cos(2 * s['HMIX_10']) * (s['GAUGE_1']**2 + s['GAUGE_2']**2) *
               s['HMIX_3']**2) / 8. + s['MSL2_3_3']
    corrfac = 1 + s['HMIX_1'] * s['MINPAR_3'] / (4 * pi)**2 * (
        -s['GAUGE_2']**2 * s['MSOFT_2'] *
        (Ii(msnutau, s['MSOFT_2'], s['HMIX_1']) + 1 / 2. *
         (ctau**2 * Ii(mst[0], s['MSOFT_2'], s['HMIX_1']) +
          stau**2 * Ii(mst[1], s['MSOFT_2'], s['HMIX_1']))) +
        s['GAUGE_1']**2 * s['MSOFT_1'] *
        (Ii(mst[0], mst[1], s['MSOFT_1']) +
         (ctau**2 / 2 - stau**2) * Ii(mst[0], s['MSOFT_1'], s['HMIX_1']) +
         (ctau**2 / 2 - stau**2) * Ii(mst[1], s['MSOFT_1'], s['HMIX_1'])))
    return s['YE_3_3'] / corrfac


def process_df(df, delta_b=True, delta_tau=True, check_masses=True):
    df['stable'] = True
    if delta_b:
        df['YD_33_resum'] = df.apply(resum_delta_b, axis=1)
        df.loc[df['YD_33_resum'] == False, 'stable'] = False
        df.loc[df['YD_33_resum'] != False, 'YD_3_3'] = df.loc[
            df['YD_33_resum'] != False, ('YD_33_resum')]
        del df['YD_33_resum']
    if delta_tau:
        df['YE_33_resum'] = df.apply(resum_delta_tau, axis=1)
        df.loc[df['YE_33_resum'] == False, 'stable'] = False
        df.loc[df['YE_33_resum'] != False, 'YE_3_3'] = df.loc[
            df['YE_33_resum'] != False, ('YE_33_resum')]
        del df['YE_33_resum']
    if check_masses:
        df['stable'] = df['stable'] & df.apply(check_tree_masssq, axis=1)
    dffinal = df.loc[df['stable'], :].reset_index(drop=True)
    del dffinal['stable']
    return dffinal

"""
def categorize(df, kind, tol=1e-3):
    def vev(name):
        return np.abs(df[kind + name]) > tol

    stable = np.zeros(df.index.size, dtype=bool)
    if kind == 'fast_' or kind == 'deep_':
        stable = df.fast_B == -2
    h = (vev('vhur0')) & (vev('vhdr0'))
    t = (vev('vulr3')) & (vev('vurr3'))
    b = (vev('vdlr3')) & (vev('vdrr3'))
    l = (vev('velr3')) & (vev('verr3'))
    v = (vev('vvlr3'))
    return [[
        h & np.invert(t | b | l | v | stable), {
            'label': r"$H$ vevs",
            'c': '#9e9e9e'
        }
    ], [
        h & t & np.invert(b | l | v | stable), {
            "label": r"$H,\tilde{t}$ vevs",
            'c': '#fdd835'
        }
    ], [
        h & b & np.invert(t | l | v | stable), {
            'label': r"$H,\tilde{b}$ vevs",
            'c': '#2196f3'
        }
    ], [
        h & l & np.invert(t | b | v | stable), {
            'label': r"$H,\tilde{\tau}$ vevs",
            'c': '#ef5350'
        }
    ], [
        h & b & t & np.invert(l | v | stable), {
            'label': r"$H,\tilde{t},\tilde{b}$ vevs",
            'c': '#00c853'
        }
    ], [
        h & b & l & np.invert(t | v | stable), {
            'label': r"$H,\tilde{b},\tilde{\tau}$ vevs",
            'c': '#aa00ff'
        }
    ], [
        h & l & t & np.invert(b | v | stable), {
            'label': r"$H,\tilde{t},\tilde{\tau}$ vevs",
            'c': '#ff9100'
        }
    ], [
        v & np.invert(stable), {
            'label': r"$unexpected \tilde{\nu}$ vevs",
            'c': '#455a64'
        }
    ]]
"""

def LoadModel(inputslha='spcfiles/sps1a.spc', outputconfig="test_local.csv"):
    try:
        d = pyslha.read(inputslha)
    except: return False
    d.blocks['MODSEL']
    model_dict = {}
    model_dict["MINPAR_3"]   = d.blocks["MINPAR"][3]
    model_dict["SMINPUTS_1"] = d.blocks["SMINPUTS"][1]
    model_dict["SMINPUTS_2"] = d.blocks["SMINPUTS"][2]
    model_dict["SMINPUTS_3"] = d.blocks["SMINPUTS"][3]
    model_dict["SMINPUTS_4"] = d.blocks["SMINPUTS"][4]
    model_dict["SMINPUTS_5"] = d.blocks["SMINPUTS"][5]
    model_dict["SMINPUTS_6"] = d.blocks["SMINPUTS"][6]
    model_dict["SMINPUTS_7"] = d.blocks["SMINPUTS"][7]
    model_dict["GAUGE_Q"]    = d.blocks["GAUGE"].q
    model_dict["GAUGE_1"]    = d.blocks["GAUGE"][1]
    model_dict["GAUGE_2"]    = d.blocks["GAUGE"][2]
    model_dict["GAUGE_3"]    = d.blocks["GAUGE"][3]
    model_dict["HMIX_Q"]     = d.blocks["HMIX"].q
    model_dict["HMIX_1"]     = d.blocks["HMIX"][1]
    model_dict["HMIX_2"]     = d.blocks["HMIX"][2]
    model_dict["HMIX_3"]     = d.blocks["HMIX"][3]
    model_dict["HMIX_4"]     = d.blocks["HMIX"][4]
    model_dict["HMIX_10"]    = 0 #d.blocks["HMIX"][10]
    model_dict["HMIX_101"]   = 0 #d.blocks["HMIX"][101]
    model_dict["HMIX_102"]   = 0 #d.blocks["HMIX"][102]
    model_dict["HMIX_103"]   = 0 #d.blocks["HMIX"][103]
    model_dict["MSOFT_Q"]    = d.blocks["MSOFT"].q
    model_dict["MSOFT_1"]    = d.blocks["MSOFT"][1]
    model_dict["MSOFT_2"]    = d.blocks["MSOFT"][2]
    model_dict["MSOFT_3"]    = d.blocks["MSOFT"][3]
    model_dict["MSOFT_21"]   = d.blocks["MSOFT"][21]
    model_dict["MSOFT_22"]   = d.blocks["MSOFT"][22]
    model_dict["YU_Q"]       = d.blocks["YU"].q
    model_dict["YU_1_1"]     = d.blocks["YU"][1,1]
    model_dict["YU_1_2"]     = 0 #d.blocks["YU"][1,2]
    model_dict["YU_1_3"]     = 0 #d.blocks["YU"][1,3]
    model_dict["YU_2_1"]     = 0 #d.blocks["YU"][2,1]
    model_dict["YU_2_2"]     = d.blocks["YU"][2,2]
    model_dict["YU_2_3"]     = 0 #d.blocks["YU"][2,3]
    model_dict["YU_3_1"]     = 0 #d.blocks["YU"][3,1]
    model_dict["YU_3_2"]     = 0 #d.blocks["YU"][3,2]
    model_dict["YU_3_3"]     = d.blocks["YU"][3,3]
    model_dict["YD_Q"]       = d.blocks["YD"].q
    model_dict["YD_1_1"]     = d.blocks["YD"][1,1]
    model_dict["YD_1_2"]     = 0 #d.blocks["YD"][1,2]
    model_dict["YD_1_3"]     = 0 #d.blocks["YD"][1,3]
    model_dict["YD_2_1"]     = 0 #d.blocks["YD"][2,1]
    model_dict["YD_2_2"]     = d.blocks["YD"][2,2]   
    model_dict["YD_2_3"]     = 0 #d.blocks["YD"][2,3]
    model_dict["YD_3_1"]     = 0 #d.blocks["YD"][3,1]
    model_dict["YD_3_2"]     = 0 #d.blocks["YD"][3,2]
    model_dict["YD_3_3"]     = d.blocks["YD"][3,3]
    model_dict["YE_Q"]       = d.blocks["YE"].q
    model_dict["YE_1_1"]     = d.blocks["YE"][1,1]
    model_dict["YE_1_2"]     = 0 #d.blocks["YE"][1,2]
    model_dict["YE_1_3"]     = 0 #d.blocks["YE"][1,3]
    model_dict["YE_2_1"]     = 0 #d.blocks["YE"][2,1]
    model_dict["YE_2_2"]     = d.blocks["YE"][2,2]
    model_dict["YE_2_3"]     = 0 #d.blocks["YE"][2,3]
    model_dict["YE_3_1"]     = 0 #d.blocks["YE"][3,1]
    model_dict["YE_3_2"]     = 0 #d.blocks["YE"][3,2]
    model_dict["YE_3_3"]     = d.blocks["YE"][3,3]
    model_dict["TU_Q"]       = d.blocks["AU"].q
    model_dict["TU_1_1"]     = d.blocks["AU"][1,1]
    model_dict["TU_1_2"]     = 0 #d.blocks["AU"][1,2]
    model_dict["TU_1_3"]     = 0 #d.blocks["AU"][1,3]
    model_dict["TU_2_1"]     = 0 #d.blocks["AU"][2,1]
    model_dict["TU_2_2"]     = d.blocks["AU"][2,2]
    model_dict["TU_2_3"]     = 0 #d.blocks["AU"][2,3]
    model_dict["TU_3_1"]     = 0 #d.blocks["AU"][3,1]
    model_dict["TU_3_2"]     = 0 #d.blocks["AU"][3,2]
    model_dict["TU_3_3"]     = d.blocks["AU"][3,3]
    model_dict["TD_Q"]       = d.blocks["AD"].q
    model_dict["TD_1_1"]     = d.blocks["AD"][1,1]
    model_dict["TD_1_2"]     = 0 #d.blocks["AD"][1,2]
    model_dict["TD_1_3"]     = 0 #d.blocks["AD"][1,3]
    model_dict["TD_2_1"]     = 0 #d.blocks["AD"][2,1]
    model_dict["TD_2_2"]     = d.blocks["AD"][2,2]
    model_dict["TD_2_3"]     = 0 #d.blocks["AD"][2,3]
    model_dict["TD_3_1"]     = 0 #d.blocks["AD"][3,1]
    model_dict["TD_3_2"]     = 0 #d.blocks["AD"][3,2]
    model_dict["TD_3_3"]     = d.blocks["AD"][3,3]
    model_dict["TE_Q"]       = d.blocks["AE"].q
    model_dict["TE_1_1"]     = d.blocks["AE"][1,1]
    model_dict["TE_1_2"]     = 0 #d.blocks["AE"][1,2]     
    model_dict["TE_1_3"]     = 0 #d.blocks["AE"][1,3]     
    model_dict["TE_2_1"]     = 0 #d.blocks["AE"][2,1]     
    model_dict["TE_2_2"]     = d.blocks["AE"][2,2]
    model_dict["TE_2_3"]     = 0 #d.blocks["AE"][2,3]
    model_dict["TE_3_1"]     = 0 #d.blocks["AE"][3,1]
    model_dict["TE_3_2"]     = 0 #d.blocks["AE"][3,2]
    model_dict["TE_3_3"]     = d.blocks["AE"][3,3]
    model_dict["MSQ2_Q"]     = d.blocks["YU"].q #d.blocks["MSQ2"]["Q"]
    model_dict["MSQ2_1_1"]   = d.blocks["MSOFT"][41]*d.blocks["MSOFT"][41] #d.blocks["MSQ2"]["1_1"]
    model_dict["MSQ2_1_2"]   = 0 #d.blocks["MSQ2"]["1_2"]
    model_dict["MSQ2_1_3"]   = 0 #d.blocks["MSQ2"]["1_3"]
    model_dict["MSQ2_2_1"]   = 0 #d.blocks["MSQ2"]["2_1"]
    model_dict["MSQ2_2_2"]   = d.blocks["MSOFT"][42]*d.blocks["MSOFT"][42] #d.blocks["MSQ2"]["2_2"]
    model_dict["MSQ2_2_3"]   = 0 #d.blocks["MSQ2"]["2_3"]
    model_dict["MSQ2_3_1"]   = 0 #d.blocks["MSQ2"]["3_1"]
    model_dict["MSQ2_3_2"]   = 0 #d.blocks["MSQ2"]["3_2"]
    model_dict["MSQ2_3_3"]   = d.blocks["MSOFT"][43]*d.blocks["MSOFT"][43] #d.blocks["MSQ2"]["3_3"]
    model_dict["MSL2_Q"]     = d.blocks["YU"].q #d.blocks["MSL2"]["Q"]
    model_dict["MSL2_1_1"]   = d.blocks["MSOFT"][31]*d.blocks["MSOFT"][31] #d.blocks["MSL2"]["1_1"]
    model_dict["MSL2_1_2"]   = 0 #d.blocks["MSL2"]["1_2"]
    model_dict["MSL2_1_3"]   = 0 #d.blocks["MSL2"]["1_3"]
    model_dict["MSL2_2_1"]   = 0 #d.blocks["MSL2"]["2_1"]
    model_dict["MSL2_2_2"]   = d.blocks["MSOFT"][32]*d.blocks["MSOFT"][32] #d.blocks["MSL2"]["2_2"]
    model_dict["MSL2_2_3"]   = 0 #d.blocks["MSL2"]["2_3"]
    model_dict["MSL2_3_1"]   = 0 #d.blocks["MSL2"]["3_1"]
    model_dict["MSL2_3_2"]   = 0 #d.blocks["MSL2"]["3_2"]
    model_dict["MSL2_3_3"]   = d.blocks["MSOFT"][33]*d.blocks["MSOFT"][33] #d.blocks["MSL2"]["3_3"]
    model_dict["MSD2_Q"]     = d.blocks["YU"].q #d.blocks["MSD2"]["Q"]
    model_dict["MSD2_1_1"]   = d.blocks["MSOFT"][47]*d.blocks["MSOFT"][47] #d.blocks["MSD2"]["1_1"]
    model_dict["MSD2_1_2"]   = 0 #d.blocks["MSD2"]["1_2"]
    model_dict["MSD2_1_3"]   = 0 #d.blocks["MSD2"]["1_3"]
    model_dict["MSD2_2_1"]   = 0 #d.blocks["MSD2"]["2_1"]
    model_dict["MSD2_2_2"]   = d.blocks["MSOFT"][48]*d.blocks["MSOFT"][48] #d.blocks["MSD2"]["2_2"]
    model_dict["MSD2_2_3"]   = 0 #d.blocks["MSD2"]["2_3"]
    model_dict["MSD2_3_1"]   = 0 #d.blocks["MSD2"]["3_1"]
    model_dict["MSD2_3_2"]   = 0 #d.blocks["MSD2"]["3_2"]
    model_dict["MSD2_3_3"]   = d.blocks["MSOFT"][49]*d.blocks["MSOFT"][49] #d.blocks["MSD2"]["3_3"]
    model_dict["MSU2_Q"]     = d.blocks["YU"].q #d.blocks["MSU2"]["Q"]
    model_dict["MSU2_1_1"]   = d.blocks["MSOFT"][44]*d.blocks["MSOFT"][44] #d.blocks["MSU2"]["1_1"]
    model_dict["MSU2_1_2"]   = 0 #d.blocks["MSU2"]["1_2"]
    model_dict["MSU2_1_3"]   = 0 #d.blocks["MSU2"]["1_3"]
    model_dict["MSU2_2_1"]   = 0 #d.blocks["MSU2"]["2_1"]
    model_dict["MSU2_2_2"]   = d.blocks["MSOFT"][45]*d.blocks["MSOFT"][45] #d.blocks["MSU2"]["2_2"]
    model_dict["MSU2_2_3"]   = 0 #d.blocks["MSU2"]["2_3"]
    model_dict["MSU2_3_1"]   = 0 #d.blocks["MSU2"]["3_1"]
    model_dict["MSU2_3_2"]   = 0 #d.blocks["MSU2"]["3_2"]
    model_dict["MSU2_3_3"]   = d.blocks["MSOFT"][46]*d.blocks["MSOFT"][46] #d.blocks["MSU2"]["3_3"]
    model_dict["MSE2_Q"]     = d.blocks["YU"].q #d.blocks["MSE2"]["Q"]
    model_dict["MSE2_1_1"]   = d.blocks["MSOFT"][34]*d.blocks["MSOFT"][34] #d.blocks["MSE2"]["1_1"]
    model_dict["MSE2_1_2"]   = 0 #d.blocks["MSE2"]["1_2"]
    model_dict["MSE2_1_3"]   = 0 #d.blocks["MSE2"]["1_3"]
    model_dict["MSE2_2_1"]   = 0 #d.blocks["MSE2"]["2_1"]
    model_dict["MSE2_2_2"]   = d.blocks["MSOFT"][35]*d.blocks["MSOFT"][35] #d.blocks["MSE2"]["2_2"]
    model_dict["MSE2_2_3"]   = 0 #d.blocks["MSE2"]["2_3"]
    model_dict["MSE2_3_1"]   = 0 #d.blocks["MSE2"]["3_1"]
    model_dict["MSE2_3_2"]   = 0 #d.blocks["MSE2"]["3_2"]
    model_dict["MSE2_3_3"]   = d.blocks["MSOFT"][36]*d.blocks["MSOFT"][36] #d.blocks["MSE2"]["3_3"]
    
    model_df = pd.DataFrame(model_dict, index=[0])
    model_df.to_csv(outputconfig, sep ='\t')
    
    return True


def DumpConfigFile(createConfigFile, input_slha_convert, output_file):
    
    text_file = open(createConfigFile, "w")
    
    text_file.write("EVADE:"+ "\n")
    text_file.write("{"+ "\n")
    text_file.write("   input = \"" + input_slha_convert + "\""+ "\n")
    text_file.write("   output = \"" + output_file + "\""+ "\n")
    text_file.write("   outputType = \"stability\""+ "\n")
    text_file.write("   StationarityConditions:"+ "\n")
    text_file.write("   {"+ "\n")
    text_file.write("       fieldSets = ("+ "\n")
    text_file.write("           [\"vhur0\",\"vhdr0\",\"vulr3\",\"vurr3\"],"+ "\n")
    text_file.write("           [\"vhur0\",\"vhdr0\",\"vdlr3\",\"vdrr3\"],"+ "\n")
    text_file.write("           [\"vhur0\",\"vhdr0\",\"velr3\",\"verr3\",\"vvlr3\"]"+ "\n")
    text_file.write("       )"+ "\n")
    text_file.write("   }"+ "\n")
    text_file.write("}"+ "\n")
    text_file.close()


def convert_slha(input_slha, evade_infile, evade_conffile, outfile) -> bool:
    modelName = input_slha.split('/')[-1]
    modelName = modelName.split('.')[0]
    # print(modelName)
    
    #LoadModel(input_slha, outputconfig = modelName+'.in' )
    #DumpConfigFile(createConfigFile = modelName+'.cfg', input_slha_convert = modelName+'.in', output_file = modelName+'.tsv')
    success = LoadModel(input_slha, outputconfig = evade_infile )
    
    if not success:
        return success
    
    DumpConfigFile(createConfigFile = evade_conffile, input_slha_convert = evade_infile, output_file = outfile)
    
    return True