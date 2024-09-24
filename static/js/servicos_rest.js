
// *******     *******     ********  **********
// /**////**   **/////**   **//////  /////**/// 
// /**   /**  **     //** /**            /**    
// /*******  /**      /** /*********     /**    
// /**////   /**      /** ////////**     /**    
// /**       //**     **        /**      /**    
// /**        //*******    ********      /**    
// //          ///////    ////////       //     

//+-----------------------------+
//|Função de Cadastro do Jogador|
//+-----------------------------+
function cadastrarJogados(dados_cadatro){
    const xhr = new XMLHttpRequest(dados_cadatro);
    xhr.open("POST", "http://"+ip+":"+ porta+"/cadastro", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8","Access-Control-Allow-Origin", "*");
    xhr.send(JSON.stringify(dados_cadatro));

    xhr.onload=function(){
        //alert("Jogador existente " + xhr.status);
        if (xhr.status ==201){ 
         alert("Cadastro efetuado com sucesso!")
        }else if (xhr.status == 400){ 
            alert("Erro: Jogador já existente!")
        };
    };
}

function atualizar_placar(placar){
    cpf=placar.Cpf
    const xhr = new XMLHttpRequest(placar);
    xhr.open( "POST", "http://"+ip+":"+porta+"/placar/:"+cpf, true ); // false for synchronous request
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8","Access-Control-Allow-Origin", "*");
    console.log(placar)
    xhr.send(JSON.stringify(placar));
    //return xmlHttp.responseText;
    xhr.onload = function(){
        if(xhr.status===200){
            var xmlHttp = new XMLHttpRequest();
            alert("Atualização efetuada com sucesso!");
        }
        
        else if(cpf.status===404){
            alert("Erro ao fazer a requisição!");
        }

    }
};


//    ********     ********  **********
//   **//////**   /**/////  /////**/// 
//  **      //    /**           /**    
//  /**           /*******      /**    
//  /**    *****  /**////       /**    
//  //**  ////**  /**           /**    
//   //********   /********     /**    
//    ////////    ////////      //     

//+---------------------------+
//|Função de Pesquisar Jogador| 
//+---------------------------+
function pesquisarJogadorporCPF(cpf){
    const xhr = new XMLHttpRequest(cpf);
    if(cpf!==""){
        xhr.open("GET", "http://"+ip+":"+porta+"/cpf/"+cpf, true);
        xhr.send();
    }else{
        alert("CPF inválido!");
        return false;
    }
    
    xhr.onload = function(){
        if(xhr.status===200){
            let endereco = JSON.parse(xhr.response);

            
            document.getElementById("cep").value =endereco[0].cep;
            document.getElementById("cidade").value =endereco[0].cidade;
            var ttt = formatacaoDataRecebimento (endereco[0].data_de_nascimento);
            document.getElementById("data").value = ttt;
            var sexo = endereco[0].sexo;
            document.getElementById("nome").value =endereco[0].nome_do_jogador;
            sexo = convercaoSexoAtualizar(sexo)
            document.getElementById("sexo").value =sexo;
            document.getElementById("uf").value =endereco[0].uf; 
            g_dados_jogador =  endereco;    
        } else if(cpf.status===404){
            alert("Erro ao fazer a requisição!");
            g_dados_jogador = null;
        }
    }

};

//+-----------------------------+
//|Função de Pesquisar o Placar |
//+-----------------------------+
function tabelaPlacar(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://"+ip+":"+porta+"/placar", true);
    xhr.send();
    xhr.onload= function(){
        if(xhr.status===200){
            let placar = JSON.parse(xhr.response);
            $(document).ready(function() {
                $('#example').DataTable( {
                
                data:placar,
                columns: [
                        {"data": 'nome_do_jogador'},
                        {"data": 'pontuacao'},
                        {"data": 'caractere',
                            render:function(data,type){
                                if(type==='display'){  
                                    var iconImage='';           
                                
                                    switch(data){
                                        case 'X':
                                            iconImage = 'Espada.png';
                                            break;

                                        case 'O':
                                            iconImage = 'Escudo.png';
                                            break;
                            };
                            return '<img src="../static/img/' + iconImage + '" alt="' + data + '" style="width: 24px; height: auto; vertical-align: middle;" />';                           
                        }
                        return data;
                        }
                        },
                        {"data": 'modo_de_jogo'}
            ],
            bPaginate: false,
            bFilter: false, 
            bInfo: false,
            order: [[2, 'asc']]
                
            } );
            } );

        }
    }


};

//  *******    **     **   **********
//  /**////**  /**    /**  /////**/// 
//  /**   /**  /**    /**      /**    
//  /*******   /**    /**      /**    
//  /**////    /**    /**      /**    
//  /**        /**    /**      /**    
//  /**        //*******       /**    
//  //          ///////        //     
//+-----------------------------+
//|Função de Atualizar Cadastro |
//+-----------------------------+
function atualizarJogador(dados_cadatro){
    const xhr = new XMLHttpRequest(dados_cadatro);
    id_jogador=dados_cadatro.id_jogador
    xhr.open( "PUT",  "http://"+ip+":"+porta+"/cadastro/att/"+id_jogador, true ); // false for synchronous request
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8","Access-Control-Allow-Origin", "*");
    console.log(dados_cadatro)
    xhr.send(JSON.stringify(dados_cadatro));
    //return xmlHttp.responseText;
    xhr.onload = function(){
        if(xhr.status===200){
            var xmlHttp = new XMLHttpRequest();
            alert("Atualização efetuada com sucesso!");
        }
        
        else if(cpf.status===404){
            alert("Erro ao fazer a requisição!");
        }

    }
};


//   *******      ********  **         ********   **********   ********
//  /**////**   /**/////   /**        /**/////   /////**///   /**///// 
//  /**    /**  /**        /**        /**            /**      /**      
//  /**    /**  /*******   /**        /*******       /**      /******* 
//  /**    /**  /**////    /**        /**////        /**      /**////  
//  /**    **   /**        /**        /**            /**      /**      
//  /*******    /********  /********  /********      /**      /********
//  ///////     ////////   ////////   ////////       //       //////// 
//+-------------------------+
//|Função de Deletar Jogador|
//+-------------------------+
function deletarJogador(dados_cadatro){
    const xhr = new XMLHttpRequest(dados_cadatro);
    id_jogador=dados_cadatro.id_jogador
    xhr.open( "DELETE",  "http://"+ip+":"+porta+"/jogador/"+id_jogador, true ); // false for synchronous request
    xhr.send();
    xhr.onload = function(){
        if(xhr.status===200){
            var xmlHttp = new XMLHttpRequest();
            alert("Exclusão efetuada com sucesso!")
        }
        
        else if(cpf.status===404){
            alert("Erro ao tentar excluir!");
        }

    }

}

console.log(`
                   #@@@ :@@@@@:"+
                  "+@*+@@@%+++++@@:                         
                  +@*+++@%++ :+@@@@@%                      
                  +@*++++*@%   %@##@%                      
              :@@@*+++++@@@@#- %@##@%                      
            .@%+++++++++@@@@#++@@@@@@@%                    
            .@%+*@*++++++++++++++%@##@%                    
            .@%+++++%@@@ :@@+++++%@##@%                    
              :@@@@@@@######+++++++@@@@@@@@@-              
                  +@#### .+*@#+++++@@@@##@@@-              
                  +@*++++*@@+++++++++@@@%+%@-              
                    #@@@@%+++++@@*+++@@+*@-                
                    #@+=++=+*++++%@@@@@+*@-                
                  +@@@@@===+@#+++++++@@@*                  
                :@*+++@@@@**@#+++++@@@%                    
                  +@@@@@@@@@@@@@@@@@%                      
                             =@*+++@%                      
                               %@@@.         `);
//+-------------------------------------------------------------------------------------------------+