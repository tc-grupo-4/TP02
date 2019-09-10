R=39e3;
C=2.7e-9;
Avol = 10^(110/20); %Cuál uso de la hoja de datos?
BWP = 15e6;
wp = 2*pi*BWP/Avol;
opt = bodeoptions();
opt.FreqUnits = 'Hz';

s = tf('s');
w = 2*pi*logspace(0, 6, 10000);

z1=1/(s*C);
%z1 = 1/s/C+470;
z2 = R;

%Esto para el CASO IDEAL%
G = -z2/z1; %Caso ideal
%opt.Title.String = 'Derivador - Caso Ideal';
%Zin = z1;
%%%bode(Zin, w, opt);
%w = 2*pi*logspace(0, 11, 10000);
bode(G, w, opt);
%bode(G);
grid on;

%%Esto para Avol finito%%
hold on
%opt.Title.String = 'Derivador - Avol finito';
G= -Avol*z2/(z2+(Avol+1)*z1);
%Zin= z2/(Avol+1)+z1;
%w = 2*pi*logspace(0, 11, 10000);
%bode(G, w, opt);
%grid on;
%Ahora me quedo con el automatico%
bode(G);
grid on;

%%Esto para Avol con w%%
hold on
Avolw = Avol/(1+(s/wp));
G = -Avolw*z2/(z2+(Avolw+1)*z1);
%Zin = z2/(Avolw+1)+z1;
%opt.Title.String = 'Derivador - Avol(w) con polo dominante)';
bode(G, w, opt);
grid on;





%%%%Esto para el SUPERPUESTO%%%
R=39e3;
C=2.7e-9;
Avol = 10^(110/20); %Cuál uso de la hoja de datos?
BWP = 15e6;
wp = 2*pi*BWP/Avol;
opt = bodeoptions();
opt.FreqUnits = 'Hz';

s = tf('s');
w = 2*pi*logspace(0, 6, 10000);

z1=1/(s*C);
%z1 = 1/s/C+470;
z2 = R;
Avolw = Avol/(1+(s/wp));
G = -Avolw*z2/(z2+(Avolw+1)*z1);
%bode(G, w, opt);
bode(G);
grid on;

hold on;
G= -Avol*z2/(z2+(Avol+1)*z1);
bode(G);
grid on;

hold on;
G = -z2/z1;
bode(G);
grid on;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

r = 39e3; c = 2.7e-9;
Ao = 10^(110/20); % de la hoja de datos: Ao=110dB
BWP = 15e6;
wp = 2*pi*BWP/Ao;
syms r2;
w0 = sqrt(wp*(1+Ao)/c/(r+r2));
xi = w0/2*(c*(r+r2*(1+Ao))+1/wp)/(1+Ao);
r2 = eval(solve(xi == 0.707, r2));

%SIMBOLICO%
syms R AVOL BWP WP Z1 Z2 S R C
Z1 = 1/(S*C);
Z2=R;
G=-Z2/Z1
G= -AVOL*Z2/(Z2+(AVOL+1)*Z1)
AVOLW = AVOL/(1+(S/WP));
G = -AVOLW*Z2/(Z2+(AVOLW+1)*Z1)


H = tf([1 0.1 7.5],[1 0.12 9 0 0]);
w_v = [10:10:100]*2*pi;                                 % Vector Of Radian Frequencies
[mag,phs,RadianFrequency] = bode(H, w_v);
Magnitude = squeeze(mag);
Phase = squeeze(phs);
T = table(RadianFrequency,Magnitude,Phase);
writetable=(T,.xlsx);