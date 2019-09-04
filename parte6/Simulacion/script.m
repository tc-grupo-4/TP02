clear all
close all

data = csvread('Draft1.csv',1,0);
vin = data(:,1);
vout = data(:,2);

x0=10;
y0=10;
width=550;
height=300;
set(gcf,'units','points','position',[x0,y0,width,height])


semilogx(vin, vout);
title('Simulacion', 'Interpreter', 'latex');
xlabel('$V_{in}[V]$','Interpreter', 'latex');
ylabel('$V_{out}[V]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');

grid minor

print -dpdf 'grafica_simulacion.pdf'

semilogx(f, Q);
title('Factor de Calidad', 'Interpreter', 'latex');
xlabel('$f[Hz]$','Interpreter', 'latex');
ylabel('$Q$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');
axis tight
grid minor

print -dpdf 'grafica_Q.pdf'

semilogx(f, R);
title('Factor R', 'Interpreter', 'latex');
xlabel('$f[Hz]$','Interpreter', 'latex');
ylabel('$R[\Omega]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');
axis tight
grid minor

print -dpdf 'grafica_factor_R.pdf'

semilogx(f, Phi);
title('Argumento de Impedancia', 'Interpreter', 'latex');
xlabel('$f[Hz]$','Interpreter', 'latex');
ylabel('$\varphi[Grad]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');
axis tight
grid minor

print -dpdf 'grafica_phi.pdf'