# 주의!
# 애초에 가상환경으로 설정하여 돌아가는 파일이므로 venv환경에서 이를 시행하려면 각 라이브러리를 install해줘야 함.

# 플라스크 시행하는 부분으로 cmd창에 입력하는 명령문

# source bin/activate 로 가상환경 실행
# export FLASK_APP=main
# flask run

from flask import Flask, render_template, url_for, request
import json
import pymysql
import simplejson
import pandas as pd


# password 설정부분
_password = '패스워드를 입력하세요'

# SQL구문
sample_db = pymysql.connect(
        user='root', 
        password=f'{_password}',
        host='localhost',
        database='dacon_credit')
cursor = sample_db.cursor()
sql = "select * from train"
cursor.execute(sql)
sub = cursor.fetchall()
sample_db.close()

df1 = pd.DataFrame(sub)
# 출력할 값으로 ['Child_num','Income_total', 'Family_size', 'Begin_month', 'Year_total','Work_total', 'Nth_card', 'Ability']를 의미함.
_col =[4, 5,16,17,19,20,21,22]     

# Max값을 하위 100%로 설정하여 하위 몇 %에 위치하는지 알기 쉽게 식을 설정하고 dataframe으로 뽑음
df2 = round((df1[_col] / df1[_col].max())*100, 2)


app = Flask(__name__)   



# 미리 url을 짜놓고 들어가기도 함. (몇번 페이지를 만들것이고 어떤 기능을 형성할 것인지 문서화하고 개발을 시도함)
# 로컬 호스트에 들어갈 때, index.html을 보여주겠다.
# Main page가 되는 부분임.
@app.route('/Main')
def Main():
    try:
        sample_db = pymysql.connect(
            user='root', 
            password=f'{_password}',
            host='localhost',
            database='dacon_credit'
        )
        cursor = sample_db.cursor()
        sql = "select * from train limit 1500"
        cursor.execute(sql)
        result1 = cursor.fetchall()
    
    finally:
        sample_db.close()
    # 이부분은 sql을 잘 수행했는지 확인하는 부분으로 cmd에서 값을 출력해줌.
    # print(result1)
    # templates폴더 내에 있는 Main.html에 result1를 result라는 값으로 보내준다는 의미.
    return render_template('Main.html', result = result1)



# Main에서 input값을 message로 받아서 sql에 그 값을 입력하고 다시 Main으로 보내는 부분으로
# ajax를 이용하여 동적인 html을 구현하였음.
@app.route('/get_json')
def get_json():
    # result2는 ID에 해당하는 정보와 Minmaxscaler를 한 값을 보내줘야하므로 생성한 list임
    # result2로 지정하여 Main값에서 return해주는 result값과 겹치지 않도록 2값을 부여함
    result2 = []
    # 이부분은 input에 입력한 값을 getjson으로 받아온 값임.
    _message = request.args["message"]
    try:
        sample_db = pymysql.connect(
            user='root', 
            password=f'{_password}',
            host='localhost',
            database='dacon_credit'
        )
        cursor = sample_db.cursor()
        sql = "select * from train where ID = %s"
        val = (_message)
        cursor.execute(sql, val)
        sql_result = cursor.fetchall()
    finally:
        sample_db.close()

    # sql로 얻은 값을 append하는 부분
    result2.append(sql_result)
    
    # getjson으로 받은 값을 int로 변경하고 그값을 num변수로 지정함
    num = int(val)
    # 위에서 생성한 df 100을 곱하고 소숫점 2자리까지 출력하여 %값으로 변환한 후 list형태로 바꿔줌
    ID_radar = df2.iloc[num].tolist()
    # df의 result2에 append해줌.
    result2.append(ID_radar)
    
    # 잘 출력되었는지 확인하는 부분
    # print(sql_result)
    # print(ID_radar)
    # print(result2)   
    return json.dumps(result2)


@app.route('/credit_occyp') #대시보드 만들기
def creditall():
    #credit =[]
    occyp_type =[]
    count = []
    
    #하나 더 삽입  credit == 0 
    def credit0():      
        occyp_type0 = []
        count0 = []
        
        try:
            sample_db0 = pymysql.connect(
                user='root',
                password=f'{_password}',
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

    #하나 더 삽입  credit == 1 
    def credit1():      
        occyp_type1 = []
        count1 = []
        
        try:
            sample_db1 = pymysql.connect(
                user='root',
                password=f'{_password}',
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

    #하나 더 삽입  credit == 2 
    def credit2():      
        occyp_type2 = []
        count2 = []
        
        try:
            sample_db2 = pymysql.connect(
                user='root',
                password=f'{_password}',
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
            password=f'{_password}',
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

        print(result)
        #print(ID)
        # print(occyp_type)
    finally:
        sample_db.close()
    
    count0 = json.dumps(credit0())
    count1 = json.dumps(credit1())
    count2 = json.dumps(credit2())
    print(count0)
    return render_template('credit_occyp.html', result = result, occyp_type = occyp_type, count=count, count0 = count0, count1 = count1, count2=count2)
    

@app.route('/credit_income')
def credit_income():
    credit=[]
    income_t_mean=[]
    income_t_count=[]
    ability=[]
    try:
        sample_db = pymysql.connect(
            user='root',
            password=f'{_password}',
            host='localhost',
            db='dacon_credit'
        )
        cursor = sample_db.cursor()
        sql = "SELECT credit, avg(income_total), count(income_total),avg(ability) FROM train GROUP BY credit ORDER BY credit ASC;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for list in result:
            credit.append(list[0])
            income_t_mean.append(list[1])
            income_t_count.append(list[2])
            ability.append(list[3])
        income_t_mean = simplejson.dumps(income_t_mean)
        ability = simplejson.dumps(ability)
        # print(credit)
        # print(income_t_mean)
        # print(income_t_count)
        # print(ability)
    finally:
        sample_db.close()
    return render_template('credit_income.html', result=result, credit=credit, income_t_count=income_t_count, income_t_mean=income_t_mean,ability=ability)

@app.route('/cardNum_income')
def cardNum_income():
    cardNum=[]
    income_t_mean=[]
    income_t_count=[]
    credit=[]
    ability=[]
    try:
        sample_db = pymysql.connect(
            user='root',
            password=f'{_password}',
            host='localhost',
            db='dacon_credit'
        )
        cursor = sample_db.cursor()
        sql = "SELECT Nth_card, avg(income_total), count(income_total), avg(credit), avg(ability) FROM train WHERE Nth_card<=13 GROUP BY Nth_card ORDER BY Nth_card ASC;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for list in result:
            cardNum.append(list[0])
            income_t_mean.append(list[1])
            income_t_count.append(list[2])
            credit.append(list[3])
            ability.append(list[4])
        income_t_mean = simplejson.dumps(income_t_mean)
        credit = simplejson.dumps(credit)
        ability = simplejson.dumps(ability)
        # print(cardNum)
        # print(income_t_mean)
        # print(income_t_count)
        # print(credit)
        # print(ability)
    finally:
        sample_db.close()
    return render_template('cardNum_income.html', result=result, cardNum=cardNum, income_t_count=income_t_count, income_t_mean=income_t_mean,credit=credit,ability=ability)



@app.route('/age_income')
def age_income():
    age=[20, 25, 30, 35, 40, 45, 50, 55, 60]
    d_age = []
    income_t_mean=[]
    income_t_count=[]
    credit=[]
    ability=[]
    try:
        sample_db = pymysql.connect(
            user='root',
            password='jjms7794',
            host='localhost',
            db='dacon_credit'
        )
        cursor = sample_db.cursor()
        # sql = "SELECT floor(year_total), avg(income_total), count(income_total), avg(credit),avg(ability) FROM train GROUP BY year_total ORDER BY year_total ASC;"
        sql1 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE year_total<25;"
        sql2 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 25<=year_total and year_total<30;"
        sql3 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 30<=year_total and year_total<35;"
        sql4 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 35<=year_total and year_total<40;"
        sql5 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 40<=year_total and year_total<45;"
        sql6 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 45<=year_total and year_total<50;"
        sql7 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 50<=year_total and year_total<55;"
        sql8 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 55<=year_total and year_total<60;"
        sql9 = "SELECT year_total, avg(income_total), count(income_total), avg(credit),avg(ability) FROM train WHERE 60<=year_total;"

        def list_result(sql):
            cursor.execute(sql)
            result = cursor.fetchall()
            for list in result:
                d_age.append(list[0])
                income_t_mean.append(list[1])
                income_t_count.append(list[2])
                credit.append(list[3])
                ability.append(list[4])

        list_result(sql1)
        list_result(sql2)
        list_result(sql3)
        list_result(sql4)
        list_result(sql5)
        list_result(sql6)
        list_result(sql7)
        list_result(sql8)
        list_result(sql9)

        income_t_mean = simplejson.dumps(income_t_mean)
        credit = simplejson.dumps(credit)
        ability = simplejson.dumps(ability)

        # print(age)
        # print(income_t_mean)
        # print(income_t_count)
        # print(credit)
        # print(ability)
    finally:
        sample_db.close()
    return render_template('age_income.html', age=age, income_t_count=income_t_count, income_t_mean=income_t_mean,credit=credit,ability=ability)



app.run()







