from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


def calcular(a, b, operacao):
    if operacao == "somar":
        return a + b
    if operacao == "subtrair":
        return a - b
    if operacao == "multiplicar":
        return a * b
    if operacao == "dividir":
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b
    raise ValueError("Operação inválida.")


class CalculadoraHandler(BaseHTTPRequestHandler):
    def responder(self, resultado=""):
        pagina = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Docker</title>
</head>
<body>
    <h1>Calculadora Docker</h1>
    <form method="post" action="/">
        <input type="number" step="any" name="a"
               placeholder="Primeiro número" required>
        <select name="operacao">
            <option value="somar">Somar</option>
            <option value="subtrair">Subtrair</option>
            <option value="multiplicar">Multiplicar</option>
            <option value="dividir">Dividir</option>
        </select>
        <input type="number" step="any" name="b"
               placeholder="Segundo número" required>
        <button type="submit">Calcular</button>
    </form>
    <p>{resultado}</p>
</body>
</html>"""
        conteudo = pagina.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(conteudo)))
        self.end_headers()
        self.wfile.write(conteudo)

    def do_GET(self):
        self.responder()

    def do_POST(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        dados = parse_qs(self.rfile.read(tamanho).decode("utf-8"))

        try:
            resultado = calcular(
                float(dados["a"][0]),
                float(dados["b"][0]),
                dados["operacao"][0],
            )
            mensagem = f"Resultado: {resultado}"
        except (ValueError, KeyError):
            mensagem = "Confira os números. Não é possível dividir por zero."

        self.responder(mensagem)


if __name__ == "__main__":
    servidor = HTTPServer(("0.0.0.0", 5000), CalculadoraHandler)
    print("Calculadora disponível na porta 5000", flush=True)
    servidor.serve_forever()