import sqlite3

def get_conection():
  con = sqlite3.connect("final_velha.db")
  #con = sqlite3.connect("D:/Arquivos/Scripts/ProjJogoDaVelha/jogo-da-velha/Backend/final_velha.db")
  return con
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
def retorna_placar_nome():
  con = get_conection()
  cur = con.cursor()
  str_select = 'SELECT pontuacao,modo_de_jogo,caractere,nome_do_jogador FROM tb_jogador jogador INNER JOIN tb_placar placar ON jogador.id_jogador=placar.id_jogador;'
  cur.execute(str_select)
  con.commit()
  rows=cur.fetchall()
  con.close()
  return rows

#+------------------------------------------------------------+
#|Script de Leitura da Tabela Jogador e Dados por meio do CPF |
#+------------------------------------------------------------+
def obter_dados_jogador_cpf (cpf):
  con = get_conection()
  cur = con.cursor()
  str_select = 'SELECT * FROM tb_jogador jogador INNER JOIN tb_dados_jogador dados ON jogador.id_jogador=dados.id_jogador WHERE dados. cpf = '+"'" + str(cpf)+ "'" +";"
  cur.execute(str_select)
  con.commit()
  rows=cur.fetchall()
  con.close()
  return rows

#+--------------------------------------------------------------------------------------------------------------
#   **  ****     **   ********  ********  *******    **********
#  /** /**/**   /**  **//////  /**/////  /**////**  /////**/// 
#  /** /**//**  /** /**        /**       /**   /**      /**    
#  /** /** //** /** /********* /*******  /*******       /**    
#  /** /**  //**/** ////////** /**////   /**///**       /**    
#  /** /**   //****        /** /**       /**  //**      /**    
#  /** /**    //***  ********  /******** /**   //**     /**    
#  //  //      ///  ////////   ////////  //     //      //     
#+----------------------------------------------------+
#| Script de Inserção Jogador e seus Dados (Cadastro) |
#+----------------------------------------------------+
def insert_jogador(nome_do_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf):
  con = get_conection()
  cur = con.cursor()
  str_insert = 'INSERT INTO tb_jogador(nome_do_jogador) VALUES ('"'" + nome_do_jogador + "'" + ');'
  cur.execute(str_insert)
  cur.execute('select last_insert_rowid()')
  id_jogador = cur.fetchone()[0]
  str_insert = 'INSERT INTO tb_dados_jogador(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf) VALUES ('+ str(id_jogador) + ','+"'" + str(sexo) + "'" + ','+ "'" + str(data_de_nascimento) + "'" +',' + "'" + str(cidade) +"'" + ',' + "'" + str(uf) + "'" ',' + "'" + str(cep) +"'" +','"'"+str(cpf)+"'" +');'
  cur.execute(str_insert)
  con.commit()
  con.close()
  return id_jogador

#+-------------------------------------------+
#| Script de Inserção Placar por meio do CPF |
#+-------------------------------------------+
def insertPlacar2(cpf,pontuacao,caractere,modo_de_jogo):
  con = get_conection()
  cur = con.cursor()
  str_select = 'SELECT id_jogador FROM tb_dados_jogador WHERE cpf='+"'"+str(cpf)+"';"
  cur.execute(str_select)
  id_jogador = cur.fetchone()[0]
  str_insert = 'INSERT INTO tb_placar(id_jogador,pontuacao, caractere, modo_de_jogo) VALUES ('+str(id_jogador)  + ',' + str(pontuacao) + ',' + "'" + caractere +  "'" +',' + "'" + modo_de_jogo + "'"+ ');'
  cur.execute(str_insert)
  con.commit()
  con.close()


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
#+-------------------------------------------------------------------------------+-----
#|+ Script de Update das Tabelas Dados de Jogador e Jogador (Update do Registro) |
#+-------------------------------------------------------------------------------+-------------
def update_cadastro(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf,nome_do_jogador):
  con = get_conection()
  cur = con.cursor()
  str_update = 'UPDATE tb_dados_jogador SET sexo='+ "'" + sexo + "'" + ",data_de_nascimento="+ "'" + str(data_de_nascimento) + "'" + ",cidade= "+ "'" +  cidade +"'" + ",uf=" + "'" + uf + "'" + ",cep=" + "'" + str(cep) + "'" + ",cpf=" + "'" + str(cpf) + "'" + "WHERE id_jogador=" + str(id_jogador) + ";"
  cur.execute(str_update)
  str_update = 'UPDATE tb_jogador SET  nome_do_jogador='"'" + nome_do_jogador +  "'" 'WHERE id_jogador= '"'" + str(id_jogador) + "'"  ";"
  cur.execute(str_update)
  con.commit()
  con.close()

#+---------------------------------------------------------------------------------------------------------------------------------------------
#   *******    ********  **        ********  **********  ********
#  /**////**  /**/////  /**       /**/////  /////**///  /**///// 
#  /**    /** /**       /**       /**           /**     /**      
#  /**    /** /*******  /**       /*******      /**     /******* 
#  /**    /** /**////   /**       /**////       /**     /**////  
#  /**    **  /**       /**       /**           /**     /**      
#  /*******   /******** /******** /********     /**     /********
#  ///////    ////////  ////////  ////////      //      //////// 
def delete_dados_placar_jogador_idj(id_jogador):
  con = get_conection()
  cur = con.cursor()
  str_delete = 'DELETE FROM tb_dados_jogador	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  str_delete = 'DELETE FROM tb_placar	WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  str_delete = 'DELETE FROM tb_jogador WHERE id_jogador =' + "'" + str(id_jogador) + "'" +';'
  cur.execute(str_delete)
  con.commit()
  con.close()  



#           		     #@@@ :@@@@@:                           
#                  +@*+@@@%+++++@@:                         
#                  +@*+++@%++ :+@@@@@%                      
#                  +@*++++*@%   %@##@%                      
#              :@@@*+++++@@@@#- %@##@%                      
#            .@%+++++++++@@@@#++@@@@@@@%                    
#            .@%+*@*++++++++++++++%@##@%                    
#            .@%+++++%@@@ :@@+++++%@##@%                    
#              :@@@@@@@######+++++++@@@@@@@@@-              
#                  +@#### .+*@#+++++@@@@##@@@-              
#                  +@*++++*@@+++++++++@@@%+%@-              
#                    #@@@@%+++++@@*+++@@+*@-                
#                    #@+=++=+*++++%@@@@@+*@-                
#                  +@@@@@===+@#+++++++@@@*                  
#                :@*+++@@@@**@#+++++@@@%                    
#                  +@@@@@@@@@@@@@@@@@%                      
#                             =@*+++@%                      
#                               %@@@.         