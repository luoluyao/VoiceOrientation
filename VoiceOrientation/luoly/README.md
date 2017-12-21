# 文件说明
## generatePar.py

  * 使用maus切割，生成TextGrid文件
  
  * $ python generatePar.py **<filename(.wav not include)>**
  
  * **注意** 里面有个 //BPF=youtellme.par// 需要换成新的文件
  
## generateResult.py
  
  * 用于批量执行readwav.py 脚本
  
  * 输出三个麦克风与某一个麦克风的Tdoa（sample数） （**注意采样频率**）
  
  * $ python generateResult.py **<filename(.wav not include)>**
  
## readwav.py

 * 输入：两个音频文件(.wav)和对应的TextGrid文件
 * 输出：三个麦克风与某一个麦克风各个音素的tdoa
 
 ## classify/python
 
 * 该文件夹提供检测异常（即，机器发声）的算法，包括一类svm。

## process.m

 * 输入：音频文件，及切割时间
 * 输出：各个音素时间差
 * 与 readwav区别是：使用的是matlab本身的互相关函数
