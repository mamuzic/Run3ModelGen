#include"../include/micromegas.h"
#include"../include/micromegas_aux.h"

//===================  Experimental Limits ==============


typedef double ( * funcArg)(double x, void * arf);

#ifdef oolldd
double  XENON1T_90(double M)
{ 
// 1805.12562  
  if(M<6 || M>1000) { return sqrt(-1);}
  double   data_1t_lnM[25]={ 1.790E+00, 1.885E+00, 2.006E+00, 2.148E+00, 2.297E+00, 2.449E+00, 2.598E+00, 2.783E+00, 2.961E+00, 3.117E+00, 3.302E+00, 3.444E+00, 3.614E+00, 3.796E+00, 4.037E+00, 4.268E+00, 4.581E+00, 4.904E+00, 5.178E+00, 5.441E+00, 5.768E+00, 6.095E+00, 6.369E+00, 6.550E+00, 6.891E+00};
  double   data_1t_lnS[25]={ 1.040E+00, 2.794E-02,-1.003E+00,-2.035E+00,-2.888E+00,-3.591E+00,-4.144E+00,-4.717E+00,-5.111E+00,-5.326E+00,-5.458E+00,-5.486E+00,-5.440E+00,-5.375E+00,-5.178E+00,-4.982E+00,-4.711E+00,-4.412E+00,-4.150E+00,-3.925E+00,-3.598E+00,-3.270E+00,-3.009E+00,-2.812E+00,-2.485E+00};

  return 1E-44*exp( polint3(log(M),25,data_1t_lnM,  data_1t_lnS)); 
} 
#endif
double  XENON1T_90(double M)
{ 
// 1805.12562  
  if(M<6 || M>10000) { return sqrt(-1);}
  
   double   data_1t_lnM[16]={ 1.7918E+00, 2.0794E+00, 2.1972E+00, 2.3026E+00, 2.7081E+00, 2.9957E+00, 3.4012E+00, 3.6889E+00, 3.9120E+00, 4.2485E+00, 4.6052E+00, 5.0106E+00, 5.2983E+00, 5.9915E+00, 6.9078E+00, 9.2103E+00};
   double   data_1t_lnS[25]={ 9.1027E-01,-1.5852E+00,-2.3646E+00,-2.9210E+00,-4.4456E+00,-5.1749E+00,-5.5085E+00,-5.4084E+00,-5.2480E+00,-4.9920E+00,-4.6968E+00,-4.3329E+00,-4.0658E+00,-3.3986E+00,-2.4958E+00,-1.9784E-01};
  
  return 1E-44*exp( polint3(log(M),16,data_1t_lnM,  data_1t_lnS)); 
} 




double DS50_90(double M)
{
  double X[]={0.66758716,0.701560,0.80475533,0.93670535,1.0839419,1.232539,1.4514834,1.7910694,
1.9607502,2.152783,2.3774657,2.6179435,2.968157,3.1929226,3.444752,3.705608,
3.9745953,4.2755737,4.708043,5.049796,5.6423516,6.0696225,7.0236797,7.847855,9.081425,10.0};
  double Y[]={9.775542E-39,5.932523E-39,1.590042E-39,4.66674E-40,1.68017E-40,7.2538E-41,3.0614E-41,1.292E-41,1.0066E-41,8.586E-42,7.16E-42,5.836E-42,4.868E-42,
3.542E-42,2.637E-42,1.963E-42,1.397E-42,1.138E-42,8.28E-43,6.75E-43,5.38E-43,4.7E-43,3.83E-43,3.2E-43,2.79E-43,2.6E-43};
  double  x= M;
  if(x<X[0] || x>X[25])   return sqrt(-1);
  double  y=polint3(x,26,X,Y);
  return y;
}

double DS50_90_noB(double M)
{
  double X[]={1.52535,1.57974,1.66013,1.78585,1.98378,2.21010,2.55750,2.94227,3.47506,3.80428,4.11632,
4.55923,5.09422,5.77570,5.94683,6.70310,8.24723,10.0};
  double Y[]={9.77554e-39,7.59069e-41,5.40004e-41,2.99261e-41,1.62130e-41,1.07746e-41,7.66510e-42,5.45245e-42,3.87879e-42,2.51953e-42,
1.67455e-42,1.13785e-42,7.39886e-43,5.38099e-43,4.91856e-43,4.10580e-43,2.98477e-43,2.60642e-43};
  double  x= M;
  if(x<X[0] || x>X[17])   return sqrt(-1); 
  double  y=polint3(x,17,X,Y);
  return y;
}


double CRESST_III_90(double M)
{
// 1904.00498 , 1905.07335v3

double X[20]={0.16   , 0.208     ,0.2704    ,0.35152   ,0.456976  ,0.594069  ,0.772289  ,1         ,1.5       ,2.25      ,3.375     ,5.0625    ,7.59375   ,11.3906   ,17.0859   ,25.6289   ,38.4434   ,57.665    ,86.4976   ,129.746};
double Y[20]={473.589, 5.72634,0.73854,0.262798,0.106657,0.042227,0.0166904,0.00735987,0.0027698,0.00056334,0.000112663,3.79581e-05,1.11803e-05,3.26202e-06,1.48371e-06,1.06977e-06,1.03226e-06,1.22993e-06,1.64711e-06,2.33581e-06};

 double lnY[20];
 if(M<X[0] || M>X[19]) return sqrt(-1);
 
 for(int i=0;i<20;i++) lnY[i]=log(Y[i]);
 return    1E-36*exp(polint3(M,20,X,lnY));
}

double CRESST_III_SDn_90(double M)
{

double X[20]={  0.16     ,0.208    ,0.2704   ,0.35152  ,0.456976 ,0.594069 ,0.772289 ,1        ,1.5      ,2.25     ,3.375    ,5.0625   ,7.59375  ,11.3906  ,17.0859  ,25.6289  ,38.4434  ,57.665   ,86.4976  ,129.746};  
double Y[20]={ 1.41379e+09, 1.30417e+07, 1.38878e+06, 479170, 193183, 80146.6, 32455, 13089.8, 5615.3, 3170.17, 1004.26, 508.033, 317.802, 278.246, 294.276, 358.564, 476.733, 666.298, 957.892, 1399.73};

 double lnY[20];
 if(M<X[0] || M>X[19]) return sqrt(-1);
  
 for(int i=0;i<20;i++) lnY[i]=log(Y[i]);
 return    1E-36*exp(polint3(M,20,X,lnY));
    
}


double XENON1T_SDp_90(double M)
{
  double X[]={160,184,235,283,339,407,470,559,700,811,920,1083};
  double Y[]={130,196,295,357,404,436,439,421,391,363,336,291};
  double x,y;
  x=  250+(log10(M)-1)*(668-250);   
  if(x+3<X[0] || x>X[11]) { printf("M=%.1E out of Xenon1T range\n",M);  return 0; }
  y=polint3(x,12,X,Y);
  return 1E-40*pow(10, 4*(y-474)/(21-474));
}

double XENON1T_SDn_90(double M)
{
  double X[]={159,211,273,343,410,504,620,729,915,1085};
  double Y[]={299,421,515,576,604,602,578,551,501,457};
  double x,y;
  x=  250+(log10(M)-1)*(668-250);   
  if(x+3<X[0] || x>X[9]) { printf("M=%.1E out of Xenon1T range\n",M);  return 0; }
  y=polint3(x,10,X,Y);
  return 1E-40*pow(10, 4*(y-476)/(21-474));
}



double PICO60_SDp_90(double M)
{
  double  X[41]={ 2.7542 , 3.0200 , 3.3113 , 3.6308 , 3.9811 , 4.3652 , 4.7863 , 5.2481 , 5.7544 , 6.3096 , 6.9183 , 7.5858 , 8.3176 , 9.1201 , 10.000 , 10.965 , 12.023 , 13.183 , 14.454 , 15.849 , 17.378 , 19.055 , 20.893 , 22.909 , 25.119 , 31.623 , 39.811 , 50.119 , 63.096 , 79.433 , 100.00 , 125.89 , 158.49 , 199.53 , 251.19 , 316.23 , 1000.0 , 3162.3 , 10000  , 31623  , 100000 };
  double  Y[41]={1.5963e-36, 7.2146e-38, 1.6675e-38, 3.9279e-39, 1.5982e-39, 8.0302e-40, 4.4673e-40, 2.7069e-40, 1.9277e-40, 1.3766e-40, 1.0545e-40, 8.3942e-41, 6.9240e-41, 5.8732e-41, 5.1877e-41, 4.5991e-41, 4.1587e-41, 3.8886e-41, 3.6786e-41, 3.4587e-41, 3.3472e-41, 3.2645e-41, 3.2056e-41, 3.1734e-41, 3.1585e-41, 3.2228e-41, 3.4011e-41, 3.6985e-41, 4.1332e-41, 4.7184e-41, 5.4948e-41, 6.4818e-41, 7.6788e-41, 9.3926e-41, 1.1422e-40, 1.3842e-40, 4.1409e-40, 1.2783e-39, 3.9659e-39, 1.2689e-38, 4.0017e-38}; 

  if(M<2.7542 || M>10000)  return sqrt(-1); 
  
  double logX[41],logY[41];
  for(int i=0;i<41;i++) {logX[i]=log(X[i]); logY[i]=log(Y[i]);}
  
  return exp(polint3(log(M),41,logX,logY));
}  



double PICO60_90(double M)
{
   double X[41]={2.7542 , 3.0200 , 3.3113 , 3.6308 , 3.9811 , 4.3652 , 4.7863 , 5.2481 , 5.7544 , 6.3096 , 6.9183 , 7.5858 , 8.3176 , 9.1201 , 10.000 , 10.965 , 12.023 , 13.183 , 14.454 , 15.849 , 17.378 , 19.055 , 20.893 , 22.909 , 25.119 , 31.623 , 39.811 , 50.119 , 63.096 , 79.433 , 100.00 , 125.89 , 158.49 , 199.53 , 251.19 , 316.23 , 1000.0 , 3162.3 , 10000  , 31623  , 100000 };
   double Y[41]={ 2.8850e-39, 1.9855e-40, 3.4389e-41, 9.9866e-42, 4.1113e-42, 1.9687e-42, 1.0947e-42, 6.8471e-43, 4.5924e-43, 3.2256e-43, 2.4749e-43, 1.9765e-43, 1.6294e-43, 1.3777e-43, 1.2191e-43, 1.0798e-43, 9.9160e-44, 9.2508e-44, 8.5771e-44, 8.2583e-44, 7.8311e-44, 7.6528e-44, 7.5318e-44, 7.4593e-44, 7.4290e-44, 7.5584e-44, 7.9740e-44, 8.6719e-44, 9.6748e-44, 1.1029e-43, 1.2802e-43, 1.5119e-43, 1.8074e-43, 2.1785e-43, 2.6529e-43, 3.2522e-43, 9.5813e-43, 2.9623e-42, 9.3009e-42, 2.9346e-41, 9.2733e-41};

   if(M<2.7542 || M>10000)   return sqrt(-1); 
   double logX[41],logY[41];
   for(int i=0;i<41;i++) {logX[i]=log(X[i]); logY[i]=log(Y[i]);}   
   return exp(polint3(log(M),41,logX,logY));
}

//====================================================================


double (*dNdEfact)(double Enr_kev,int A )=NULL;



//======================= CRESST_III ===============================

static double CRESSTeff(double E, char*chA)
{ 

  double  eGrid[101]={0.030,0.190,0.349,0.509,0.669,0.829,0.988,1.148,1.308,1.467,1.627,1.787,1.946,2.106,2.266,2.426,2.585,2.745,2.905,3.064,3.224,3.384,3.543,3.703,3.863,4.023,4.182,4.342,4.502,4.661,4.821,4.981,5.140,5.300,5.460,5.620,5.779,5.939,6.099,6.258,6.418,6.578,6.737,6.897,7.057,7.217,7.376,7.536,7.696,7.855,8.015,8.175,8.334,8.494,8.654,8.814,8.973,9.133,9.293,9.452,9.612,9.772,9.931,10.091,10.251,10.411,10.570,10.730,10.890,11.049,11.209,11.369,11.528,11.688,11.848,12.008,12.167,12.327,12.487,12.646,12.806,12.966,13.125,13.285,13.445,13.605,13.764,13.924,14.084,14.243,14.403,14.563,14.722,14.882,15.042,15.202,15.361,15.521,15.681,15.840,15.998};
  double  CaDat[101]={0.501,0.530,0.556,0.579,0.600,0.620,0.638,0.655,0.670,0.685,0.699,0.712,0.724,0.735,0.746,0.756,0.766,0.775,0.783,0.792,0.800,0.807,0.814,0.821,0.828,0.834,0.840,0.846,0.851,0.856,0.861,0.866,0.871,0.875,0.879,0.883,0.887,0.891,0.895,0.898,0.902,0.905,0.908,0.911,0.914,0.917,0.919,0.922,0.924,0.927,0.929,0.931,0.933,0.936,0.938,0.939,0.941,0.943,0.945,0.947,0.948,0.950,0.951, 0.953, 0.954, 0.956,0.957,0.958,0.959,0.961,0.962,0.963,0.964,0.965,0.966,0.967,0.968,0.969,0.970,0.971,0.972,0.972,0.973,0.974,0.975,0.975,0.976,0.977,0.977,0.978,0.979,0.979,0.980,0.980,0.981,0.982,0.982,0.983,0.983,0.983,0.984};
  double  ODat[101]= {0.495,0.493,0.492,0.491,0.491,0.491,0.491,0.491,0.491,0.491,0.491,0.492,0.492,0.492,0.493,0.493,0.493,0.494,0.494,0.494,0.495,0.495,0.495,0.495,0.496,0.496,0.496,0.496,0.496,0.497,0.497,0.497,0.497,0.497,0.497,0.498,0.498,0.498,0.498,0.498,0.498,0.498,0.498,0.498,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499,0.499, 0.499, 0.499, 0.499,0.499,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500,0.500};
  double  WDat[101]= {0.506,0.561,0.613,0.662,0.706,0.747,0.783,0.815,0.843,0.868,0.889,0.907,0.922,0.935,0.946,0.955,0.963,0.969,0.974,0.978,0.982,0.984,0.986,0.988,0.990,0.991,0.992,0.992,0.993,0.993,0.994,0.994,0.994,0.994,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995, 0.995, 0.995, 0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,0.995,};

  double ER[23]= {0.0176757,  0.0221943, 0.0265357, 0.0310543, 0.0316745, 0.0353957, 0.051748, 0.0527613, 0.0734057, 0.0950634, 0.116721,   0.138379,  0.156943,  0.265231,  0.423023,  1.05419,   2.10923,  4.21931,   6.32939,   8.43946, 10.5464,  21.0937,  42.1914};
  double Eff[23]={0.00192164, 0.0208901, 0.111801,  0.300011,  0.328655,  0.465871,  0.565451, 0.5726,    0.58121,   0.588026,  0.591991,   0.597233,  0.599254,  0.617353,  0.627702,  0.657885,  0.657977, 0.653419,  0.636019,  0.617891, 0.626768, 0.671934, 0.678923};

  if(E>17) return 0;
  if(chA=="Ca") return polint3(E,101,eGrid,CaDat);
  if(chA=="O")  return polint3(E,101,eGrid,ODat);
  if(chA=="W")  return polint3(E,101,eGrid,WDat);
  if(chA=="Eff") return polint3(E,23,ER,Eff); 
  return 0;
}


#define CRESST_Exposure 5.594 //  5.689
static double sigmaCresst=0.0055, nSigmaCresst=2.4;

static double eCresst;
static double CRESST_smooth(double E,double* dNdE)
{
  double norm=sqrt(2*M_PI)*erf(M_SQRT2*nSigmaCresst);
  return dNdERecoil(E,dNdE)* exp(-pow((eCresst-E)/sigmaCresst,2)/2)/(norm*sigmaCresst);
}

static  void CRESST_III_MaxGap(double*dNdE, double *M, int *N, int *pos)
{ 

   double events[443]={0.03,0.0303,0.0303,0.0304,0.0304,0.0308,0.0309,0.0310,0.0310,0.0312,0.0313,0.0313,0.0314,0.0314,0.0315,0.0316,0.0316,0.0316,0.0316,0.0317,0.0318,0.0319,0.0319,0.0319,0.0319,0.0320,0.0321,0.0322,0.0322,0.0323,0.0324,0.0324,0.0324,0.0324,0.0324,0.0324,0.0325,0.0325,0.0326,0.0326,0.0326,0.0327,0.0327,0.0329,0.0329,0.0330,0.0330,0.0331,0.0331,0.0331,0.0332,0.0332,0.0333,0.0334,0.0334,0.0334,0.0335,0.0336,0.0337,0.0337,0.0337,0.0337,0.0338,0.0340,0.0343,0.0344,0.0345,0.0346,0.0346,0.0347,0.0349,0.0349,0.0350,0.0351,0.0351,0.0351,0.0351,0.0351,0.0352,0.0352,0.0352,0.0353,0.0353,0.0353,0.0353,0.0354,0.0354,0.0354,0.0356,0.0356,0.0357,0.0357,0.0357,0.0357,0.0358,0.0358,0.0358,0.0359,0.0360,0.0360,0.0360,0.0360,0.0361,0.0361,0.0362,0.0362,0.0363,0.0363,0.0364,0.0364,0.0366,0.0366,0.0366,0.0367,0.0368,0.0369,0.0370,0.0370,0.0371,0.0371,0.0372,0.0372,0.0373,0.0373,0.0374,0.0374,0.0375,0.0375,0.0378,0.0379,0.0380,0.0382,0.0382,0.0383,0.0383,0.0383,0.0384,0.0385,0.0387,0.0387,0.0389,0.0389,0.0389,0.0390,0.0390,0.0390,0.0391,0.0392,0.0392,0.0393,0.0393,0.0393,0.0394,0.0394,0.0395,0.0397,0.0397,0.0397,0.0398,0.0398,0.0399,0.0399,0.0400,0.0400,0.0401,0.0402,0.0403,0.0403,0.0403,0.0404,0.0405,0.0408,0.0408,0.0408,0.0408,0.0408,0.0408,0.0410,0.0410,0.0410,0.0414,0.0415,0.0416,0.0416,0.0416,0.0417,0.0418,0.0420,0.0420,0.0420,0.0421,0.0422,0.0423,0.0423,0.0425,0.0425,0.0427,0.0428,0.0428,0.0428,0.0429,0.0430,0.0430,0.0432,0.0433,0.0434,0.0438,0.0438,0.0438,0.0438,0.0440,0.0441,0.0442,0.0443,0.0444,0.0444,0.0444,0.0445,0.0447,0.0448,0.0450,0.0450,0.0450,0.0452,0.0453,0.0454,0.0456,0.0459,0.0460,0.0460,0.0460,0.0461,0.0461,0.0462,0.0463,0.0463,0.0464,0.0465,0.0465,0.0466,0.0466,0.0466,0.0466,0.0467,0.0467,0.0467,0.0471,0.0471,0.0473,0.0474,0.0475,0.0476,0.0476,0.0477,0.0477,0.0477,0.0480,0.0484,0.0484,0.0487,0.0487,0.0487,0.0492,0.0494,0.0495,0.0495,0.0496,0.0497,0.0497,0.0497,0.0497,0.0500,0.0504,0.0505,0.0505,0.0506,0.0507,0.0509,0.0511,0.0511,0.0512,0.0512,0.0516,0.0516,0.0517,0.0517,0.0518,0.0519,0.0520,0.0521,0.0521,0.0522,0.0522,0.0523,0.0524,0.0525,0.0528,0.0531,0.0533,0.0533,0.0534,0.0539,0.0543,0.0543,0.0545,0.0546,0.0546,0.0547,0.0548,0.0550,0.0550,0.0552,0.0553,0.0562,0.0562,0.0562,0.0566,0.0567,0.0570,0.0574,0.0579,0.0581,0.0583,0.0583,0.0587,0.0587,0.0588,0.0590,0.0593,0.0599,0.0599,0.0599,0.0599,0.0600,0.0603,0.0605,0.0606,0.0615,0.0620,0.0622,0.0624,0.0626,0.0626,0.0627,0.0630,0.0634,0.0638,0.0638,0.0639,0.0644,0.0644,0.0647,0.0648,0.0659,0.0660,0.0664,0.0668,0.0670,0.0675,0.0679,0.0682,0.0682,0.0694,0.0696,0.0697,0.0705,0.0708,0.0709,0.0720,0.0727,0.0736,0.0739,0.0742,0.0750,0.0757,0.0765,0.0774,0.0797,0.0797,0.0816,0.0819,0.0822,0.0829,0.0833,0.0842,0.0842,0.0846,0.0847,0.0865,0.0875,0.0884,0.0888,0.0888,0.0889,0.0905,0.0907,0.0909,0.0909,0.0925,0.0931,0.0937,0.0941,0.0946,0.0947,0.0952,0.0954,0.0988,0.1025,0.1034,0.1041,0.1050,0.1051,0.1088,0.1091,0.1116,0.1120,0.1157,0.1176,0.1194,0.1216,0.1229,0.1245,0.1258,0.1345,0.1407,0.1425,0.1469,0.1570,0.1593,0.1594,0.1682,0.1684,0.1721,0.1799,0.2101,0.2684,0.3440,0.3731,0.3842,0.5112,0.5297,0.6268,16};
   double m=0;
   int lm=0;
   *N=0;
   for(int l=0;l<442;l++) 
   {  
      if(events[l]+0.00005<events[l+1])        
      { double cc=CRESST_Exposure*simpson_arg((funcArg)dNdERecoil,dNdE, events[l]+0.00005,events[l+1],1E-2,NULL);
             if(cc>m) {m=cc;lm=l;}     
     }
     (*N)++;
     if(m>0 && dNdERecoil(events[l+1],dNdE)==0) break; 
   }
   if(pos) *pos=lm;
   *M=m;
}

extern float UpperLim(float CL,int If, int N, float* FC, float muB,float*FB,int *Iflag);

static  double CRESST_III_UpperLim(double pval, double*dNdE)
{ 
   double events[443]={0.0301,0.0303,0.0303,0.0304,0.0304,0.0308,0.0309,0.0310,0.0310,0.0312,0.0313,0.0313,0.0314,0.0314,0.0315,0.0316,0.0316,0.0316,0.0316,0.0317,0.0318,0.0319,0.0319,0.0319,0.0319,0.0320,0.0321,0.0322,0.0322,0.0323,0.0324,0.0324,0.0324,0.0324,0.0324,0.0324,0.0325,0.0325,0.0326,0.0326,0.0326,0.0327,0.0327,0.0329,0.0329,0.0330,0.0330,0.0331,0.0331,0.0331,0.0332,0.0332,0.0333,0.0334,0.0334,0.0334,0.0335,0.0336,0.0337,0.0337,0.0337,0.0337,0.0338,0.0340,0.0343,0.0344,0.0345,0.0346,0.0346,0.0347,0.0349,0.0349,0.0350,0.0351,0.0351,0.0351,0.0351,0.0351,0.0352,0.0352,0.0352,0.0353,0.0353,0.0353,0.0353,0.0354,0.0354,0.0354,0.0356,0.0356,0.0357,0.0357,0.0357,0.0357,0.0358,0.0358,0.0358,0.0359,0.0360,0.0360,0.0360,0.0360,0.0361,0.0361,0.0362,0.0362,0.0363,0.0363,0.0364,0.0364,0.0366,0.0366,0.0366,0.0367,0.0368,0.0369,0.0370,0.0370,0.0371,0.0371,0.0372,0.0372,0.0373,0.0373,0.0374,0.0374,0.0375,0.0375,0.0378,0.0379,0.0380,0.0382,0.0382,0.0383,0.0383,0.0383,0.0384,0.0385,0.0387,0.0387,0.0389,0.0389,0.0389,0.0390,0.0390,0.0390,0.0391,0.0392,0.0392,0.0393,0.0393,0.0393,0.0394,0.0394,0.0395,0.0397,0.0397,0.0397,0.0398,0.0398,0.0399,0.0399,0.0400,0.0400,0.0401,0.0402,0.0403,0.0403,0.0403,0.0404,0.0405,0.0408,0.0408,0.0408,0.0408,0.0408,0.0408,0.0410,0.0410,0.0410,0.0414,0.0415,0.0416,0.0416,0.0416,0.0417,0.0418,0.0420,0.0420,0.0420,0.0421,0.0422,0.0423,0.0423,0.0425,0.0425,0.0427,0.0428,0.0428,0.0428,0.0429,0.0430,0.0430,0.0432,0.0433,0.0434,0.0438,0.0438,0.0438,0.0438,0.0440,0.0441,0.0442,0.0443,0.0444,0.0444,0.0444,0.0445,0.0447,0.0448,0.0450,0.0450,0.0450,0.0452,0.0453,0.0454,0.0456,0.0459,0.0460,0.0460,0.0460,0.0461,0.0461,0.0462,0.0463,0.0463,0.0464,0.0465,0.0465,0.0466,0.0466,0.0466,0.0466,0.0467,0.0467,0.0467,0.0471,0.0471,0.0473,0.0474,0.0475,0.0476,0.0476,0.0477,0.0477,0.0477,0.0480,0.0484,0.0484,0.0487,0.0487,0.0487,0.0492,0.0494,0.0495,0.0495,0.0496,0.0497,0.0497,0.0497,0.0497,0.0500,0.0504,0.0505,0.0505,0.0506,0.0507,0.0509,0.0511,0.0511,0.0512,0.0512,0.0516,0.0516,0.0517,0.0517,0.0518,0.0519,0.0520,0.0521,0.0521,0.0522,0.0522,0.0523,0.0524,0.0525,0.0528,0.0531,0.0533,0.0533,0.0534,0.0539,0.0543,0.0543,0.0545,0.0546,0.0546,0.0547,0.0548,0.0550,0.0550,0.0552,0.0553,0.0562,0.0562,0.0562,0.0566,0.0567,0.0570,0.0574,0.0579,0.0581,0.0583,0.0583,0.0587,0.0587,0.0588,0.0590,0.0593,0.0599,0.0599,0.0599,0.0599,0.0600,0.0603,0.0605,0.0606,0.0615,0.0620,0.0622,0.0624,0.0626,0.0626,0.0627,0.0630,0.0634,0.0638,0.0638,0.0639,0.0644,0.0644,0.0647,0.0648,0.0659,0.0660,0.0664,0.0668,0.0670,0.0675,0.0679,0.0682,0.0682,0.0694,0.0696,0.0697,0.0705,0.0708,0.0709,0.0720,0.0727,0.0736,0.0739,0.0742,0.0750,0.0757,0.0765,0.0774,0.0797,0.0797,0.0816,0.0819,0.0822,0.0829,0.0833,0.0842,0.0842,0.0846,0.0847,0.0865,0.0875,0.0884,0.0888,0.0888,0.0889,0.0905,0.0907,0.0909,0.0909,0.0925,0.0931,0.0937,0.0941,0.0946,0.0947,0.0952,0.0954,0.0988,0.1025,0.1034,0.1041,0.1050,0.1051,0.1088,0.1091,0.1116,0.1120,0.1157,0.1176,0.1194,0.1216,0.1229,0.1245,0.1258,0.1345,0.1407,0.1425,0.1469,0.1570,0.1593,0.1594,0.1682,0.1684,0.1721,0.1799,0.2101,0.2684,0.3440,0.3731,0.3842,0.5112,0.5297,0.6268,16};
   float prob[443]={};
   float probB[443]={};
   prob[0]=0;

   for(int l=0;l<442;l++) prob[l+1]=CRESST_Exposure*simpson_arg((funcArg)dNdERecoil,dNdE, events[l],events[l+1],1E-2,NULL);
   for(int l=1;l<442;l++) prob[l+1]+=prob[l];
   double Nexp=prob[442];
   for(int l=1;l<=442;l++) prob[l]/=Nexp;
   int Iflag;

   double pval1=0.2, pval2=0.005;   
   if(pval2<=pval && pval<=pval1) return UpperLim(1-pval,7, 441, prob, 0,probB,&Iflag)/Nexp;
   else 
   {
      double s1=UpperLim(1-pval1,7, 441, prob, 0,probB,&Iflag)/Nexp
            ,s2=UpperLim(1-pval2,7, 441, prob, 0,probB,&Iflag)/Nexp; // s2>s1   
      if(pval<pval1){ double s0=(s2-s1)/log(pval1/pval2), c0=pval2*exp(s2/s0); return -log(pval/c0)*s0; }
      else return s1*(1-pval)/(1-pval1);
   }   
}


//=========== Xenon1T_2018 =================

static double BgXe1T=0; //0.65;

static double p0Z1T_best(double E)
{

  int Ntab=14;
  double Etab[14]={1.692E+00,2.000E+00,3.000E+00,4.000E+00,5.000E+00,6.000E+00,7.000E+00,8.000E+00,9.000E+00,1.000E+01,1.100E+01,1.200E+01,1.300E+01,1.400E+01};
  double Ptab[14]={0.000E+00,3.059E-02,1.051E-01,2.190E-01,3.519E-01,4.606E-01,5.203E-01,5.266E-01,4.808E-01,3.852E-01,2.732E-01,1.576E-01,6.648E-02,0.000E+00};
      
  if(E<=Etab[0] || E>=Etab[Ntab-1]) return 0;

  return (1-BgXe1T/log(10))*polint3(E,Ntab,Etab,Ptab); 
}


double Xe1TpEff(double E) {  return  p0Z1T_best(E); } 



// ====================== DarkSide50  data ===============

static double  DSExposure=6786;


#define static
static int neLast=48;   // the last experimental bin
static int neB=7;       // the first bin where addition backgrount is not expected
static double  resolution=0.2;    // energy resolution as a part of total energy
static double DSbgFactor=1.04;   //addition  factor for background 
static double xQuenching=0.;   // quenching interpolation bitween min and max. 0.25 -solid like Fig.6  
static int noBinCase=2;

#define static
static int DS_neStart=4;   // first experimental bin.  
static double DS_E1ion= 0.0195;   // (0.0195 KeV- Masa)/(15.76 ev - WWW)  - energy of ionization
static int neFluct=2; // 1 binominal, 2-improved Poisson  
#undef static 


static double dsData[49]= {17.4835,   32.4039,    0.903473, 0.0991742,0.0371351,0.033451, 0.0291776,0.0293249,0.0278513,0.0363983,0.0338931,0.0384613,0.036693,0.0484819,0.0495134,0.0514291,0.0517239,0.0518712,0.0565868,0.0605655,0.0596814,0.0679336,0.0677863,0.0642496,0.0736807,0.0804593,0.0792805,0.0789857,0.081933,0.0859117,0.0844381,0.0928377,0.0888589,0.0935745,0.094164,0.1005,0.108458,0.111258,0.118479,0.11951,0.119215,0.129973,0.137636,0.137783,0.128352,0.142204,0.139404,0.157971,0.146919};
static double dsBG2[50]=  {0.00602712, 0.00690356,0.0141333,0.0174831,0.0175687,0.0182198,0.0230185,0.0239824,0.0263956,0.0304772, 0.0334905, 0.0406516, 0.0417688, 0.0451036, 0.0447058, 0.0523288, 0.0461504, 0.0520661, 0.0545954, 0.0647725, 0.0657942, 0.0624255, 0.0625346, 0.0715269, 0.0700218, 0.067198, 0.0753539, 0.0823083, 0.0846454, 0.078775, 0.0916336, 0.0917193, 0.0967442, 0.0946218, 0.101878, 0.0994093, 0.104243, 0.109654, 0.118155, 0.112426, 0.116344, 0.125108, 0.127717, 0.123506, 0.125227, 0.12702, 0.134878, 0.13838, 0.129947, 0.14118};
static double dsBG1[49] = { 0.0039792, 0.00770391,0.0138123,0.0160307,0.018476, 0.0195815,0.0225872,0.022327, 0.0277712,0.0328081,0.0344941,0.0375329,0.0372013,0.0438044,0.0492287,0.049246,0.0529514,0.0538343,0.0551339,0.0602985,0.0591826,0.0609475,0.0666318,0.0652344,0.0747834,0.0781232,0.0769915,0.0807583,0.0813425,0.0898694,0.0897154,0.0903464,0.091853,0.0999071,0.100018,0.103706,0.10664,0.106524,0.112548,0.111782,0.11566,0.117054,0.118499,0.125868,0.131495,0.13227,0.130564,0.133745,0.139985};
static double*dsBG=dsBG2;


static double QuenMin(double E)
{   double X[]={ 134.3, 159.5, 184.5, 208.5, 234.0, 271.5, 308.5, 342.5, 376.5, 409.0, 439.0, 469.5, 501.5, 531.5, 564.5, 597.5, 630.5, 677.0};
    double Y[]={ 212.3, 213.5, 213.5, 214.0, 214.0, 214.5, 217.5, 225.0, 235.0, 250.5, 269.0, 290.0, 308.5, 326.5, 343.0, 356.5, 367.0, 379.0};
    double x= 270.5+ (623-270.5)*0.5*log10(E);
    if(x<134.3) x=134.3;
    return   10*(polint3(x,18,X,Y)-399)/(44.5-399);  
}




static double QuenMax(double E)
{   double X[]={128.0, 238.5, 296.0, 350.0, 398.0, 445.0, 482.5, 510.5, 538.5, 570.5, 601.0, 644.5, 679.5};
    double Y[]={ 91.0,  99.5, 109.0, 135.0, 174.0, 220.0, 257.0, 282.0, 306.5, 325.5, 344.0, 361.0, 371.0};
    double x= 270.5+ (623-270.5)*0.5*log10(E);
     if(x<128) x=128;
    return   10*(polint3(x,13,X,Y)-399)/(44.5-399);  
}

static double quenchingArrE[100],quenchingArrN[100];

void  setQuenching(double quenchX)
{  
   double step=1;
   for(int i=0;i<100;i++) 
   { double E=DS_E1ion+i*step;
     quenchingArrE[i]=E;
     quenchingArrN[i]= (E-DS_E1ion)*(QuenMin(E)*(1-quenchX) + QuenMax(E)*quenchX);
   }  
}


/*static*/ double Ne(double E) { return polint3(E,100, quenchingArrE,quenchingArrN);  }
static double En(double n ){ return polint3(n,100, quenchingArrN,quenchingArrE);}


static double dNdn(double Ne,double *dNdE)
{
  double E=En(Ne);
  double dEnrdN=En(Ne+0.5)-En(Ne-0.5);
  return dNdERecoil(E,dNdE)*dEnrdN;
}



static double  smoothBin(double x, double * arr) // using Gauss distribution for S2 photons
{ double res=0;
  for(int n=1;n<50;n++)
  {
//     double w=sqrt(n/toS2);
//     double w=resolution*n;
     double w=resolution*2*sqrt(n);
//     double w=resolution*4;
     double d=(x-n)/w;
     d*=d*0.5;
     if(d<8) res+=arr[n]*exp(-d)/w;
  }   
  
  return res/sqrt(2*M_PI);
}

double n_PoissonI(double E, double*LnNorm)
{   

#define TAB 

#ifdef TAB
  double EE[80]= {1.960000E-02,2.175600E-02,2.414916E-02,2.680557E-02,2.975418E-02,3.302714E-02,3.666013E-02,4.069274E-02,4.516894E-02,5.013752E-02,5.565265E-02,6.177444E-02,6.856963E-02,7.611229E-02,8.448464E-02,9.377795E-02,1.040935E-01,1.155438E-01,1.282536E-01,1.423615E-01,1.580213E-01,1.754036E-01,1.946981E-01,2.161148E-01,2.398875E-01,2.662751E-01,2.955654E-01,3.280775E-01,3.641661E-01,4.042243E-01,4.486890E-01,4.980448E-01,5.528297E-01,6.136410E-01,6.811415E-01,7.560671E-01,8.392345E-01,9.315502E-01,1.034021E+00,1.147763E+00,1.274017E+00,1.414159E+00,1.569716E+00,1.742385E+00,1.934048E+00,2.146793E+00,2.382940E+00,2.645063E+00,2.936020E+00,3.258983E+00,3.617471E+00,4.015392E+00,4.457086E+00,4.947365E+00,5.491575E+00,6.095648E+00,6.766170E+00,7.510448E+00,8.336598E+00,9.253623E+00,1.027152E+01,1.140139E+01,1.265554E+01,1.404765E+01,1.559289E+01,1.730811E+01,1.921200E+01,2.132532E+01,2.367111E+01,2.627493E+01,2.916517E+01,3.237334E+01,3.593441E+01,3.988720E+01,4.427479E+01,4.914502E+01,5.455097E+01,6.055157E+01,6.721225E+01,7.460559E+01};
  double NP[80]= {1.053731E-01,1.183208E-01,1.330598E-01,1.498755E-01,1.691416E-01,1.912844E-01,2.168569E-01,2.463418E-01,2.785055E-01,3.133974E-01,3.515373E-01,3.934742E-01,4.398356E-01,4.910893E-01,5.478160E-01,6.105662E-01,6.800317E-01,7.570604E-01,8.423739E-01,9.369330E-01,1.041606E+00,1.157723E+00,1.286360E+00,1.428729E+00,1.586506E+00,1.761318E+00,1.954945E+00,2.169157E+00,2.406572E+00,2.669014E+00,2.959159E+00,3.280274E+00,3.635186E+00,4.027296E+00,4.459859E+00,4.937917E+00,5.464697E+00,6.044936E+00,6.684287E+00,7.388465E+00,8.165267E+00,9.018511E+00,9.951521E+00,1.096925E+01,1.207303E+01,1.325881E+01,1.453128E+01,1.589787E+01,1.737345E+01,1.897514E+01,2.069493E+01,2.250756E+01,2.437644E+01,2.631492E+01,2.832828E+01,3.039910E+01,3.251796E+01,3.466244E+01,3.683794E+01,3.903911E+01,4.121272E+01,4.333791E+01,4.553306E+01,4.793401E+01,5.058000E+01,5.338358E+01,5.622970E+01,5.895480E+01,6.147749E+01,6.387346E+01,6.628838E+01,6.886196E+01,7.153097E+01,7.424462E+01,7.700729E+01,7.977687E+01,8.257838E+01,8.541896E+01,8.830548E+01,9.125225E+01};
  double LnN[80]={5.374736E-04,1.219468E-02,2.529386E-02,4.003475E-02,5.665559E-02,7.542802E-02,9.668006E-02,1.207538E-01,1.475529E-01,1.772512E-01,2.101761E-01,2.466971E-01,2.872721E-01,3.323107E-01,3.823081E-01,4.377572E-01,4.992578E-01,5.675345E-01,6.432472E-01,7.272366E-01,8.202991E-01,9.235770E-01,1.038057E+00,1.164842E+00,1.305398E+00,1.461184E+00,1.633796E+00,1.824856E+00,2.036649E+00,2.270897E+00,2.530001E+00,2.816852E+00,3.134047E+00,3.484668E+00,3.871727E+00,4.299682E+00,4.771624E+00,5.291882E+00,5.865572E+00,6.497926E+00,7.195906E+00,7.963396E+00,8.803957E+00,9.722507E+00,1.072115E+01,1.179771E+01,1.295702E+01,1.420624E+01,1.555859E+01,1.702936E+01,1.861347E+01,2.029163E+01,2.203483E+01,2.385476E+01,2.575650E+01,2.772613E+01,2.975597E+01,3.182707E+01,3.394356E+01,3.610035E+01,3.825071E+01,4.037475E+01,4.257417E+01,4.496889E+01,4.759589E+01,5.037953E+01,5.321750E+01,5.596138E+01,5.853400E+01,6.099999E+01,6.348998E+01,6.613215E+01,6.886896E+01,7.165322E+01,7.448854E+01,7.733490E+01,8.021506E+01,8.313526E+01,8.610161E+01,8.912747E+01};
  *LnNorm=polint3(E,80,EE,LnN); 
  return polint3(E,80,EE,NP); 
#else


  int  nMax=E/DS_E1ion;
  if(nMax<=0)  return 0;
   setQuenching(0);
  double ne_=Ne(E);
//  printf("ne_=%E nMax=%d\n",ne_,nMax);
  if(ne_>nMax) return 0; // ?????
  double delta=0.5;
  double ne__=ne_;
  for(;;)
  { 
     double normX=0;
     double neX=0;
     double lnCbin=0;
     double normX_=0;     
     for(int ne=0;ne<=nMax;ne++) 
     {  double c=exp(ne*log(ne__*(1-ne*DS_E1ion/E))-lnCbin);
        double cc=exp(ne*log(ne__)-lnCbin);
//printf("c=%E  exo(%E) ne__*(1-ne*DS_E1ion/E)=%E \n",c,ne*log(ne__*(1-ne*DS_E1ion/E))-lnCbin,ne__*(1-ne*DS_E1ion/E ));
        normX_+=cc;
        normX+=c;
        neX+=c*ne;
        lnCbin+=log(ne+1);
     } 
//     printf("ne_=%E ne__=%E, normX_*exp(-ne__)=%E normX*exp(-ne__)=%E\n", ne_,ne__,normX_*exp(-ne__), normX*exp(-ne__));
     if(delta<0.0001) { *LnNorm=log(normX); return ne__;}
     if(neX/normX>ne_) { ne__/=(1+delta);  delta/=2;}  else ne__*=1+delta; 
  }
#endif
#undef TAB
}


int  neSignal( int binFluctuation,  double *dNdE, double* binSignal) 
{
   double binS[50];  // no smothing, real ne distribution   
   for(int i=0;i<50;i++)  binS[i]=0;

   if(binFluctuation==1) 
   { 
     double Emax=maxRecoil(40);
     double step=Emax/100;
     for(double E=step/2; E<50; E+=step)
     {  
        double c=dNdERecoil(E,dNdE);
        if(c<=0) continue;
        int  nMax=E/DS_E1ion; 
        if(nMax<=0) continue;
        double ne_=Ne(E);
        if(ne_>nMax) continue;
//        if(ne_<0.5) continue;
        double  logP=log(ne_/nMax), log1P=log(1-ne_/nMax);
        double  Cbin=1;      
        if(E>2 && c==0) break; 
        for(int ne=0;(ne<=nMax)&&(ne<50);ne++)
        {  
          double q=Cbin*exp(ne*logP+(nMax-ne)*log1P);
          binS[ne]+=step*c*q;
//if(!isfinite(binS[ne])) { printf("E=%e c=%E  Mcdm=%e Cbin=%e ne=%d, ne_=%E  logP=%e logP1=%E\n",E,c,Mcdm,Cbin,ne,ne_,logP,log1P); exit(0);}            
          Cbin*=(nMax-ne); 
          Cbin/=(ne+1);
        }
     }
//     binS[0]=0;
//     printf("Mcdm=%E \n");
//       double ss=0;
//       for(int i=1;i<40;i++) {printf("binS[%d]=%E\n", i, binS[i]* DSExposure); ss+=binS[i];}
//       printf("ss before smoothing= %E\n",ss);
//     ss=0 ;
     for(int i=0; i<=neLast;i++) binSignal[i]=simpson_arg((funcArg)smoothBin,binS, i,i+1, 1E-3,NULL);  
//     for(int i=0;i<40;i++) {printf("binSignal[%d]=%E\n", i, binSignal[i]* DSExposure); ss+=binSignal[i];}
//      printf("ss after smoothing= %E\n",ss);
      
   }
   else if(binFluctuation==2) 
   { 
     double Emax=maxRecoil(40);
     double step=Emax/100;
     for(double E=step/2; E<50; E+=step)
     {  
        double c=dNdERecoil(E,dNdE);
        if(c<=0) continue;
        int  nMax=E/DS_E1ion; 
        if(nMax<=0) continue;
        double ne_=Ne(E);
        if(ne_>nMax) continue;
        double  logP=log(ne_/nMax), log1P=log(1-ne_/nMax);
        double  LnCbin=0;      
        if(E>2 && c==0) break; 
        
        double LnNorm;
        double ne__=ne_;
        ne__=n_PoissonI(E,&LnNorm);
        
        for(int ne=0;(ne<=nMax)&&(ne<50);ne++)
        { 
          double q;
           q= exp(ne*log(ne__*(1-ne*DS_E1ion/E))-LnNorm- LnCbin);
          binS[ne]+=step*c*q;
          LnCbin+=log(ne+1);
        }        
     }
int err; 
     for(int i=0; i<=neLast;i++) binSignal[i]=simpson_arg((funcArg)smoothBin,binS, i,i+1, 1E-3,&err);
if(err){
  for(int k=0;k<50;k++) printf("binS[%d]=%E\n",k,binS[k]);
    exit(0);  
 }     
   }
   else
   if(noBinCase==1)
   {
      double Emax=maxRecoil(40);
      double step=Emax/100;
      for(int i=0;i<=neLast;i++)  binSignal[i]=0;
      for(double E=step/2; E<50; E+=step)
      {     
          double c=dNdERecoil(E,dNdE);
          if(c<=0) continue;                                 
          {
             double ww=En(4)* sqrt(E/En(4))*resolution;
             for(int n=0;n<=neLast;n++)
             { binSignal[n]+=0.5*step*c*(erf( (En(n+1)-E)/M_SQRT2/ww)- erf( (En(n)-E)/M_SQRT2/ww));}                                                                                            
          }
      }
   }else
   {
      for(int i=1;i<50;i++)
      { 
         binS[i]=simpson_arg((funcArg)dNdERecoil,dNdE, En(i),En(i+1), 1E-3,NULL);
      }     
      binS[0]=0;                     
      for(int i=0; i<=neLast;i++) binSignal[i]=simpson_arg((funcArg)smoothBin,binS, i,i+1, 1E-3,NULL);
   }
      
//   double s=0, ss=0; 
//   for(int i=0;i<15;i++) {printf("i=%d S=%e  SS=%E  \n",i,binS[i],binSignal[i]); s+=binS[i];  ss+=binSignal[i];}
//   printf(" s=%E  ss=%E\n",s,ss);
}


double DSll(double c,double * binSignal)
{

  double l=1;
  for(int  n=DS_neStart;n<=neLast;n++)
  { 
     double b=dsBG[n]*DSbgFactor;
     double d=dsData[n];
     double s=binSignal[n]*c;

     double th0=b,th1=b+s;
     
     if(n<neB) 
     { if(d>=b+s) continue;
       if(b<d) th0=d; 
     }
          
     double cc= th0-th1 +d*log(th1/th0); 
     
     l*=exp(DSExposure*cc); 
  }
  return l;
}


static double  cDSllbest(double *binSignal)
{

  double c1=0.5,c2=1,c3=2, step=2;
  double f1,f2,f3; 

  f1=DSll(c1,binSignal); 
  if(f1==1)     
  {  while(f1==1) { c1*=2; f1=DSll(c1,binSignal);} 
     c2=2*c1;  f2=DSll(c2,binSignal);
     c3=2*c2;  f3=DSll(c3,binSignal);
  }
  else if(f1==0) 
  { c3=c1; f3=f1;
    while(f3==0) { c3/=2; f3=DSll(c3,binSignal);}
    c2=c3/2; f2=DSll(c2,binSignal);
    c1=c2/2; f1=DSll(c1,binSignal); 
  }
  else{ f2=DSll(c2,binSignal); f3=DSll(c3,binSignal); } 
 
  for(;;)
  { 
         if(f1<f2 && f2<f3) { c1=c2; f1=f2; c2=c3; f2=f3; c3=step*c3;f3=DSll(c3,binSignal);}
    else if(f1>f2 && f2>f3) { c3=c2; f3=f2; c2=c1; f2=f1; c1=c1/step;f1=DSll(c1,binSignal);}
    else { c3=c2;f3=f2; c2=sqrt(c1*c3); f2=DSll(c2,binSignal); step=sqrt(step);}
    if( fabs(step-1)<1E-3 && fabs(f1/f2-1)<1E-3 && fabs(f2/f3-1)<1E-3) return c2;  
  }
}  
  
static double DSllExclude(double pval, double *binSignal)
{
   
  double c1=1,c2=0.5,f1=0,f2=0,c_,f_;

  c2=cDSllbest(binSignal);  
  f2=DSll(c2,binSignal);
  pval*=f2;

  for( ;f2>pval; ) { c1=c2; f1=f2;   c2*=2; f2=DSll(c2,binSignal);}
  for( ; fabs(log(c1/c2))>1E-3; ) 
  {
    c_=sqrt(c1*c2);
     f_=DSll(c_,binSignal); 
     if(f_<pval) { c2=c_; f2=f_;} else { c1=c_;f1=f_;}
  }   
   
  return sqrt(c1*c2);
} 




//=======================================================

double DSllQ(int binFluctuation, double c, double *dNdE)
{  
  double dll5[10];
  double xx[10];
   double binSignal[50];
 //  setQuenching(0);
 //  neSignal( binFluctuation,  dNdE, binSignal);
 //  return DSll(c,binSignal);
     
  for(int i=0;i<10;i++) 
  {  double binSignal[50];
     double Q=0.05+0.1*i;
     xx[i]=Q;
     setQuenching(Q);
     neSignal(neFluct,  dNdE, binSignal);
     dll5[i]=DSll(c,binSignal);
     dll5[i]*=exp(-0.5*(Q/0.25-1)*(Q/0.25-1));
//for(int k=0;k<20;k++) printf("binSignal[%d]=%e\n",k,binSignal[k]);     
  }
//  displayPlot("DllQ","Q",0,1,0,1,"dll",10,dll5,NULL);
  double max=0;
  double x0=0;
  for(double x=0;x<1;x+=0.01) { double m=polint3(x,10,xx,dll5); if(m>max){ max=m; x0=x;} }
//  printf("Q=%E\n",x0);
  return max;
}


static double  cDSllbestQ(int binFluctuation,  double *dNdE)
{

  double c1=1,c2=0.5,f1=0,f2=0,c_,f_;

  while(f1==0 || f2==0)
  { c1/=2;c2/=2;
    f1=DSllQ(binFluctuation, c1, dNdE);
    f2=DSllQ(binFluctuation, c2, dNdE);
  }   
  if(f2<f1) { c_=c1; c1=c2; c2=c_; f_=f1;f1=f2;f2=f_;} 
 
  while ( c1<c2 ) { c1=c2*2; f1=DSllQ(binFluctuation,c1,dNdE); if(f1>f2){ c_=c1; c1=c2; c2=c_; f_=f1;f1=f2;f2=f_;} }
   
  for(; fabs(f2/f1-1)>1E-3; )
  {  
     c_=c2*c2/c1; f_=DSllQ(binFluctuation,c_,dNdE);
         
     if(f_<f2) 
     { c_=sqrt(c1*c2); f_=DSllQ(binFluctuation,c_,dNdE);
       if(f_>f2) {c1=c2;f1=f2;c2=c_;f2=f_;} else { c1=c_;f1=f_;}
     } 
     else  { c1=c2; f1=f2; c2=c_; f2=f_;}
  }   
  return c2;
}  


double DSllExcludeQ(int binF,double pval, double *dNdE)
{
   
  double c1=1,c2=0.5,f1=0,f2=0,c_,f_;

  c2=cDSllbestQ(binF,dNdE);  
  f2=DSllQ(binF,c2,dNdE);
  pval*=f2;

  for( ;f2>pval; ) { c1=c2; f1=f2;   c2*=2; f2=DSllQ(binF,c2,dNdE);}
  for( ; fabs(log(c1/c2))>1E-3; ) 
  {
    c_=sqrt(c1*c2);
     f_=DSllQ(binF,c_,dNdE); 
     if(f_<pval) { c2=c_; f2=f_;} else { c1=c_;f1=f_;}
  }   
   
  return sqrt(c1*c2);
} 

SxxType* XENON1T_2018_sdXe129=SxxXe129SHELL;
SxxType* XENON1T_2018_sdXe131=SxxXe131SHELL;
SxxType* PICO_2019_sdF19=SxxF19EFT;


int setSpinDepFF( int experiment, int name_of_FF_set)
{
    switch(experiment)
    {
      case  XENON1T_2018 :
        switch(name_of_FF_set)
        {
            case EFT: 
            XENON1T_2018_sdXe129=SxxXe129EFT;
            XENON1T_2018_sdXe131=SxxXe131EFT;                              return 0;   
          case SHELL:
            XENON1T_2018_sdXe129=SxxXe129SHELL;
            XENON1T_2018_sdXe131=SxxXe131SHELL;
            return 0;
          case SHELLm:
            XENON1T_2018_sdXe129=SxxXe129SHELLm;
            XENON1T_2018_sdXe131=SxxXe131SHELLm;                           return 0;
          default: printf("Unknown form factor set for  XENON1T_2018\n");  return 1;
        }      
     case PICO_2019:
       switch(name_of_FF_set)
       { 
          case EFT:
            PICO_2019_sdF19=SxxF19EFT;                                      return 0;
          case SHELL:
            PICO_2019_sdF19=SxxF19SHELL;                                    return 0;
          case SHELLm:
            PICO_2019_sdF19=SxxF19SHELLm;                                   return 0;     
          default: printf("Unknown form factor  set for  PICO_2019\n");     return 1; 
       }  
       
      case CRESST_2019:
            printf("Curently CRESST_2019 does not use Spin Dependent form factor.\n"); return 1;
      case  DarkSide_2018:
            printf("DarkSide_2018  does not check  Spin Dependent signal.\n"); return 1;
      default: printf(" First argument does not correcponds to direct detection experiment excorted by micrOMEGAs\n");
    } 
}



static double *dNdE_XENON1T_2018=NULL,  *dNdE_DarkSide_2018=NULL, *dNdE_PICO_2019=NULL,*dNdE_CRESST_2019;

static double PICObg=1.47;
static double PICOdTr=1.55;


static double DD_factor_(double pval,char**expName)
{ 
  double ff=0,ff_;
  double *dNdE;
  *expName="";
  dNdE=dNdE_XENON1T_2018;
  if(dNdE)
  { 
     double Emax=maxRecoil(131);
     if(Emax>15)  Emax=15;
     if(Emax>1.69)
     {
       ff_= -(log(pval)+BgXe1T)/(900*279*simpson_arg((funcArg)dNdERecoil,dNdE, 1.69,Emax,1E-3,NULL));
       if( isfinite(ff_) &&  (ff==0 ||  ff_<ff) ) { ff=ff_;  *expName="XENON1T_2018";}
     }   
  } 

  dNdE=dNdE_CRESST_2019;
  
  if(dNdE)
  { 
     ff_=CRESST_III_UpperLim(pval,dNdE);
     if( isfinite(ff_) &&  (ff==0 ||  ff_<ff) ) { ff=ff_;  *expName="CRESST_2019"; } 
  }   
   
  dNdE=dNdE_DarkSide_2018;
  if(dNdE)
  { 
     setQuenching(xQuenching);
     double binSignal[50];
     neSignal(neFluct, dNdE, binSignal);
     if(binSignal[DS_neStart]==0) ff_=sqrt(-1);
     else  ff_=DSllExclude(pval, binSignal);        
     if( isfinite(ff_) &&  (ff==0 ||  ff_<ff) ) { ff=ff_;  *expName="DarkSide_2018";}
  }
  
  dNdE=dNdE_PICO_2019;
  if(dNdE)
  {   
    double Emax=maxRecoil(19);
    double nEvents=1404*simpson_arg((funcArg)dNdERecoil,dNdE,2.45+PICOdTr,3.3+PICOdTr,1E-3,NULL);
    
    if(3.3+PICOdTr<Emax)  nEvents+=(1404+1167)*simpson_arg((funcArg)dNdERecoil,dNdE,3.3+PICOdTr,Emax,1E-3,NULL);   

//displayPlot("PICO EVENTS","E[KeV]", 2.45+PICOdTr, Emax,0,1,"",0, dNdERecoil, dNdE);
//printf("PICO nEvents=%e\n", nEvents);           

    double nEv=3; 
    if(pval<0.01)
    { nEv=3;
      for(double nEv_;;) { nEv_=nEv; nEv=3-log(pval) -3*log(3/nEv);  if(fabs(nEv-nEv_)<= 0.001*nEv) break; }
      nEv-=PICObg;
    } else nEv= FeldmanCousins(3, PICObg,1-pval);
    
    ff_=nEv/nEvents; //*0.75;
    
    if( isfinite(ff_) &&  (ff==0 ||  ff_<ff) ) { ff=ff_;  *expName="PICO_2019";} 
  } 
  if(*expName=="") return sqrt(-1);
  return ff;
}


static double DD_pval_(double s, char**expName)
{  
  double pval=1,pval_;
  double *dNdE;
  
  dNdE=dNdE_XENON1T_2018;
  if(dNdE)
  { 
     double Emax=maxRecoil(131);
     if(Emax>15) Emax=15;
     if(Emax>1.69)
     {  
       pval_=exp(- s*900*279*simpson_arg((funcArg)dNdERecoil,dNdE, 1.69,Emax,1E-3,NULL) -BgXe1T);
       if(isfinite(pval_))
       {  if(!expName) pval*=pval_; else if(pval_<pval) { pval=pval_; *expName="XENON1T_2018";}}
     }  
  } 

  dNdE=dNdE_CRESST_2019;  
  if(dNdE)
  {
     int lm=0,N=0;
     double m=0;
     double pval1=0.2, pval2=0.005;
     
     double s1=CRESST_III_UpperLim(pval1,dNdE), s2=CRESST_III_UpperLim(pval2,dNdE); // s2>s1 
     double ds=s2-s1;
     if(s1<=s  && s<=s2)  for(;;)
     {
       pval_=(s*(pval1-pval2)+s1*pval2-s2*pval1)/(s1-s2);       
       double s_=CRESST_III_UpperLim(pval_,dNdE);
       if(fabs(s-s_)<0.01*ds) break; 
       if(s_<s) {s1=s_;pval1=pval_;} else { s2=s_; pval2=pval_;} 
     } else
     {
        if(s>s2) { double s0=(s2-s1)/log(pval1/pval2), c0=pval2*exp(s2/s0); pval_=c0*exp(-s/s0);}
        else  pval_=1-s/s1*(1-pval1);  
     }
     if(isfinite(pval_))
     {  if(!expName) pval*=pval_; else if(pval_<pval) { pval=pval_; *expName="CRESST_2019";}}
  } 


  dNdE=dNdE_DarkSide_2018;  
  if(dNdE)
  { 
     setQuenching(xQuenching);
     double binSignal[50];
     neSignal(neFluct, dNdE, binSignal);
     if(binSignal[DS_neStart]==0) pval_=sqrt(-1);
     else
     {
       for(int i=0;i<50;i++) binSignal[i]*=s;
       pval_=  DSll(1,binSignal)/DSll(cDSllbest(binSignal),binSignal);
     }     
     if(isfinite(pval_))
     {  if(!expName) pval*=pval_; else if(pval_<pval) { pval=pval_; *expName="DarkSide_2018";}}     
  } 

  dNdE=dNdE_PICO_2019;  
  if(dNdE)
  { 
    double Emax=maxRecoil(19);
    double nEvents=1404*simpson_arg((funcArg)dNdERecoil,dNdE,2.45+PICOdTr,3.3+PICOdTr,1E-3,NULL);
    if(3.3+PICOdTr<Emax) nEvents+=(1404+1167)*simpson_arg((funcArg)dNdERecoil,dNdE,3.3+PICOdTr,Emax,1E-3,NULL);
     
    nEvents*=s;           
    if(nEvents>10.5) pval_=pow((nEvents+PICObg)/3,3)/exp(PICObg+nEvents-3); 
    else if(nEvents<2.5) pval_=1; 
    else
    { double p1=0.01, n1=FeldmanCousins(3, PICObg,1-p1), p2=0.99,n2=FeldmanCousins(3,PICObg,1-p2);
    
//printf(" n1=%E n2=%E nEvents=%E \n", n1,n2,nEvents);
//exit(0);    
      for(;;) 
      { 
//        printf("px=%E\n",0.5*(p1+p2));   
           double px=0.5*(p1+p2), nx=FeldmanCousins(3, PICObg,1-px);
        
//        printf("px=%E nx=%E\n",px, nx);   
          if(fabs(nx-nEvents)<0.01) {pval_=px; break;}
          if(fabs(p1-p2)<1E-3*(p1+p2)) {pval_=0.5*(p1+p2); break;}
          if(nx>nEvents) { p1=px; n1=nx;}
          else { p2=px;n2=nx;}
//          printf("                       p1=%E   n1=%E nx=%E p2=%E n2=%E\n", p1,n1,nx,p2,n2);                 
      }
    }
    if(isfinite(pval_)) 
    {  if(!expName) pval*=pval_; else if(pval_<pval) { pval=pval_; *expName="PICO_2019";}}         
  }

  return pval;
}

static double  LLAll(double s) { return DD_pval_(s,NULL); }


static double  LLbest(double (*LL)(double))
{

  double c1=0.5,c2=1,c3=2, step=2;
  double f1,f2,f3; 

  f1=LL(c1); 
  if(f1==1)     
  {  while(f1==1) { c1*=2; f1=LL(c1);} 
     c2=2*c1;  f2=LL(c2);
     c3=2*c2;  f3=LL(c3);
  }
  else if(f1<1E-40) 
  { c3=c1; f3=f1;
    while(f3<1E-40) { c3/=2; f3=LL(c3);}
    c2=c3/2; f2=LL(c2);
    c1=c2/2; f1=LL(c1); 
  }
  else{ f2=LL(c2); f3=LL(c3); } 

//printf("f(0)=%E   f(%e)=%e f(%e)=%e\n", LL(0), c2,f2,c3,f3); 
  for(;;)
  { 
         if(f1<f2 && f2<f3) { c1=c2; f1=f2; c2=c3; f2=f3; c3=step*c3;f3=LL(c3);}
    else if(f1>f2 && f2>f3) { c3=c2; f3=f2; c2=c1; f2=f1; c1=c1/step;f1=LL(c1);}
    else { c3=c2;f3=f2; c2=sqrt(c1*c3); f2=LL(c2); step=sqrt(step);}
//printf("step=%E f1=%e f2=%E f3=%e\n",step,f1,f2,f3);    
    if( fabs(step-1)<1E-3 && fabs(f1/f2-1)<1E-3 && fabs(f2/f3-1)<1E-3) return c2;  
  }
}  
  
static double LLexclude(double pval, double (*LL)(double))
{
   
  double c1=1,c2=0.5,f1=0,f2=0,c_,f_;
  c2=LLbest(LL);
    
  f2=LL(c2); 
  pval*=f2;
  for( ;f2>pval; ) { c1=c2; f1=f2;   c2*=2; f2=LL(c2);}
  for( ; fabs(log(c1/c2))>1E-3; ) 
  {  
     c_=sqrt(c1*c2);
     f_=LL(c_);     
     if(f_<pval) { c2=c_; f2=f_;} else { c1=c_;f1=f_;}
  }   
  
  return sqrt(c1*c2);
} 



static int  initDDexpCS( unsigned int Experiments, double(*vfv)(double),double cs_SI_P, double cs_SI_N,  double cs_SD_P, double cs_SD_N)
{
    int nEx=0,nEx_mem=0; 
    double  dNdE[RE_DIM];
    double  dNdE_[RE_DIM];

    if((Experiments &XENON1T_2018) && maxRecoil(131)>1.69  )
    { 
      nucleusRecoilCS(vfv,131,Z_Xe,J_Xe131,XENON1T_2018_sdXe131,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N,dNdE_); 
      for(int i=0;i<RE_DIM;i++) dNdE[i]=0.218*dNdE_[i];
      nucleusRecoilCS(vfv,129,Z_Xe,J_Xe129,XENON1T_2018_sdXe129,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N, dNdE_);
      for(int i=0;i<RE_DIM;i++) dNdE[i]+=0.262*dNdE_[i];
      nucleusRecoilCS(vfv,132,Z_Xe,0.,NULL,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N, dNdE_);
      for(int i=0;i<RE_DIM;i++) dNdE[i]+=(1-0.218-0.262)*dNdE_[i];    
      if(dNdEfact) for(int n=0;n<RE_DIM;n++) dNdE[n]*=dNdEfact(RE_START*pow(RE_STEP,n),130);
      for(int i=0;i<RE_DIM;i++) dNdE[i]*=p0Z1T_best(RE_START*pow(RE_STEP,i) );
   
      for(int k=0;k<RE_DIM;k++) if(dNdE[k]>0)
      {
         dNdE_XENON1T_2018=realloc(dNdE_XENON1T_2018,sizeof(double)*RE_DIM);
         for(int i=0;i<RE_DIM;i++) dNdE_XENON1T_2018[i]=dNdE[i];
         nEx++;
         break;
      }     
    }
    if(nEx==nEx_mem && dNdE_XENON1T_2018) { free(dNdE_XENON1T_2018); dNdE_XENON1T_2018=NULL;}
    
    nEx_mem=nEx;    
    if(Experiments & DarkSide_2018)
    {   
       nucleusRecoilCS(vfv,40,18 ,0,NULL,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N, dNdE);
       if(dNdEfact) for(int n=0;n<RE_DIM;n++) dNdE[n]*=dNdEfact(RE_START*pow(RE_STEP,n),40);
       for(int k=0;k<RE_DIM;k++) if(dNdE[k]>0)
       {
          dNdE_DarkSide_2018  =realloc( dNdE_DarkSide_2018, sizeof(double)*RE_DIM); 
          for(int i=0;i<RE_DIM;i++)dNdE_DarkSide_2018[i]=dNdE[i];
          nEx++;
          break;
       }   
    } 
    if(nEx==nEx_mem && dNdE_DarkSide_2018) { free(dNdE_DarkSide_2018); dNdE_DarkSide_2018=NULL;}
    
    nEx_mem=nEx;
    if((Experiments & PICO_2019) && maxRecoil(19)>2.45+PICOdTr  )
    {
      
      double  xF=8*19./(8*19.+3*12);
      double  xC=1-xF;    
      nucleusRecoilCS(vfv,19,Z_F,J_F19,PICO_2019_sdF19,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N, dNdE);      
      if(dNdEfact) for(int n=0;n<RE_DIM;n++) dNdE[n]*=dNdEfact(RE_START*pow(RE_STEP,n),19);
      nucleusRecoilCS(vfv,12,6,0,NULL,cs_SI_P, cs_SI_N,  cs_SD_P, cs_SD_N, dNdE_);
      if(dNdEfact) for(int n=0;n<RE_DIM;n++) dNdE_[n]*=dNdEfact(RE_START*pow(RE_STEP,n),12);  
      for(int k=0;k<RE_DIM;k++) if(dNdE[k]>0)
      {    
        dNdE_PICO_2019=realloc(dNdE_PICO_2019,sizeof(double)*RE_DIM); 
        for(int i=0;i<RE_DIM;i++) dNdE_PICO_2019[i]=xF*dNdE[i]+xC*dNdE_[i];
        nEx++;
        break;
      }  
    } 
    if(nEx==nEx_mem && dNdE_PICO_2019) {free(dNdE_PICO_2019); dNdE_PICO_2019=NULL;}  
    
    nEx_mem=nEx;
    if((Experiments & CRESST_2019))
    { double dNdECa[RE_DIM], dNdEW[RE_DIM], dNdEO[RE_DIM], dNdEO17[RE_DIM]; 
      double  xCa=  40/(40.+184.+4*16.);
      double  xW=  184/(40.+184.+4*16.);
      double  xO= 4*16/(40.+184.+4*16.);  

      nucleusRecoilCS(vfv,40,Z_Ca,0,NULL,cs_SI_P, cs_SI_N,  0, 0, dNdECa);
      nucleusRecoilCS(vfv,184,Z_W,0,NULL,cs_SI_P, cs_SI_N,  0, 0, dNdEW);
      nucleusRecoilCS(vfv,16,Z_O,0,NULL, cs_SI_P, cs_SI_N,  0, 0, dNdEO);
      nucleusRecoil0CS(vfv,17,Z_O,J_O17,0,Sn_O17,cs_SI_P,cs_SI_N,0,cs_SD_N,dNdEO17);        
      
      for(int n=0;n<RE_DIM;n++)
      { double E=RE_START*pow(RE_STEP,n);
        if(E>17) dNdE[n]=0; else
        { if(dNdEfact) dNdE[n]=xCa*dNdEfact(E,40)* CRESSTeff(E,"Ca")*dNdECa[n]
                              +xW *dNdEfact(E,184)*CRESSTeff(E,"W")* dNdEW[n]
                              +xO* dNdEfact(E,16)* CRESSTeff(E,"O")* dNdEO[n]
                              +xO*0.000367*dNdEfact(E,17)*CRESSTeff(E,"O")*dNdEO17[n];
          else         dNdE[n]=xCa*CRESSTeff(E,"Ca")*dNdECa[n]
                              +xW *CRESSTeff(E,"W")* dNdEW[n]
                              +xO* CRESSTeff(E,"O")* dNdEO[n]
                              +xO*0.000367*CRESSTeff(E,"O")*dNdEO17[n];            
        }
        
      }
      
/*    
char mess[30];
sprintf(mess,"Mcdm=%e\n",Mcdm);        
displayPlot(mess,"E[keV]",0.001,0.1,1,3,"Ca",0,dNdERecoil,dNdECa
                                        ,"W",0,dNdERecoil,dNdEW
                                        ,"O",0,dNdERecoil,dNdEO ); 
*/      
     dNdE_CRESST_2019=realloc(dNdE_CRESST_2019,sizeof(double)*RE_DIM);
     for(int k=0;k<RE_DIM;k++) if(dNdE[k]>0)
     {    
        for(int i=0;i<RE_DIM;i++)
        {  eCresst=RE_START*pow(RE_STEP,i);
           double Emin=eCresst-nSigmaCresst*sigmaCresst;
           if(Emin<RE_START) Emin=RE_START;
           dNdE_CRESST_2019[i]=simpson_arg(CRESST_smooth, dNdE ,Emin,eCresst+nSigmaCresst*sigmaCresst,1E-2,NULL);
           dNdE_CRESST_2019[i]*=CRESSTeff(eCresst,"Eff");           
        }
//char mess[30];
//sprintf(mess,"Mcdm=%e\n",Mcdm);        
//displayPlot(mess,"E[keV]",0.0001,0.1,1,1,"",0,dNdERecoil,dNdE_CRESST_2019);
        nEx++;    
        break; 
      }  
    } 
    if(nEx==nEx_mem && dNdE_CRESST_2019) {free(dNdE_CRESST_2019); dNdE_CRESST_2019=NULL;}  
    
  return nEx;
}


double DD_pvalCS(unsigned int Experiments, double(*vfv)(double), double cs_SI_P, double cs_SI_N,  double cs_SD_P, double cs_SD_N,char**expName)
{  
  if(expName) *expName="";
  if( !isfinite(cs_SI_P) || !isfinite(cs_SI_N) || !isfinite(cs_SD_P)|| !isfinite(cs_SD_N)) return 1;
  if(!initDDexpCS(Experiments,vfv,cs_SI_P, cs_SI_N, cs_SD_P, cs_SD_N)) return 1;
  
  if(!expName) return LLAll(1)/LLAll(LLbest(LLAll));
  
  return DD_pval_(1,expName);
  
}

double DD_factorCS(unsigned int Experiments, double pval, double(*vfv)(double), double cs_SI_P, double cs_SI_N,  double cs_SD_P, double cs_SD_N,char**expName)
{ 
  double ff;
  if( !isfinite(cs_SI_P) || !isfinite(cs_SI_N) || !isfinite(cs_SD_P)|| !isfinite(cs_SD_N)) return sqrt(-1);
  if(!initDDexpCS(Experiments,vfv,cs_SI_P, cs_SI_N, cs_SD_P, cs_SD_N)) return sqrt(-1);
  

//  displayPlot("LLAll","s",500,700,0,1,"",0,LLAll,NULL); exit(0); 

  if(!expName){  return LLexclude(pval,LLAll);}
  
  ff=DD_factor_(pval,expName);
  return ff;
}

static int  initDDexp( unsigned int Experiments, double(*vfv)(double))
{
    int nEx=0,nEx_mem; 
    double  dNdE[RE_DIM];
    double  dNdE_[RE_DIM];

    if((Experiments &XENON1T_2018) && maxRecoil(131)>1.69 )
    {
      nucleusRecoil(vfv,131,Z_Xe,J_Xe131,XENON1T_2018_sdXe131,dNdE_); 
      for(int i=0;i<RE_DIM;i++) dNdE[i]=0.218*dNdE_[i];
      nucleusRecoil(vfv,129,Z_Xe,J_Xe129,XENON1T_2018_sdXe129,dNdE_);
      for(int i=0;i<RE_DIM;i++) dNdE[i]+=0.262*dNdE_[i];
      nucleusRecoil(vfv,132,Z_Xe,0.,NULL,dNdE_);
      for(int i=0;i<RE_DIM;i++) dNdE[i]+=(1-0.218-0.262)*dNdE_[i];

      dNdE_XENON1T_2018=realloc(dNdE_XENON1T_2018,sizeof(double)*RE_DIM);
      for(int i=0;i<RE_DIM;i++) dNdE_XENON1T_2018[i]=dNdE[i]*p0Z1T_best(RE_START*pow(RE_STEP,i) );
      nEx++;     
    } else  if(dNdE_XENON1T_2018) { free(dNdE_XENON1T_2018); dNdE_XENON1T_2018=NULL;}
        
    if(Experiments & DarkSide_2018)
    {  
       dNdE_DarkSide_2018  =realloc( dNdE_DarkSide_2018, sizeof(double)*RE_DIM); 
       nucleusRecoil(vfv,40,18 ,0,NULL,dNdE_DarkSide_2018);
       nEx++;
    } else  if( dNdE_DarkSide_2018) { free(dNdE_DarkSide_2018); dNdE_DarkSide_2018=NULL;}
    
    if((Experiments & PICO_2019) && maxRecoil(19)>2.45+1.6 )
    {
      double  xF=8*19./(8*19.+3*12);
      double  xC=1-xF;    
      nucleusRecoil(vfv,19,Z_F,J_F19,PICO_2019_sdF19,dNdE);       
      nucleusRecoil(vfv,12,6,0,NULL,dNdE_);
      dNdE_PICO_2019=realloc(dNdE_PICO_2019,sizeof(double)*RE_DIM); 
      for(int i=0;i<RE_DIM;i++) dNdE_PICO_2019[i]=xF*dNdE[i]+xC*dNdE_[i]; 
      nEx++;
    } else if(dNdE_PICO_2019) {free(dNdE_PICO_2019); dNdE_PICO_2019=NULL;}  

    nEx_mem=nEx;
    if((Experiments & CRESST_2019) )
    { double dNdECa[RE_DIM], dNdEW[RE_DIM], dNdEO[RE_DIM], dNdEO17[RE_DIM]; 
      double  xCa=  40/(40.+184.+4*16.);
      double  xW=  184/(40.+184.+4*16.);
      double  xO= 4*16/(40.+184.+4*16.);  

      nucleusRecoil(vfv,40,Z_Ca,0,NULL, dNdECa);
      nucleusRecoil(vfv,184,Z_W,0,NULL, dNdEW);
      nucleusRecoil(vfv,16,Z_O,0,NULL,  dNdEO);
      nucleusRecoil0(vfv,17,Z_O,J_O17,0,Sn_O17,dNdEO17);        
      
      for(int n=0;n<RE_DIM;n++)
      { double E=RE_START*pow(RE_STEP,n);
        if(E>17) dNdE[n]=0; else
        { if(dNdEfact) dNdE[n]=xCa*dNdEfact(E,40)* CRESSTeff(E,"Ca")*dNdECa[n]
                              +xW *dNdEfact(E,184)*CRESSTeff(E,"W")* dNdEW[n]
                              +xO* dNdEfact(E,16)* CRESSTeff(E,"O")* dNdEO[n]
                              +xO*0.000367*dNdEfact(E,17)*CRESSTeff(E,"O")*dNdEO17[n];
          else         dNdE[n]=xCa*CRESSTeff(E,"Ca")*dNdECa[n]
                              +xW *CRESSTeff(E,"W")* dNdEW[n]
                              +xO* CRESSTeff(E,"O")* dNdEO[n]
                              +xO*0.000367*CRESSTeff(E,"O")*dNdEO17[n];            
          }                 
      }          
      
      dNdE_CRESST_2019=realloc(dNdE_CRESST_2019,sizeof(double)*RE_DIM);
      for(int n=0;n<RE_DIM;n++) dNdE_CRESST_2019[n]=dNdE[n];
        
      for(int k=0;k<RE_DIM;k++) if(dNdE[k]>0)
      {    
        for(int i=0;i<RE_DIM;i++)
        {  eCresst=RE_START*pow(RE_STEP,i);
           double Emin=eCresst-nSigmaCresst*sigmaCresst;
           if(Emin<RE_START) Emin=RE_START;
           dNdE_CRESST_2019[i]=simpson_arg(CRESST_smooth, dNdE ,Emin,eCresst+nSigmaCresst*sigmaCresst,1E-2,NULL);
           dNdE_CRESST_2019[i]*=CRESSTeff(eCresst,"Eff");       
        }   
        nEx++;
        break;
      }  
    } 
    if(nEx==nEx_mem && dNdE_CRESST_2019) {free(dNdE_CRESST_2019); dNdE_CRESST_2019=NULL;}  
    
  return nEx;
}


double DD_pval(unsigned int Experiments, double(*vfv)(double), char**expName)
{  
  if(expName)*expName="";

  double pval=1,pval_;
  double *dNdE;
  char*eName=NULL;

  if(!initDDexp(Experiments, vfv)) return 1;

//  if(!expName)  displayPlot("LL","x",0,1.5,0,1,"",0, LLAll,NULL);  
 
  if(!expName) return LLAll(1)/LLAll(LLbest(LLAll));
  return DD_pval_(1, expName);
}


double DD_factor(unsigned int Experiments, double pval, double(*vfv)(double),char**expName)
{  
  if(!initDDexp(Experiments, vfv)) return sqrt(-1);

  if(!expName) return LLexclude(pval,LLAll);
  
  return DD_factor_(pval,expName);
}

