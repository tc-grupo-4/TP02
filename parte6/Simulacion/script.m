clear all
close all

data = csvread('medicion.csv',1,0);
t = data(:,0);
vin = data(:,1);

x0=10;
y0=10;
width=550;
height=300;
set(gcf,'units','points','position',[x0,y0,width,height])


plot(t,vin);
title('Señal de entrada', 'Interpreter', 'latex');
xlabel('$V_{in}[V]$','Interpreter', 'latex');
ylabel('$V_{out}[V]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');

grid minor

print -dpdf 'grafica_input_medicion.pdf'