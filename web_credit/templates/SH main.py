from flask import Flask, render_template, url_for, request
import pymysql
import json

app = Flask(__name__)



@app.route('/credit') 
def creditall():
    #credit =[]
    occyp_type =[]
    count = []
    
    #credit == 0 
    def credit0():      
        occyp_type0 = []
        count0 = []
        
        try:
            sample_db0 = pymysql.connect(
                user='root',
                passwd='1111',
                host='localhost',
                db='dacon_credit'
            )
            cursor0 = sample_db0.cursor()
            sql0 = "select occyp_type, count(occyp_type) from train where credit = 0 group by occyp_type order by count(occyp_type)DESC"
            cursor0.execute(sql0)         #sql 구문 실행
            result0 = cursor0.fetchall()

            for list0 in result0:
                #credit.append(list[0])
                occyp_type0.append(list0[0])
                count0.append(list0[1])

            print(result0)
            #print(ID)
            # print(occyp_type)
            # print(credit)
        finally:
            sample_db0.close()
        return count0

    #credit == 1 
    def credit1():      
        occyp_type1 = []
        count1 = []
        
        try:
            sample_db1 = pymysql.connect(
                user='root',
                passwd='1111',
                host='localhost',
                db='dacon_credit'
            )
            cursor1 = sample_db1.cursor()
            sql1 = "select occyp_type, count(occyp_type) from train where credit = 1 group by occyp_type order by count(occyp_type)DESC"
            cursor1.execute(sql1)         #sql 구문 실행
            result1 = cursor1.fetchall()

            for list1 in result1:
                #credit.append(list[0])
                occyp_type1.append(list1[0])
                count1.append(list1[1])

            print(result1)
            #print(ID)
            # print(occyp_type)
            # print(credit)
        finally:
            sample_db1.close()
                
        return count1

    #credit == 2 
    def credit2():      
        occyp_type2 = []
        count2 = []
        
        try:
            sample_db2 = pymysql.connect(
                user='root',
                passwd='1111',
                host='localhost',
                db='dacon_credit'
            )
            cursor2 = sample_db2.cursor()
            sql2 = "select occyp_type, count(occyp_type) from train where credit = 2 group by occyp_type order by count(occyp_type)DESC"
            cursor2.execute(sql2)         #sql 구문 실행
            result2 = cursor2.fetchall()

            for list2 in result2:
                #credit.append(list[0])
                occyp_type2.append(list2[0])
                count2.append(list2[1])

            print(result2)
            #print(ID)
            # print(occyp_type)
            # print(credit)
        finally:
            sample_db2.close()
        
        
        return count2


    #credit All
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1111',
            host='localhost',
            db='dacon_credit'
        )
        cursor = sample_db.cursor()
        sql = "select occyp_type, count(occyp_type) from train group by occyp_type order by count(occyp_type)DESC"
        cursor.execute(sql)         #sql 구문 실행
        result = cursor.fetchall()

        for list in result:
            #credit.append(list[0])
            occyp_type.append(list[0])
            count.append(list[1])

        #print(result)
        #print(ID)
        # print(occyp_type)
    finally:
        sample_db.close()
    
    count0 = json.dumps(credit0())
    count1 = json.dumps(credit1())
    count2 = json.dumps(credit2())
    print(count0)
    return render_template('index.html', result = result, occyp_type = occyp_type, count=count, count0 = count0, count1 = count1, count2=count2)







app.run