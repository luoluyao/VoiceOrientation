clear;
time = [0.18,0.27,0.27,0.8,0.8,1.91,1.91,1.96]; 

times = int32(time * 384000);


result = [];
for count = 0 : length(time)/2 - 1
   
    data0 = wavread('E:\luoluyao\毕业前工作\实验数据\data\newtolley\testCase12-01.wav',[times(1 + count * 2)  times(2 + count * 2)]);
    data1 = wavread('E:\luoluyao\毕业前工作\实验数据\data\newtolley\testCase12-02.wav',[times(1 + count * 2)  times(2 + count * 2)]);
    data2 = wavread('E:\luoluyao\毕业前工作\实验数据\data\newtolley\testCase12-03.wav',[times(1 + count * 2)  times(2 + count * 2)]);
    data3 = wavread('E:\luoluyao\毕业前工作\实验数据\data\newtolley\testCase12-04.wav',[times(1 + count * 2)  times(2 + count * 2)]);
   
    cc1 = xcorr(data1, data0);
    [ma1,I1] = max(cc1);
    r1 = length(data1) - I1;

    cc2 = xcorr(data1, data2);
    [ma2,I2] = max(cc2);
    r2 = length(data1) - I2;

    cc3 = xcorr(data1, data3);
    [ma3,I3] = max(cc3);
    r3 = length(data1) - I3;
    tmp = [r1, r2, r3];
    result = [result, tmp];
end

result = reshape(result, 4, 3);
result