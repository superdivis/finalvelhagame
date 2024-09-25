from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template
from datetime import date
from finalDAO import * 
import json

ip = 'localhost'
#ip='192.168.0.58'
#ip='https://finalvelhagame-c4c8841e9172.herokuapp.com/'

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro_novo")
def cadastro_novo():
    return render_template("cadastro_novo.html")

@app.route("/cadastro_atualizar")
def cadastro_atualizar():
    return render_template("cadastro_atualizar.html")

@app.route("/pontos")
def pontos():
    return render_template("placar.html")

@app.route("/jogar")
def jogar():
    return render_template("tabuleiro.html")


#+-----------+
#|Metodo CRUD|
#+-----------+------------------------------------------------
#   ********   ********  **********
#  **//////** /**/////  /////**/// 
# **      //  /**           /**    
#/**          /*******      /**    
#/**    ***** /**////       /**    
#//**  ////** /**           /**    
# //********  /********     /**    
#  ////////   ////////      //     
#
#+-----------------------------+
#|Endpoint para obter um placar|
#+-----------------------------+
@app.route('/placar', methods=['GET'])
def obter_placar():
    placar = retorna_placar_nome()
    placar_json_ret = []
    if len(placar) == 0:
        return jsonify({'erro': 'Jogador não encontrado!'}), 404
    #Montagem da lista de jogadores
    for p in placar:
        tmp_json={"nome_do_jogador":p[3] ,"pontuacao":p[0] ,"caractere":p[2] ,"modo_de_jogo":p[1]}
        placar_json_ret.append(tmp_json)
        
    return jsonify(placar_json_ret)

@app.route('/cpf/<string:cpf>', methods=['GET'])
def obter_cpf(cpf):
    cpf_cadastro = obter_dados_jogador_cpf(cpf)
    placar_json_ret = []
    if len(cpf_cadastro) == 0:
        return jsonify({'erro': 'Jogador não encontrado!'}), 404
    #Montagem da lista de jogadores
    for parametro in cpf_cadastro:
        tmp_json={"id_jogador":parametro[0] ,"cidade":parametro[5] ,"sexo":parametro[9] ,"nome_do_jogador":parametro[1] ,"uf":parametro[6] , "cep":parametro[7] , "cpf":parametro[8] ,"data_de_nascimento":parametro[4]}
        placar_json_ret.append(tmp_json)
        
    return jsonify(placar_json_ret)

#--------------------------------------------------------------------
#   *******     *******     ********  **********
#  /**////**   **/////**   **//////  /////**/// 
#  /**   /**  **     //** /**            /**    
#  /*******  /**      /** /*********     /**    
#  /**////   /**      /** ////////**     /**    
#  /**       //**     **         /**     /**    
#  /**        //*******    ********      /**    
#  //          ///////    ////////       //     
#
#+------------------+
#|Cadastro Jogador  |
#+------------------+
@app.route('/cadastro', methods=['POST'])
def cadastro():
    try:
        nome_do_jogador=request.json.get('nome_do_jogador')
        sexo=request.json.get('sexo')
        data_de_nascimento=request.json.get('data_de_nascimento')
        cidade=request.json.get('cidade')
        uf=request.json.get('uf')
        cep=request.json.get('cep')
        cpf=request.json.get('cpf')
        insert_jogador(nome_do_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf)
    except:
        return jsonify({'resultado': False}),400       
    return jsonify({'resultado':True}),201


#+---------------------------------------+
#|Endpoint para adicionar um novo Placar |
#+----------------------------------------+
@app.route('/placar/<string:cpf>', methods=['POST'])
def placar(cpf):
    print(cpf)
    cpf=request.json.get('Cpf')
    pontuacao=request.json.get('Pontuacao')
    caractere=request.json.get('Caractere')
    modo_de_jogo=request.json.get('Modo_de_Jogo')
    insertPlacar2(cpf,pontuacao,caractere,modo_de_jogo)
    return jsonify(True), 201

#------------------------------------------------------------------------
#   *******   **     **  **********
#  /**////** /**    /** /////**/// 
#  /**   /** /**    /**     /**    
#  /*******  /**    /**     /**    
#  /**////   /**    /**     /**    
#  /**       /**    /**     /**    
#  /**       //*******      /**    
#  //         ///////       //     
#



#+-------------------------------------------------------+
#| Endpoint para atualizar o Cadastro existente pelo CPF |
#+-------------------------------------------------------+
@app.route('/cadastro/att/<int:id_jogador>', methods=['PUT'])
def att_cadastro(id_jogador):
    try:
        sexo = request.json.get('sexo')
        data_de_nascimento = request.json.get('data_de_nascimento')
        cidade = request.json.get('cidade')
        uf = request.json.get('uf')
        cep = request.json.get('cep')
        cpf = request.json.get('cpf')
        nome_do_jogador = request.json.get('nome_do_jogador')
        update_cadastro(id_jogador,sexo,data_de_nascimento,cidade,uf,cep,cpf,nome_do_jogador)
    except:
        return jsonify({'resultado': False}),400
    return jsonify({'resultado': True})


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
#+-----------------------------------------------------------------------------------+
#| Endpoint para deletar a Tabela Dados,Placar e Jogador pelo ID do Jogador|
#+-----------------------------------------------------------------------------------+
@app.route('/jogador/<int:id_jogador>', methods=['DELETE'])
def deletar_jogador(id_jogador):
    try:
        delete_dados_placar_jogador_idj(id_jogador)
    except:
        return jsonify({'resultado': False}),400   
    return jsonify({'resultado': True})


if __name__ == '__main__':
    app.run(debug=True, host=ip)

#------------------------------------------------------------------------------

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
             