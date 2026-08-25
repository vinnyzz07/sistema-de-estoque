document.addEventListener('DOMContentLoaded', function () {
    const campoBusca = document.getElementById('busca-produto');
    const filtroCategoria = document.getElementById('filtro-categoria');

    function filtrarProdutos() {
        const termo = campoBusca ? campoBusca.value.toLowerCase().trim() : '';
        const categoriaSelecionada = filtroCategoria ? filtroCategoria.value.toLowerCase() : '';
        const linhas = document.querySelectorAll('table tbody tr');

        linhas.forEach(function (linha) {
            const nomeProduto = linha.querySelector('td').textContent.toLowerCase();
            const categoriaProduto = linha.children[1].textContent.toLowerCase();

            const correspondeNome = nomeProduto.includes(termo);
            const correspondeCategoria = categoriaSelecionada === '' || categoriaProduto === categoriaSelecionada;

            if (correspondeNome && correspondeCategoria) {
                linha.style.display = '';
            } else {
                linha.style.display = 'none';
            }
        });
    }

    if (campoBusca) {
        campoBusca.addEventListener('input', filtrarProdutos);
    }

    if (filtroCategoria) {
        filtroCategoria.addEventListener('change', filtrarProdutos);
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const botoesAba = document.querySelectorAll('.aba');
    const conteudos = document.querySelectorAll('.conteudo-aba');

    botoesAba.forEach(function (botao) {
        botao.addEventListener('click', function () {
            const alvo = this.getAttribute('data-aba');

            botoesAba.forEach(b => b.classList.remove('ativa'));
            conteudos.forEach(c => c.classList.remove('ativa'));

            this.classList.add('ativa');
            document.getElementById(alvo).classList.add('ativa');
        });
    });
});