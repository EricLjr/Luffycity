import redis
conn=redis.Redis(host='192.168.11.157',port=6379)
#字符串操作
# conn.set('aa','ljr')
# res=conn.get('aa')
# print(res)
###########
#字典操作
#
conn.flushall()
