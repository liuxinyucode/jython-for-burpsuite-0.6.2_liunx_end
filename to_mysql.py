import pymysql


def sec_xss_INSERT(values):
    #建立连接
    db = pymysql.connect(
        host='10.10.5.16',
        port=3306,
        user='securityUser',
        password='fr@?om902sec',
        db='securityDb',
        charset='utf8',
    )

    #拿到游标
    cursor = db.cursor()

    #执行SQL语句
    #sql = 'SELECT * FROM `student`'
    sql = 'INSERT INTO sec_xss(related_taskid,request_method,request_url,first_response,first_status_code,second_response,second_status_code,contrast,account_status)' \
          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    try:
       #rows变量得到数据库中被影响的数据行数。
       rows = cursor.execute(sql, values)
       #print(sql)
       #rows = cursor.execute(sql)\
       #print(rows)
       # 向数据库提交
       db.commit()
       #如果没有commit()，库中字段已经向下移位但内容没有写进，可是自动生成的ID会自动增加。
    except:
       # 发生错误时回滚
       db.rollback()

    #关闭（游标、数据库）
    cursor.close()
    db.close()

def sec_task_INSERT(values):
    db = pymysql.connect(
        host='10.10.5.16',
        port=3306,
        user='securityUser',
        password='fr@?om902sec',
        db='securityDb',
        charset='utf8',
    )
    cursor = db.cursor()
    sql = 'INSERT INTO sec_task(system,status,create_user,create_time,start_time,finish_time)' \
          'VALUES (%s,%s,%s,%s,%s,%s)'
    print(sql)
    try:
        print(values)
        cursor.execute(sql, values)
        db.commit()
        print('ok')
    except:
       db.rollback()
    cursor.close()
    db.close()
def sec_task_SELECT(values):
    db = pymysql.connect(
        host='10.10.5.16',
        port=3306,
        user='securityUser',
        password='fr@?om902sec',
        db='securityDb',
        charset='utf8',
    )
    cursor = db.cursor()
    sql = 'SELECT id FROM sec_task where create_time=%s'
    print(sql)
    try:
        print(values)
        cursor.execute(sql, values)
        results=cursor.fetchall()
        return results[0][0]

    except:
       db.rollback()
    cursor.close()
    db.close()

def sec_task_UPDATA(values):
    db = pymysql.connect(
        host='10.10.5.16',
        port=3306,
        user='securityUser',
        password='fr@?om902sec',
        db='securityDb',
        charset='utf8',
    )
    cursor = db.cursor()
    print(values)
    sql1 = 'UPDATE sec_task SET start_time = %s  WHERE create_time = %s'
    sql2 = 'UPDATE sec_task SET status = %s  WHERE create_time = %s'
    try:
        cursor.execute(sql1, (values[1],values[2]))
        db.commit()
        cursor.execute(sql2, (values[0],values[2]))
        db.commit()
        print('ok')
    except:
       db.rollback()
    cursor.close()
    db.close()
def sec_task_UPDATA_finish(values):
    db = pymysql.connect(
        host='10.10.5.16',
        port=3306,
        user='securityUser',
        password='fr@?om902sec',
        db='securityDb',
        charset='utf8',
    )
    cursor = db.cursor()
    print(values)
    sql1 = 'UPDATE sec_task SET finish_time = %s  WHERE create_time = %s'
    sql2 = 'UPDATE sec_task SET status = %s  WHERE create_time = %s'
    try:
        cursor.execute(sql1, (values[1],values[2]))
        db.commit()
        cursor.execute(sql2, (values[0],values[2]))
        db.commit()
        print('ok')
    except:
       db.rollback()
    cursor.close()
    db.close()