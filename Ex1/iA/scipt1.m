clear all
format short
clc
N=4;
A0=100;
fp=10;
% Caso 1
R1=2.5*N*1e3;
R2=25*N*1e3;
R3=R1;
R4=10*N*1e3;

% H=[n0]/[d1 d0]

n0_1 = -A0*R2*R3
d0_1 = A0*R3*R1 + R1*R3 - R1*R2 + R2*R3
d1_1 = (R1*R3 - R1*R2 + R2*R3)/(2*pi*fp)

% Caso 2
R1=2.5*N*1e3;
R2=2.5*N*1e3;
R3=R1;
R4=10*N*1e3;

% H=[n0]/[d1 d0]

n0_2 = -A0*R2*R3
d0_2 = A0*R3*R1 + R1*R3 - R1*R2 + R2*R3
d1_2 = (R1*R3 - R1*R2 + R2*R3)/(2*pi*fp)

% Caso 3
R1=25*N*1e3;
R2=2.5*N*1e3;
R3=R1;
R4=100*N*1e3;

% H=[n0]/[d1 d0]

n0_3 = -A0*R2*R3
d0_3 = A0*R3*R1 + R1*R3 - R1*R2 + R2*R3
d1_3 = (R1*R3 - R1*R2 + R2*R3)/(2*pi*fp)

