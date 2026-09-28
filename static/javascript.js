// Aguarda todo o HTML carregar antes de executar o script
document.addEventListener("DOMContentLoaded", function() {
    
    // Função principal responsável por clonar qualquer bloco do formulário
    function ativarClonagem(idBotao, idSecao, classeBloco) {
        const botao = document.getElementById(idBotao);
        const secao = document.getElementById(idSecao);

        botao.addEventListener("click", function() {
            // Pega o primeiro bloco da seção para usar como "molde"
            const blocos = secao.querySelectorAll("." + classeBloco);
            const blocoMolde = blocos[0];
            
            // Faz a cópia exata do HTML do bloco (true copia os elementos internos também)
            const novoBloco = blocoMolde.cloneNode(true);

            // Limpa os valores dos inputs e textareas do bloco copiado
            const campos = novoBloco.querySelectorAll("input, textarea");
            campos.forEach(function(campo) {
                if (campo.type === "checkbox") {
                    campo.checked = false; // Desmarca o checkbox
                } else {
                    campo.value = ""; // Apaga o texto
                }
            });

            // Cria dinamicamente um botão "Remover" para o novo bloco
            const btnRemover = document.createElement("button");
            btnRemover.type = "button";
            btnRemover.textContent = "Remover esta entrada";
            
            // Estilização injetada via JS (dispensa criar classe no CSS agora)
            btnRemover.style.backgroundColor = "#ef4444"; // Vermelho
            btnRemover.style.color = "white";
            btnRemover.style.padding = "8px 12px";
            btnRemover.style.marginTop = "10px";
            btnRemover.style.marginBottom = "20px";
            btnRemover.style.border = "none";
            btnRemover.style.borderRadius = "4px";
            btnRemover.style.cursor = "pointer";
            btnRemover.style.width = "100%";

            // Adiciona a ação de deletar o bloco quando clicar no botão vermelho
            btnRemover.addEventListener("click", function() {
                novoBloco.remove();
            });

            // Coloca o botão remover no final do novo bloco clonado
            novoBloco.appendChild(btnRemover);

            // Insere o novo bloco na tela, logo acima do botão "+ Adicionar"
            secao.insertBefore(novoBloco, botao);
        });
    }

    // Aciona a função para a seção de Experiências Profissionais
    ativarClonagem("btn-add-experiencia", "secao-experiencias", "bloco-experiencia");

    // Aciona a função para a seção de Formações Acadêmicas
    ativarClonagem("btn-add-formacao", "secao-formacoes", "bloco-formacao");

});