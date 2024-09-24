
//Função de Verificação dos Inputs se estão Preenchidos ou não
function validarDadosJogador(nome,sexo,data,cidade,uf,cep,cpf){
    var retorno = "";
    if (cpf == ""){
        retorno=" cpf";
    };
    if(nome == ""){
        retorno = retorno + " nome";
    };
    if (data ==""){
        retorno = retorno + " data";
    };
    if (sexo ==""){
        retorno = retorno + " sexo";
    };
    if (cidade == ""){
        retorno = retorno + " cidade";
    };
    if (uf == ""){
        retorno = retorno + " uf";
    };
    if (cep == ""){
        retorno = retorno + " cep ";
    };
    return retorno;

};

function montaJson(nome,sexo,novaData,cidade,uf,cep,cpf){

    ret = {
        "nome_do_jogador": nome,
        "sexo":sexo ,
        "data_de_nascimento":novaData ,
        "cidade":cidade ,
        "uf":uf ,
        "cep":cep ,
        "cpf":cpf     
        };
    return ret;
};


function monta_json_placar(cpf,pontuacao,caractere,modo_de_jogo){
    ret= {
        "Cpf":cpf,
        "Pontuacao":pontuacao ,
        "Caractere":caractere ,
        "Modo_de_Jogo":modo_de_jogo 
         }
    return ret    
};



//Formatação do input Data de Nascimento para o formato date 
function formatacaoDataRecebimento (data){     
    var ret = new Date(data)
    const formatter = Intl.DateTimeFormat('fr-CA',{ year:'numeric',month:'2-digit',day:'2-digit'});
    var dataFormatada = formatter.format(ret);
    ret = dataFormatada;
    return ret
};

//Função de Checagem de Arrays
function checkArrays(a1, a2) {
    return JSON.stringify(a1) === JSON.stringify(a2);
}

//Formatação do input Data de Nascimento para o formato date 
function formatacaoData (data){     
    var ret = data.split("-");
    var dd = ret[2];
    var mm=ret [1];
    var aa=ret[0];
    ret = dd+"/"+mm+"/"+aa;
    return ret
};

function convercaoSexoAtualizar(sexo){
    if (sexo=="M"){ 
    sexo="Homem";
    }else{
    sexo="Mulher";
    }
    return sexo;
};

function convercaoSexo(sexo){
    if (sexo=="Homem"){ 
    sexo="M";
    console.log("Sexo: "+sexo);
    }else{
    console.log("Sexo: "+sexo);
    sexo="F";
    }
    return sexo;
};

//+----------------------------------------+
//|Função referente ao cadastro de jogador | 
//+----------------------------------------+
function acaoBtnCadastro(){  
    //Capturando os dados das caixas de input, informando o elemento formulario, e acessando os atributos name de cada  caixa de texto
    var cpf = formulariodecaptura.cpf.value; 
    var nome = formulariodecaptura.nome.value;
    var data = formulariodecaptura.data.value;
    var sexo = formulariodecaptura.sexo.value;
    var cidade = formulariodecaptura.cidade.value;
    var uf = formulariodecaptura.uf.value;
    var cep = formulariodecaptura.cep.value;

    //+--------------------------------+
    //|Formatação dos dados para envio |
    //+--------------------------------+

    //Converção do input de Sexo para o formato char
    sexo = convercaoSexo(sexo);

    //Formatação do input Data de Nascimento para o formato date 
    data =formatacaoData (data);
    
    //Monta json 
    dados_jogador = montaJson(nome,sexo,data,cidade,uf,cep,cpf);

    var dado_ok = validarDadosJogador(nome,sexo,data,cidade,uf,cep,cpf);
    
    //Verifica função de cadastro e retorna se foi cadastrado
    if (dado_ok == ""){
        cadastrarJogados(dados_jogador);
    }else {
        alert("Os campos"+ dado_ok +"são obrigatorios!");
    }
};  

//+----------------------+
//|Verificador de vitoria|
//+----------------------+
function verifica_vencedor(board,global_p){
    var retorno = false;
    var linha1 = [board[0],board[1],board[2]];
    var linha2 = [board[3],board[4],board[5]];
    var linha3 = [board[6],board[7],board[8]];
    var coluna1 = [board[0],board[3],board[6]];
    var coluna2 = [board[1],board[4],board[7]];
    var coluna3 = [board[2],board[5],board[8]];
    var diagonal1 = [board[0],board[4],board[8]];
    var diagonal2 = [board[2],board[4],board[6]];
    var linha = [global_p,global_p,global_p]; 
    if (checkArrays(linha1,linha) || checkArrays(linha2,linha) || checkArrays(linha3,linha)){
        retorno = true;
    }
    else if (checkArrays(coluna1,linha) || checkArrays(coluna2,linha) || checkArrays(coluna3,linha)){
        retorno = true;
    }
    else if (checkArrays(diagonal1,linha) || checkArrays(diagonal2,linha)){
        retorno = true;
    }
       return retorno;
};
//Alternância de jogador
function troca_jogador(global_p){
    escudo=2;
    espada=1;    
    if (global_p ==escudo){
        global_p = espada;
    }else{
        global_p= escudo;
    }
    return global_p;
};

//+------------------------+
//| Verifica se tem empate |
//+------------------------+
function empate(board){
    var ret=true;
    for (i of board)
        if (i == 0){
        ret=false; 
        }
        return ret;
};

//+-----------------------------------+
//|Marca o board com o evento de click|
//+-----------------------------------+
function posicao_board(global_p,escolha,board,btn){
    if (global_p ==espada){        
        board[escolha] = global_p;
        //url('/static/img/Espada.png')
        btn.style.backgroundImage= 'url(/static/img/Espada.png)';
    }else if(global_p ==escudo){
        board[escolha] = global_p;
        btn.style.backgroundImage= 'url(/static/img/Escudo.png)';
    
    }
    };



function escolha_computador(global_p,comp){
    if(global_p==espada){
        comp=escudo
        return comp;
    }else if(global_p==escudo){
        comp=espada
        return comp;
    };
};


//+-----------------------------------------------+
//|Rotina de posicionamento do computador no board|
//+-----------------------------------------------+
function posicao_computador_board(board){
    var numeroAleatorio = Math.floor(Math.random() * 9);
    btn = document.querySelector("#btn_"+numeroAleatorio);    

    while(board[numeroAleatorio]!=0){

        empatou=empate(board);
        if(empatou){
            break
        }

        var numeroAleatorio = Math.floor(Math.random() * 9);
        btn = document.querySelector("#btn_"+numeroAleatorio);
    
        if (comp==espada && board[numeroAleatorio]==0){
            board[numeroAleatorio] = comp;
            document.getElementById("btn_"+numeroAleatorio).disabled = true;
            btn.style.backgroundImage= 'url(/static/img/Espada.png)';
            break
        }else if(comp==escudo && board[numeroAleatorio]==0){
            board[numeroAleatorio] = comp;
            document.getElementById("btn_"+numeroAleatorio).disabled = true;
            btn.style.backgroundImage= 'url(/static/img/Escudo.png)';
            break
    };    
    };  
    
    if (comp==espada && board[numeroAleatorio]==0){
        board[numeroAleatorio] = comp;
        document.getElementById("btn_"+numeroAleatorio).disabled = true;
        
        btn.style.backgroundImage= 'url(/static/img/Espada.png)';
        
    }else if(comp==escudo && board[numeroAleatorio]==0){
        board[numeroAleatorio] = comp;
        document.getElementById("btn_"+numeroAleatorio).disabled = true;
        btn.style.backgroundImage= 'url(/static/img/Escudo.png)';
    
    };
    };    


//+-----------------------------------------+
//|Reset do board efetuado ao fim da partida|
//+-----------------------------------------+
function reset_board(){
        btn_tabuleiro_0.style.backgroundImage= "url()";
        btn_tabuleiro_1.style.backgroundImage= "url()";
        btn_tabuleiro_2.style.backgroundImage= "url()";
        btn_tabuleiro_3.style.backgroundImage= "url()";
        btn_tabuleiro_4.style.backgroundImage= "url()";
        btn_tabuleiro_5.style.backgroundImage= "url()";
        btn_tabuleiro_6.style.backgroundImage= "url()";
        btn_tabuleiro_7.style.backgroundImage= "url()";
        btn_tabuleiro_8.style.backgroundImage= "url()";
        btn_tabuleiro_0.disabled = false;
        btn_tabuleiro_1.disabled = false;
        btn_tabuleiro_2.disabled = false;
        btn_tabuleiro_3.disabled = false;
        btn_tabuleiro_4.disabled = false;
        btn_tabuleiro_5.disabled = false;
        btn_tabuleiro_6.disabled = false;
        btn_tabuleiro_7.disabled = false;
        btn_tabuleiro_8.disabled = false;
        board = [0,0,0,0,0,0,0,0,0];
    };
//Resete das variaveis global_p
function reseta_jogador(global_p){
    if (global_p==2){
    global_p = escudo;
  }else{ 
    global_p = espada;
};
    return global_p;
};



function fim_jogo (board,global_p){
    //Verificação de vitoria
    vencedor = verifica_vencedor(board,global_p);
    var retorno = false;

    if(vencedor){
        if (global_p==1){
            pontos_espada = pontos_espada + pontuacao_vitoria;
            contador_1.innerText = pontos_espada 
            var msg=('Espada venceu! Jogar novamente ?');          
            retorno= true;
        }else if(global_p==2){
            pontos_escudo = pontos_escudo + pontuacao_vitoria;
            contador_2.innerText = pontos_escudo           
            var msg=('Escudo venceu! Jogar novamente ?');          
            retorno= true;
        };
        
        setTimeout(msg_final,100, msg);
    
        return retorno;
    };    

    
    //Verificação de empate
    empatou=empate(board);
    if(empatou){
        if (global_p==1 || global_p==2){    
            var msg=('Empate! Deseja jogar novamente ?');          
            retorno= true;
    
            };
        
            setTimeout(msg_final,100, msg); 

            return retorno;          
        };  
};


//+-------------------------------+
//|Mensagem de finalização do jogo|
//+-------------------------------+
function msg_final(msg_txt){       
    if (confirm(msg_txt) == true){
        global_p=reseta_jogador(global_p);
        reset_board();
        return global_p
    }else{
        var score=confirm('Gostaria de atualizar o score ?');        
        if (score==true){
            
            var cpf=prompt('Digite seu CPF aqui para que possamos atualizar seu score!');
            if (pontos_espada > pontos_escudo){
                caractere='X'
                
                placar=monta_json_placar(cpf,pontos_espada,caractere,modo_de_jogo);    
                atualizar_placar(placar);

                desabilitar_placar()

            }else if (pontos_escudo > pontos_espada){
                caractere='O'
                
                placar=monta_json_placar(cpf,pontos_escudo,caractere,modo_de_jogo);
                atualizar_placar(placar);  
                
                desabilitar_placar()
            };
 
        }else if(score==false){
                alert('Fim de jogo, obrigado por jogar!');           
                desabilitar_placar()
        };
          };
};

function msg_final_multiplayer(msg_txt){
    if (confirm(msg_txt) == true){
        global_p=troca_jogador(global_p);
        reset_board();
        return global_p
    }else{
        //Mensagem provisoria
        confirm('Gostaria de atualizar o score ?')
    };
}


//+--------------------------------+
//|Ação do evento de click do botão|
//+--------------------------------+
function jogada (escolha,btn){
    //+-----------+
    //|Rotina solo|
    //+-----------+
    if(modo_de_jogo=='S'){

        //Rotina do player
        posicao_board(global_p,escolha,board,btn);

        //Fim de jogo player
        if(fim_jogo(board,global_p)){
            return;
        } 

        //Rotina do computador
        comp=escolha_computador(global_p,comp);
        posicao_computador_board(board);
        
        //Fim de jogo player
        if (fim_jogo(board,comp)){
            return;
        }
        
    };

    //+------------------+
    //|Rotina multiplayer|
    //+------------------+
    if(modo_de_jogo=='M'){

        //Rotina do player
        posicao_board(global_p,escolha,board,btn);

        //Fim de jogos

        if(fim_jogo(board,global_p)){
            return;
        } 

        //Inversão do jogador
        global_p=troca_jogador(global_p);
        
    };
};
    

function desabilitar_placar(){
    btn_tabuleiro_0.disabled = true;
    btn_tabuleiro_1.disabled = true;
    btn_tabuleiro_2.disabled = true;
    btn_tabuleiro_3.disabled = true;
    btn_tabuleiro_4.disabled = true;
    btn_tabuleiro_5.disabled = true;
    btn_tabuleiro_6.disabled = true;
    btn_tabuleiro_7.disabled = true;
    btn_tabuleiro_8.disabled = true;
}