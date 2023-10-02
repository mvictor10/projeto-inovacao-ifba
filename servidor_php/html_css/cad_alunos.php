<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastar Aluno</title>
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>
    <div class="box">
        <ul class="menu">
			<li><a href="home.html">Home</a></li>
			<li><a href="cad_alunos.html">Cadastrar Aluno</a></li>
			<li><a href="reg_imagem.html">Adicionar Imagem</a></li>
			<li><a href="cad_usuario.html">Adicionar Usuário</a></li>
			<li><a href="sair.html">Sair</a></li>
		</ul>
    </div>

    <div class="form-container">
        <form action="registrar_student.php" method="POST" class="formlogin">
            <h3>Cadastrar Aluno</h3>
            <br>
            <div class="form-group">
                <label for="codigo">Código</label>
                <input placeholder="Digite o código" type="number" id="codigo" name="codigo" min="1"
                    oninput="toUpper(this)" max="99999999999" maxlength="11">
            </div>

            <div class="form-group">
                <label for="nome">Nome</label>
                <input type="text" id="nome" name="nome" placeholder="Digite o nome">
            </div>

            <div class="form-group">
                <label for="phone">Celular</label>
                <input type="tel" id="cel" name="cel" maxlength="15" placeholder="(XX) XXXXX-XXXX"
                    oninput="mascaraTelefone(this);">
            </div>

            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" placeholder="Digite o E-mail">
            </div>

            <div class="form-group">
                <button type="submit" name="login" id="login">Cadastrar</button>
            </div>
        </form>
    </div>
    <script src="./assets/js/script.js"></script>
</body>
</html>