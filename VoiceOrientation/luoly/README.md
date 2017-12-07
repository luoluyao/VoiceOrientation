# 文件说明
## generatePar.py

  * 使用maus切割，生成TextGrid文件
  
  * $ python generatePar.py **<filename(.wav not include)>**
  
## generateResult.py

  * 输出三个麦克风与某一个麦克风的Tdoa（sample数） （**注意采样频率**）
  
  * $ python generateResult.py **<filename(.wav not include)>**
  
## readwav.py

 * 输入：两个音频文件(.wav)和对应的TextGrid文件
 * 输出：三个麦克风与某一个麦克风各个音素的tdoa

## process.m

 * 输入：音频文件，及切割时间
 * 输出：各个音素时间差
 * 与 readwav区别是：使用的是matlab本身的互相关函数
