r = 15e3; c = 6.8e-9;

Ao = 10^(110/20); % de la hoja de datos: Ao=110dB
BWP = 15e6;
wp = 2*pi*BWP/Ao;
opt = bodeoptions();
opt.FreqUnits = 'Hz';

s = tf('s');
w = 2*pi*logspace(0, 6, 10000);

z1 = r;
z2 = 1/s/c;

w = 2*pi*logspace(0, 11, 10000);
%Esto para el CASO IDEAL%
G = -z2/z1; %Caso ideal
%opt.Title.String = 'Integrador - Caso Ideal';
%bode(G, w, opt);
bode(G);
grid on;

hold on
%opt.Title.String = 'Integrador - Avol finito';
G= -Avol*z2/(z2+(Avol+1)*z1);
bode(G);
%bode(G, w, opt);
grid on;

hold on
Avolw = Avol/(1+(s/wp));
G = -Avolw*z2/(z2+(Avolw+1)*z1);
bode(G);
grid on;


%SIMBOLICO%
syms R AVOL BWP WP Z1 Z2 S R C
Z1 = R;
Z2=1/(S*C);
G=-Z2/Z1
G= -AVOL*Z2/(Z2+(AVOL+1)*Z1)
AVOLW = AVOL/(1+(S/WP));
G = -AVOLW*Z2/(Z2+(AVOLW+1)*Z1)
