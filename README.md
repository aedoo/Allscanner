# Allscanner
弱端口的弱口令爆破以及未授权访问的集成检测工具。 
Weak password blasting of weak ports and integrated detection tools for unauthorized access.

目前支持的弱服务检测包括如下：

`21 FTP  弱口令检测`
`139 LDAP 未授权访问检测`
`1433 MSSQL 弱口令检测`
`3306 MYSQL 弱口令检测、未授权访问检测`
`11211 MEMCACHED 未授权访问检测`
`6379 Redis 未授权访问检测`
`27017 MongoDB 未授权访问检测`
`9200 Elasticsearch 未授权访问检测`
`1521 Oracle 弱口令检测`

之后可能还会加入：
22 SSH 
23 Telnet （登录方式繁杂并且速度较慢，暂时不考虑加入）
139 Samba
873 RSYNC
5901 VNC 
3389 RDP

## 使用说明 ##

### 查看帮助文件 ###

`python allscanner.py -h`

### 运行示例（扫描192.168.1这个C段的所服务） ###

`python allscanner.py -i 192.168.1.1/24 -t 200`

### 参数说明

`-h：查看帮助文件。`

`-i：接需要扫描的CIDR IP段，如192.168.1.1/24。`

`-t：线程数，不加此参数默认为100。`



### 运行截图（如果FTP爆出大量弱口令，说明未授权访问或者无密码登录）###

![](https://raw.githubusercontent.com/aedoo/Allscanner/master/result.png)
