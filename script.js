document.addEventListener("DOMContentLoaded", function () {
    // Carrinho de Compras
    let carrinho = {};

    // Adicionando produtos ao carrinho
    document.querySelectorAll("main > div").forEach((produto) => {
        produto.addEventListener("click", function () {
            let nomeProduto = produto.querySelectorAll("p")[1].innerText; // Pega o nome ao lado da "Imagem"
            exibirCaixaCorENome(nomeProduto);
        });
    });

    // Exibir itens do carrinho ao clicar no botão "Carrinho"
    document.getElementById("carrinho").addEventListener("click", function () {
        let caixaCarrinho = document.getElementById("caixa-carrinho");

        if (!caixaCarrinho) {
            caixaCarrinho = document.createElement("div");
            caixaCarrinho.id = "caixa-carrinho";
            caixaCarrinho.style.position = "fixed";
            caixaCarrinho.style.top = "50%";
            caixaCarrinho.style.left = "50%";
            caixaCarrinho.style.transform = "translate(-50%, -50%)";
            caixaCarrinho.style.background = "white";
            caixaCarrinho.style.padding = "20px";
            caixaCarrinho.style.border = "2px solid black";
            caixaCarrinho.style.borderRadius = "10px";
            caixaCarrinho.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.5)";
            caixaCarrinho.style.zIndex = "1000";
            caixaCarrinho.style.maxWidth = "300px"; // Limitar largura da caixa

            // Adicionar botão de fechar (X)
            let closeButton = document.createElement("span");
            closeButton.innerText = "X";
            closeButton.style.position = "absolute";
            closeButton.style.top = "10px";
            closeButton.style.right = "10px";
            closeButton.style.cursor = "pointer";
            closeButton.style.fontSize = "20px"; // Aumentar o tamanho do "X"
            closeButton.style.color = "red";
            closeButton.addEventListener("click", function () {
                caixaCarrinho.remove();
            });
            caixaCarrinho.appendChild(closeButton);

            // Botão de limpar carrinho
            let botaoLimpar = document.createElement("button");
            botaoLimpar.innerText = "Limpar Carrinho";
            botaoLimpar.style.display = "block";
            botaoLimpar.style.margin = "10px auto";
            botaoLimpar.style.padding = "10px";
            botaoLimpar.style.backgroundColor = "red";
            botaoLimpar.style.color = "white";
            botaoLimpar.style.border = "none";
            botaoLimpar.style.borderRadius = "5px";
            botaoLimpar.style.cursor = "pointer";
            botaoLimpar.addEventListener("click", function () {
                carrinho = {}; // Limpar carrinho
                atualizarCarrinho(); // Atualizar a visualização
            });

            caixaCarrinho.appendChild(botaoLimpar);
            document.body.appendChild(caixaCarrinho);
        }

        // Atualizar os itens do carrinho
        atualizarCarrinho();
    });

    // Função para atualizar o carrinho
    // Função para atualizar o carrinho
function atualizarCarrinho() {
    let caixaCarrinho = document.getElementById("caixa-carrinho");
    let listaCarrinho = document.createElement("div");

    if (Object.keys(carrinho).length > 0) {
        let totalPreco = 0;
        for (let item in carrinho) {
            // Criar um item na lista
            let itemCarrinho = document.createElement("div");
            itemCarrinho.style.display = "flex";
            itemCarrinho.style.alignItems = "center";
            itemCarrinho.style.marginBottom = "10px";

            let textoItem = document.createElement("span");
            textoItem.innerText = `${item} (x${carrinho[item].quantidade})`;
            
            // Adicionar cor e nome (se houver)
            if (carrinho[item].cor) {
                textoItem.innerText += ` - Cor: ${carrinho[item].cor}`;
            }
            if (carrinho[item].nome) {
                textoItem.innerText += ` - Nome: ${carrinho[item].nome}`;
            }

            itemCarrinho.appendChild(textoItem);

            // Botões para alterar a quantidade
            let botaoDiminuir = document.createElement("button");
            botaoDiminuir.innerText = "-";
            botaoDiminuir.style.marginLeft = "10px";
            botaoDiminuir.addEventListener("click", function () {
                if (carrinho[item].quantidade > 1) {
                    carrinho[item].quantidade -= 1;
                    atualizarCarrinho();
                }
            });

            let botaoAumentar = document.createElement("button");
            botaoAumentar.innerText = "+";
            botaoAumentar.style.marginLeft = "10px";
            botaoAumentar.addEventListener("click", function () {
                carrinho[item].quantidade += 1;
                atualizarCarrinho();
            });

            itemCarrinho.appendChild(botaoDiminuir);
            itemCarrinho.appendChild(botaoAumentar);

            // Lixeira para remover item
            let lixeira = document.createElement("button");
            lixeira.innerText = "🗑️";
            lixeira.style.marginLeft = "10px";
            lixeira.style.cursor = "pointer";
            lixeira.addEventListener("click", function () {
                delete carrinho[item];
                atualizarCarrinho();
            });

            itemCarrinho.appendChild(lixeira);
            listaCarrinho.appendChild(itemCarrinho);

            // Calcular o total de preços (supondo um preço fixo por item)
            totalPreco += 10 * carrinho[item].quantidade; // Ajuste conforme necessário para o preço real do item
        }

        // Adicionar botão de finalizar pedido
        let botaoFinalizar = document.createElement("button");
        botaoFinalizar.innerText = "Finalizar Pedido";
        botaoFinalizar.style.marginTop = "10px";
        botaoFinalizar.style.padding = "10px";
        botaoFinalizar.style.backgroundColor = "green";
        botaoFinalizar.style.color = "white";
        botaoFinalizar.style.border = "none";
        botaoFinalizar.style.borderRadius = "5px";
        botaoFinalizar.style.cursor = "pointer";
        botaoFinalizar.addEventListener("click", function () {
            finalizarPedido();
        });

        listaCarrinho.appendChild(botaoFinalizar);

        // Exibir total do carrinho
        let totalCarrinho = document.createElement("div");
        totalCarrinho.innerText = `Total: R$ ${totalPreco}`;
        listaCarrinho.appendChild(totalCarrinho);
    } else {
        listaCarrinho.innerText = "Seu carrinho está vazio!";
    }

    // Atualizar o conteúdo da caixa de carrinho
    caixaCarrinho.innerHTML = "";
    caixaCarrinho.appendChild(listaCarrinho);
}

    // Função para finalizar o pedido
    function finalizarPedido() {
        let mensagem = "Pedido:\n";
        for (let item in carrinho) {
            mensagem += `${item} (x${carrinho[item].quantidade})\n`;
        }

        let numeroWhatsApp = "82 999999999"; // Número para enviar
        let url = `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(mensagem)}`;

        // Enviar mensagem para o WhatsApp
        window.open(url, "_blank");

        // Limpar carrinho após envio
        carrinho = {};
        atualizarCarrinho(); // Atualizar visualização do carrinho
    }

    // Função para exibir a mensagem de sucesso
    function exibirMensagemSucesso(nomeProduto) {
        let mensagem = document.createElement("div");
        mensagem.id = "mensagem-sucesso";
        mensagem.style.position = "fixed";
        mensagem.style.top = "20px";
        mensagem.style.left = "50%";
        mensagem.style.transform = "translateX(-50%)";
        mensagem.style.background = "#4CAF50";
        mensagem.style.color = "white";
        mensagem.style.padding = "10px 20px";
        mensagem.style.borderRadius = "5px";
        mensagem.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.5)";
        mensagem.style.zIndex = "1000";
        mensagem.innerText = `${nomeProduto} adicionado com sucesso!`;

        document.body.appendChild(mensagem);

        setTimeout(function () {
            mensagem.remove();
        }, 3000);
    }

    // Função para exibir caixa de cor e nome ao clicar em um bolo
    function exibirCaixaCorENome(nomeProduto) {
        let caixaCorNome = document.createElement("div");
        caixaCorNome.id = "caixa-cor-nome";
        caixaCorNome.style.position = "fixed";
        caixaCorNome.style.top = "50%";
        caixaCorNome.style.left = "50%";
        caixaCorNome.style.transform = "translate(-50%, -50%)";
        caixaCorNome.style.background = "orange";
        caixaCorNome.style.padding = "20px";
        caixaCorNome.style.border = "2px solid black";
        caixaCorNome.style.borderRadius = "10px";
        caixaCorNome.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.5)";
        caixaCorNome.style.zIndex = "1000";

        let closeButton = document.createElement("span");
        closeButton.innerText = "X";
        closeButton.style.position = "absolute";
        closeButton.style.top = "10px";
        closeButton.style.right = "10px";
        closeButton.style.cursor = "pointer";
        closeButton.style.fontSize = "20px";
        closeButton.style.color = "red";
        closeButton.addEventListener("click", function () {
            caixaCorNome.remove();
        });
        caixaCorNome.appendChild(closeButton);

        let labelCor = document.createElement("label");
        labelCor.innerText = "Escolha a cor do bolo (obrigatória): ";
        let selectCor = document.createElement("select");
        let cores = ["Roxo", "Azul", "Rosa", "Verde", "Vermelho"];
        cores.forEach(cor => {
            let option = document.createElement("option");
            option.value = cor;
            option.innerText = cor;
            selectCor.appendChild(option);
        });
        caixaCorNome.appendChild(labelCor);
        caixaCorNome.appendChild(selectCor);

        let labelNome = document.createElement("label");
        labelNome.innerText = "Nome no bolo (opcional): ";
        let inputNome = document.createElement("input");
        inputNome.type = "text";
        caixaCorNome.appendChild(labelNome);
        caixaCorNome.appendChild(inputNome);

        let botaoConfirmar = document.createElement("button");
        botaoConfirmar.innerText = "Confirmar";
        botaoConfirmar.addEventListener("click", function () {
            let corSelecionada = selectCor.value;
            let nomeBolo = inputNome.value || "Sem nome";

            if (carrinho[nomeProduto]) {
                carrinho[nomeProduto].quantidade += 1;
            } else {
                carrinho[nomeProduto] = { cor: corSelecionada, nome: nomeBolo, quantidade: 1 };
            }

            caixaCorNome.remove();
            exibirMensagemSucesso(nomeProduto);
        });

        caixaCorNome.appendChild(botaoConfirmar);
        document.body.appendChild(caixaCorNome);
    }
});
