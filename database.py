import pymysql

class ConnectMysql(object):
    def __init__(self):
        self.host = '10.31.81.200'
        self.port = 3306
        self.user = 'fabrikant'
        self.password = 'bd6f1e86'
        self.conn = None
        self.cursor = None


    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()


    def close(self):
        self.cursor.close()
        self.conn.close()


    def modify_db(self, sql):
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count

    def update(self, sql):
        return self.modify_db(sql)

    def select_one(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
            return list(result)[0]  
        except Exception as e:
            print(e)     

    def select_last(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return list(result)[-1]
        except Exception as e:
            print(e)

    def select_all(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return list(result)
        except Exception as e:
            print(e)

class BDCase:
    def get_proposal_id(self):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
      
        mycursor = con.cursor()

        res = "SELECT proposal_id FROM fabrikant_atom_price_request.proposals where procedure_id=18007 and sequence_number = 2"

        mycursor.execute(res)

        rows = mycursor.fetchone()


        mycursor.close()
        return list(rows)[0]


    def set_sign_docs_participant_requirements(self, proposal_id):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
      
        mycursor = con.cursor()

        up = f'UPDATE fabrikant_atom_price_request.proposal_participant_requirements_documents SET sign_id = 1 WHERE (proposal_id ={proposal_id})'

        mycursor.execute(up)

        con.commit()
        mycursor.close()

    def get_staff_certificate_id(self, proposal_id):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
        
        mycursor = con.cursor()
        res = f'SELECT staff_certificate_id FROM fabrikant_atom_price_request.proposal_forms_staff_certificates_v2 where proposal_id={proposal_id}'

        mycursor.execute(res)

        rows = mycursor.fetchone()


        mycursor.close()
        return list(rows)[0]


    def get_questionary_id(self, proposal_id):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
      
        mycursor = con.cursor()

        res = f'SELECT questionary_id FROM fabrikant_atom_price_request.proposal_forms_questionary where proposal_id={proposal_id}'

        mycursor.execute(res)

        rows = mycursor.fetchone()


        mycursor.close()
        return list(rows)[0]


    def get_questionary_pozition_id(self, proposal_id):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
      
        mycursor = con.cursor()

        res = f'SELECT position_id FROM fabrikant_atom_price_request.proposal_forms_questionary_positions where proposal_id={proposal_id}'

        mycursor.execute(res)

        rows = mycursor.fetchone()


        mycursor.close()
        return list(rows)[0]


    def get_pozition_id(self, lot_id):
        con = pymysql.connect(
        host='10.31.81.200',
        user='fabrikant', 
        password = "bd6f1e86",
        )
      
        mycursor = con.cursor()

        res = f'SELECT * FROM fabrikant_atom_price_request.lot_positions where lot_id={lot_id}'

        mycursor.execute(res)

        rows = mycursor.fetchone()


        mycursor.close()
        return list(rows)