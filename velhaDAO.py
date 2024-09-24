#+------------------------------------------------+
#| Projeto Jogo da Velha                          |
#| autor: Bruno Gontijo                           |
#| descrição: jogo da velha para aprender phyton, |
#|            funcões de banco de dados.          |
#| data inicio: 15/03/24                          | 
#| data fim: 05/06/24                             |
#+------------------------------------------------+-------------
import psycopg2

#+----------------------------
#| Multiplos Scripts de banco de dados
#+----------------------------

#+---------------------------------------------------------------------------------------------------------------
#
#    ********  ********  **        ********   ******   **********
#   **//////  /**/////  /**       /**/////   **////** /////**/// 
#  /**        /**       /**       /**       **    //      /**    
#  /********* /*******  /**       /******* /**            /**    
#  ////////** /**////   /**       /**////  /**            /**    
#         /** /**       /**       /**      //**    **     /**    
#   ********  /******** /******** /******** //******      /**    
#  ////////   ////////  ////////  ////////   //////       //   
#
#+---------------------------+
#| Script de Leitura Placar  |
#+---------------------------+
def retorna_placar():
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT * FROM "Jogo_da_Velha".tb_placar order by pontuacao desc'
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

#+-------------------------------------+
#| Script do Leitura Placar e do nome  |
#+-------------------------------------+
def retorna_placar_nome():
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT pontuacao,modo_de_jogo,caractere,nome_do_jogador FROM "Jogo_da_Velha".tb_jogador jogador INNER JOIN "Jogo_da_Velha".tb_placar placar ON jogador.id_jogador=placar.id_jogador;'
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

#+---------------------------+
#| Script de Leitura Jogador |
#+---------------------------+
def obter_jogador():
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT * FROM "Jogo_da_Velha".tb_jogador order by id_jogador desc'
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

#+--------------------------------------------+
#|Script de Leitura da Tabela Jogador e Placar|
#+--------------------------------------------+
def obter_plac_jog():
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT * FROM "Jogo_da_Velha".tb_jogador jog INNER JOIN "Jogo_da_Velha".tb_placar plac ON jog.id_jogador = plac.id_jogador;'
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

#+--------------------------------------------+
#|Script de Leitura da Tabela Jogador e Dados |
#+--------------------------------------------+
def obter_dados_jogador ():
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT * FROM "Jogo_da_Velha".tb_jogador jog INNER JOIN "Jogo_da_Velha".tb_dados_jogador dados ON jog.id_jogador = dados.id_jogador;'
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

#+------------------------------------------------------------+
#|Script de Leitura da Tabela Jogador e Dados por meio do CPF |
#+------------------------------------------------------------+
def obter_dados_jogador_cpf (cpf):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT * FROM "Jogo_da_Velha".tb_jogador jogador INNER JOIN "Jogo_da_Velha".tb_dados_jogador dados ON jogador.id_jogador=dados.id_jogador WHERE dados. cpf = '+"'" + str(cpf)+ "'" +";"
  cur.execute(str_select)
  conn.commit()
  rows=cur.fetchall()
  conn.close()
  return rows

def select_id(cpf):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_select = 'SELECT id_jogador FROM "Jogo_da_Velha".tb_dados_jogador WHERE cpf='+"'"+str(cpf)+"';"
  cur.execute(str_select)
  id_jogador = cur.fetchone()[0]
  conn.commit()
  conn.close()
  return id_jogador
#+--------------------------------------------------------------------------------------------------------------
#   **  ****     **   ********  ********  *******    **********
#  /** /**/**   /**  **//////  /**/////  /**////**  /////**/// 
#  /** /**//**  /** /**        /**       /**   /**      /**    
#  /** /** //** /** /********* /*******  /*******       /**    
#  /** /**  //**/** ////////** /**////   /**///**       /**    
#  /** /**   //****        /** /**       /**  //**      /**    
#  /** /**    //***  ********  /******** /**   //**     /**    
#  //  //      ///  ////////   ////////  //     //      //     
#+------------------------------------------------------+
#| Script de Inserção Nome do Jogador na tabela Jogador |
#+------------------------------------------------------+
def InsertNomeJogador(nome_do_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_jogador(nome_do_jogador) VALUES ('"'" + nome_do_jogador + "'" + ');'
  cur.execute(str_insert)
  cur.execute('SELECT LASTVAL()')
  lastid = cur.fetchone()[0]
  conn.commit()
  conn.close()
  return lastid

#+----------------------------------------------------+
#| Script de Inserção Jogador e seus Dados (Cadastro) |
#+----------------------------------------------------+
def insert_jogador(nome_do_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_jogador(nome_do_jogador) VALUES ('"'" + nome_do_jogador + "'" + ');'
  cur.execute(str_insert)
  cur.execute('SELECT LASTVAL()')
  id_jogador = cur.fetchone()[0]
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_dados_jogador(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf) VALUES ('+ str(id_jogador) + ','+"'" + sexo + "'" + ','+ "'" + data_de_nascimento + "'" +',' + "'" + cidade +"'" + ',' + "'" + uf + "'" ',' + "'" + str(cep) +"'" +','"'"+str(cpf)+"'" +');'
  cur.execute(str_insert)
  conn.commit()
  conn.close()
  return id_jogador

#+---------------------------+
#| Script de Inserção Placar |
#+---------------------------+
def insertPlacar(id_jogador,pontuacao,caractere,modo_de_jogo):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_placar(id_jogador,pontuacao, caractere, modo_de_jogo) VALUES ('+str(id_jogador)  + ',' + str(pontuacao) + ',' + "'" + caractere +  "'" +',' + "'" + modo_de_jogo + "'"+ ');'
  cur.execute(str_insert)
  conn.commit()
  conn.close()


#+-------------------------------------------+
#| Script de Inserção Placar por meio do CPF |
#+-------------------------------------------+
def insertPlacar2(cpf,pontuacao,caractere,modo_de_jogo):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_select = 'SELECT id_jogador FROM "Jogo_da_Velha".tb_dados_jogador WHERE cpf='+"'"+str(cpf)+"';"
  cur.execute(str_select)
  id_jogador = cur.fetchone()[0]
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_placar(id_jogador,pontuacao, caractere, modo_de_jogo) VALUES ('+str(id_jogador)  + ',' + str(pontuacao) + ',' + "'" + caractere +  "'" +',' + "'" + modo_de_jogo + "'"+ ');'
  cur.execute(str_insert)
  conn.commit()
  conn.close()


#+----------------------------------------+
#|Script de Inserção dos Dados do Jogador |
#+----------------------------------------+
def insert_dados_jog (id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_insert = 'INSERT INTO "Jogo_da_Velha".tb_dados_jogador(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf) VALUES ('+ str(id_jogador) + ','+"'" + sexo + "'" + ','+ "'" + data_de_nascimento + "'" +',' + "'" + cidade +"'" + ',' + "'" + uf + "'" ',' + "'" + str(cep) +"'" +','"'"+str(cpf)+"'" +');'
  cur.execute(str_insert)
  conn.commit()
  conn.close()


#+-------------------------------------------------------------------------------------------------------------
#
#   **     **  *******   *******        **     **********  ********
#  /**    /** /**////** /**////**      ****   /////**///  /**///// 
#  /**    /** /**   /** /**    /**    **//**      /**     /**      
#  /**    /** /*******  /**    /**   **  //**     /**     /******* 
#  /**    /** /**////   /**    /**  **********    /**     /**////  
#  /**    /** /**       /**    **  /**//////**    /**     /**      
#  //*******  /**       /*******   /**     /**    /**     /********
#   ///////   //        ///////    //      //     //      //////// 
#+----------------------------+-----
#|+ Script de Update do Placar |
#+----------------------------+-------------
def update_pontuacao(id_jogador,id_placar,pontuacao,modo_de_jogo,caractere):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_update = 'UPDATE "Jogo_da_Velha".tb_placar SET pontuacao='+ str(pontuacao) +' , modo_de_jogo='+ "'" + modo_de_jogo + "'" + ' , caractere=' + "'" + caractere+ "'" +' WHERE id_jogador ='"'" +str(id_jogador)+"'"+ ' AND id_placar='"'" + str(id_placar)+ "'"
  cur.execute(str_update)
  conn.commit()
  conn.close()

#+-------------------------------------------------------------------------------+-----
#|+ Script de Update das Tabelas Dados de Jogador e Jogador (Update do Registro) |
#+-------------------------------------------------------------------------------+-------------
def update_cadastro(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf,nome_do_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)  
  cur = conn.cursor()
  str_update = 'UPDATE "Jogo_da_Velha".tb_dados_jogador SET sexo='+ "'" + sexo + "'" + ",data_de_nascimento="+ "'" + str(data_de_nascimento) + "'" + ",cidade= "+ "'" +  cidade +"'" + ",uf=" + "'" + uf + "'" + ",cep=" + "'" + str(cep) + "'" + ",cpf=" + "'" + str(cpf) + "'" + "WHERE id_jogador=" + str(id_jogador) + ";"
  cur.execute(str_update)
  str_update = 'UPDATE "Jogo_da_Velha".tb_jogador SET  nome_do_jogador='"'" + nome_do_jogador +  "'" 'WHERE id_jogador= '"'" + str(id_jogador) + "'"  ";"
  cur.execute(str_update)
  conn.commit()
  conn.close()


#+---------------------------------------------------------------------------------------------------------------------------------------------
#   *******    ********  **        ********  **********  ********
#  /**////**  /**/////  /**       /**/////  /////**///  /**///// 
#  /**    /** /**       /**       /**           /**     /**      
#  /**    /** /*******  /**       /*******      /**     /******* 
#  /**    /** /**////   /**       /**////       /**     /**////  
#  /**    **  /**       /**       /**           /**     /**      
#  /*******   /******** /******** /********     /**     /********
#  ///////    ////////  ////////  ////////      //      //////// 
#
#+----------------------------------------------+
#| Script de Delete Placar pela Id do jogador   |
#+----------------------------------------------+
def delete_placar_idj(id_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_placar	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()

#+----------------------------------------------+
#| Script de Delete Placar pela Id do placar    |
#+----------------------------------------------+
def delete_placar_idp(id_placar):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_placar	WHERE id_placar =' + "'" + str(id_placar) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()

#+---------------------------------------------------------+
#| Script de Delete Dados do Jogador pela Id do Jogador    |
#+---------------------------------------------------------+
def delete_dados_idj(id_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_dados_jogador	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()

#+--------------------------------------------------------+
#| Script de Delete Dados do Jogador pela Id dos Dados    |
#+--------------------------------------------------------+
def delete_dados_idd(id_dados_do_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_dados_jogador	WHERE id_dados_jogador =' + "'" + str(id_dados_do_jogador) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()

#+------------------------------------------------+
#| Script de Delete Jogador pela Id do Jogador    |
#+------------------------------------------------+
def delete_jogador_idj(id_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_jogador WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()  

def delete_dados_placar_jogador_idj(id_jogador):
  conn = psycopg2.connect(database = "postgres", 
                          user = "postgres", 
                          host= 'localhost',
                          password = "postgres",
                          port = 5432)
  cur = conn.cursor()
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_dados_jogador	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_placar	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  str_delete = 'DELETE FROM "Jogo_da_Velha".tb_jogador WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  conn.commit()
  conn.close()  
#-------------------------------------------------------------------------------------------------------------------
   
                                                              
                                                           
#                    @@@@ @@@@@@@                           
#                  @@  =@@-     :@@                         
#                  @@    @-     :@@@@@@                     
#                  @@      @     @::@@@                     
#              @@@@      @@@::   @::@@@                     
#            @@:         @@@::  :@@@@@@@                    
#            @@:  @               :@::@@                    
#            @@:      @@@  @-     :@::@@                    
#              @@@@@@@@:::::.       @@@@@@@@@@              
#                  @@::::    @      @@@:::@@@@              
#                  @@      @-         @@@   @@              
#                    @@@@@-      @    @:  @@                
#                    @@           .@@@@.  @@                
#                  @@@@@@    @        @@@@                  
#                @@    =@@-  @      @@@@                    
#                  @@@@@@@@@@@@@@@@@@@@                     
#                             @@    @@@                     
#                               @@@@                    
#         
                                                           
                                                 