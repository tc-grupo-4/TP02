clear all
close all

data = csvread('medicion_ruido.csv',2,0);
vin = data(:,2);
vout = data(:,3);

x0=10;
y0=10;
width=550;
height=300;
set(gcf,'units','points','position',[x0,y0,width,height])


plot(vin,vout);
title('Medicion con ruido', 'Interpreter', 'latex');
xlabel('$V_{in}[V]$','Interpreter', 'latex');
ylabel('$V_{out}[V]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');

grid minor

print -dpdf 'grafica_medicion_ruido.pdf'