import pymysql

#local 
#def conectarMySQL():
#    return pymysql.connect(
#        host='localhost',
#        user='root',
#        password='root',
#        db='final',
#        charset='utf8mb4',
#        cursorclass=pymysql.cursors.DictCursor
#    )

#def conectarRest():
#    return pymysql.connect(
#        host='localhost',
#        user='root',
#        password='root',
#        db='final',
#        charset='utf8mb4',
#       cursorclass=pymysql.cursors.DictCursor
#    )
    
def conectarMySQL():
    return pymysql.connect(
        host='horamda.mysql.pythonanywhere-services.com',
        user='horamda',
        password='zerogluten',
        db='horamda$default',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def conectarRest():
    return pymysql.connect(
        host='horamda.mysql.pythonanywhere-services.com',
        user='horamda',
        password='zerogluten',
        db='horamda$default',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )    