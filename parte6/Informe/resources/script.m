clear all
close all

Vout = @(x) 50*x - 17.5;
Vin = 0.2:10e-6:0.55;

%data = csvread('Draft1.csv',1,0);
%vin = data(:,1);
%vout = data(:,2);

x0=10;
y0=10;
width=550;
height=300;
set(gcf,'units','points','position',[x0,y0,width,height])


plot(Vin, Vout(Vin));
title('Salida analitica sin limitador', 'Interpreter', 'latex');
xlabel('$V_{in}[V]$','Interpreter', 'latex');
ylabel('$V_{out}[V]$', 'Interpreter', 'latex');
set(gca,'TickLabelInterpreter','latex');
axis tight
grid minor

print -dpdf 'grafica_analitica.pdf'