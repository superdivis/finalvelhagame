//+--------------------------------------------------------------------------+
//| Projeto Final Velha                                                      |
//| Autores: Alexandre Santos e Bruno Gontijo                                |
//| Descrição: Projeto de jogo da velha com css inspirado em final fantasy 7 |
//| Data fim: 26/08/2024                                                     |
//| Data produção: 25/09/2024                                                |
//+--------------------------------------------------------------------------+

//+--------------------------------------------------------------------------------------------------------+
//|Variaveis capturando o elemento botão da pagina html com Doom, através do querySelector, Informando o ID|
//+--------------------------------------------------------------------------------------------------------+
var formulariodecaptura=document.querySelector("#formulario_de_captura");
var btn_aceitar = document.querySelector("#btn_aceitar");
var btn_cancelar = document.querySelector("#btn_cancelar");
var btn_buscar = document.querySelector("#btn_buscar");
var btn_salvar = document.querySelector("#btn_salvar");
var btn_excluir = document.querySelector("#btn_excluir")
var tabela_de_pontuacao=document.querySelector("#example");

//Botão de seleção do modo de jogo
var modo_solo=document.querySelector("#btn_solo");
var modo_multiplayer=document.querySelector("#btn_multiplayer");

var g_dados_jogador;
var endereco = 'https://finalvelhagame-c4c8841e9172.herokuapp.com'
//var ip = '192.168.0.58';
//var ip = "192.168.15.132"
var porta ='';


//+---------------------------------------------------+
//|Ativando o evento de click de mouse no Botão Salvar|
//+---------------------------------------------------+
if(btn_aceitar){
    btn_aceitar.addEventListener("click", function(event) {
        event.preventDefault(); //Evita que a página seja recarregada por padrão, isso facilita a captura e validação dos dados

        acaoBtnCadastro();

    });     
}

//+--------------------------------------------------+
//|Ativa o evento de click de mouse no Botão Cancelar|
//+--------------------------------------------------+
if(btn_cancelar){
    btn_cancelar.addEventListener("click", function(event) {
        event.preventDefault(); 
        //Limpa forulário
        formulariodecaptura.cpf.value = "";    
        formulariodecaptura.nome.value = "";
        formulariodecaptura.data.value = "";
        formulariodecaptura.sexo.value = "";
        formulariodecaptura.cidade.value = "";
        formulariodecaptura.uf.value = "";
        formulariodecaptura.cep.value = "";

});
}

//+--------------------------------------+
//|Ativar evento de click no botão buscar|
//+--------------------------------------+
if(btn_buscar){
    btn_buscar.addEventListener("click", function(event){
        event.preventDefault();
        
        var cpf = formulariodecaptura.cpf.value;
        pesquisarJogadorporCPF(cpf);
    });
}

//+--------------------------------------+
//|Ativar evento de click no botão salvar|
//+--------------------------------------+
if(btn_salvar){
    btn_salvar.addEventListener("click",function(event){
        event.preventDefault();
       
        
        g_dados_jogador[0].nome_do_jogador = formulariodecaptura.nome.value;
        g_dados_jogador[0].data_de_nascimento = formatacaoData(formulariodecaptura.data.value);
        g_dados_jogador[0].sexo = convercaoSexo(formulariodecaptura.sexo.value);
        g_dados_jogador[0].cidade = formulariodecaptura.cidade.value;
        g_dados_jogador[0].uf = formulariodecaptura.uf.value;
        g_dados_jogador[0].cep = formulariodecaptura.cep.value;
                        
        atualizarJogador(g_dados_jogador[0]);
       
    });
}

//+---------------------------------------+
//|Ativar evento de click no botão Excluir|
//+---------------------------------------+
if(btn_excluir){
    btn_excluir.addEventListener("click",function(event){
        event.preventDefault();

        deletarJogador(g_dados_jogador[0]);
    })
}

//+-------------------------------------------+
//|Ativar o evento de carregar a pagina Placar|
//+-------------------------------------------+
if(tabela_de_pontuacao){
        addEventListener("load",function(event){
        event.preventDefault();
        tabelaPlacar();
  
    });
}
