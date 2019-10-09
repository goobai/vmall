# Centos 常用命令



##压缩
```shell
#将目录里所有jpg文件打包成tar.jpg
tar –cvf jpg.tar *.jpg 
#将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz 
tar –czvf jpg.tar.gz *.jpg 
```
##查看
```shell
#在不解压的情况下查看压缩包的内容
tar -tf aaa.tar.gz  

```


## 解压
```shell
#解压tar包
tar –xvf file.tar  
#解压tar.gz
tar -xzvf file.tar.gz 
```

