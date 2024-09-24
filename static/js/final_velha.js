//+------------------------------------------+
//|Funcionalidades do tabuleiro jogo da velha|                                          |
//+------------------------------------------+

//+-----------------+
//|Variaveis globais|
//+-----------------+
var pontuacao_vitoria = 1
var pontuacao_empate = 0.5
var pontos_espada = 0
var pontos_escudo = 0
var modo_de_jogo;
var board = [0,0,0,0,0,0,0,0,0];
var espada=1;
var escudo=2;
var comp='';

//+-------------------------------------------+
//|Botão para escolher com qual elemento jogar|
//+-------------------------------------------+
var selecao_espada=document.querySelector("#btn_espada");
var selecao_escudo=document.querySelector("#btn_escudo");

//Contador de ponto
var contador_1 = document.querySelector('#contador_1');
var contador_2 = document.querySelector('#contador_2');

//+---------------------------------+
//|Botões do tabuleiro jogo da velha|
//+---------------------------------+
var  btn_tabuleiro_0 = document.querySelector("#btn_0")
var  btn_tabuleiro_1 = document.querySelector("#btn_1")
var  btn_tabuleiro_2 = document.querySelector("#btn_2")
var  btn_tabuleiro_3 = document.querySelector("#btn_3")
var  btn_tabuleiro_4 = document.querySelector("#btn_4")
var  btn_tabuleiro_5 = document.querySelector("#btn_5")
var  btn_tabuleiro_6 = document.querySelector("#btn_6")
var  btn_tabuleiro_7 = document.querySelector("#btn_7")
var  btn_tabuleiro_8 = document.querySelector("#btn_8")

//+--------------------+
//|Seleção do modo solo|
//+--------------------+
if(modo_solo){
    modo_solo.addEventListener("click", function(event){
        event.preventDefault();
        modo_de_jogo='S';
        document.getElementById("btn_escolha").style.display = "block";

        document.getElementById("btn_solo").disabled = true;
        document.getElementById("btn_multiplayer").disabled = true;
});
};

//+---------------------------+
//|Seleção do modo multiplayer|
//+---------------------------+
if(modo_multiplayer){
    modo_multiplayer.addEventListener("click", function(event){
        event.preventDefault();
        modo_de_jogo='M';
        document.getElementById("btn_escolha").style.display = "block";
        
        document.getElementById("btn_solo").disabled = true;
        document.getElementById("btn_multiplayer").disabled = true;
});
};


//+-----------------------+
//|Botão de seleção espada|
//+-----------------------+
if(selecao_espada){
    selecao_espada.addEventListener("click", function(event){
        event.preventDefault();
        document.getElementById("board").style.display = "grid";
        global_p=espada;
        document.getElementById("btn_espada").disabled = true;
        document.getElementById("btn_escudo").disabled = true;

        
    });
};

//+-----------------------+
//|Botão de seleção escudo|
//+-----------------------+
if(selecao_escudo){
    selecao_escudo.addEventListener("click", function(event){
        event.preventDefault();
        document.getElementById("board").style.display = "grid";
        global_p=escudo;
        document.getElementById("btn_espada").disabled = true;
        document.getElementById("btn_escudo").disabled = true;
        
    });
};


//+---------------------------------+
//|Botões do tabuleiro jogo da velha|
//+---------------------------------+
if(btn_tabuleiro_0){
    btn_tabuleiro_0.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=0;
        var btn = btn_tabuleiro_0
        
        jogada (escolha,btn);
    });
};



if(btn_tabuleiro_1){
    btn_tabuleiro_1.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=1;
        var btn = btn_tabuleiro_1
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_2){
    btn_tabuleiro_2.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=2;
        var btn = btn_tabuleiro_2
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_3){
    btn_tabuleiro_3.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=3;
        var btn = btn_tabuleiro_3
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_4){
    btn_tabuleiro_4.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=4;
        var btn = btn_tabuleiro_4
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_5){
    btn_tabuleiro_5.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=5;
        var btn = btn_tabuleiro_5
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_6){
    btn_tabuleiro_6.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=6;
        var btn = btn_tabuleiro_6

        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_7){
    btn_tabuleiro_7.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=7;
        var btn = btn_tabuleiro_7
        
        jogada (escolha,btn);
    });
}

if(btn_tabuleiro_8){
    btn_tabuleiro_8.addEventListener("click", function(event){
        event.preventDefault();
        var escolha=8;
        var btn = btn_tabuleiro_8
        
        jogada (escolha,btn);
    });
}



//                                                                                               %%%%%%
//                                                                                      %%%%% %%%%     
//                                                          %%%                  %%%%%%%%%%%%%         
//                                                         @%%%              %%%%%%%%%%%%%             
//                                                                 @%%   %%%%%%%%%%%%% %               
//                                                      %%  %% %%%%  %%%%%%%%%%%%%%%%%%                
//                                               @@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                     
//                                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
//                                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@                          
//                                   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                            
//                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@                              
//             @%%@   @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                
//          @%%        @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@                                  
//        %%             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                    
//      @%            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                       
//     %%@        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%                                       
//   @%%%%@     @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                         
//   %%%%%       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@                                          
//  %@%%%%     %%%@@%%%% @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                             
//  @%%%%        %%%@  %%%%%%%%%%@@%%%%%%%%%%%%%%%%%%%%@                                               
// %%%%%%        @   @%%%%%%%@     %%%%%%%%%%%%%%%%%%%%                                                
// %%                     %%%%%%   %%%%%%%%%%%%%%%%%%%%%                                               
// %                 %%%%%%%%%%%  %%%%%%%%%%%%%%%%%%%%%@                                               
// %                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@                                                
// %                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                 
// %                 @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                  
// @%                  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                   
//  @      @%@@ @%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                    
//   @  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                      
//      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% @%%%                                                        
//        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  %%%                                                          
//               %%%%%%%%%%%%%%%%%%%%%%%%%%                                                            
//              @%%%%%%%%%%%%%%%%%%%%%%%%                                                              
//               @%@@%%%%%%%%%%%%%%%%%                                                                 
//                    @%%%%%%%%%%            