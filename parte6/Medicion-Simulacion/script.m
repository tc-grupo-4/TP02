clear all
close all

data_s = csvread('simulacion.csv',1,0);
vin_s = data_s(:,1);
vout_s = data_s(:,2);

data_m = csvread('medicion_osc.csv',2,0);
vin_m = data_m(:,2);
vout_m = data_m(:,3);

data_r = csvread('medicion_ruido.csv',2,0);
vin_r = data_r(:,2);
vout_r = data_r(:,3);


x0=10;
y0=10;
width=550;
height=300;
set(gcf,'units','points','position',[x0,y0,width,height])


plot(vin_s, vout_s,vin_r, vout_r);
legend({'$Simulacion$', '$Medicion$'}, 'Interpreter', 'latex')
title('Simulacion vs. Medicion con ruido', 'Interpreter', 'latex');
xlabel('$V_{in}[V]$','Interpreter', 'latex');
ylabel('$V_{out}[V]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');

grid minor

print -dpdf 'grafica_contraste_ruido.pdf'