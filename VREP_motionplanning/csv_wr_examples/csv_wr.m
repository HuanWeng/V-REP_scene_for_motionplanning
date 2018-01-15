%Write csv file.
A = [1.1,2.2,3.3;4.4,5.5,6.6];
csvwrite('test.csv', A);

%Read csv file.
B = csvread('test.csv')
