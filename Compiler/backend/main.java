// - - - - - - - - - - - - - - - - - - - -

// - - - - - - - - - - - - - - - - - - - -

// ESTA MADRE NO SE TOCA, AUN NO FUNCIONA COMO DEBERIA

// - - - - - - - - - - - - - - - - - - - -

// - - - - - - - - - - - - - - - - - - - -

package com.example.analizador;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@SpringBootApplication
@RestController
@RequestMapping("/api/v1")
@CrossOrigin(origins = "http://localhost:5137")
public class AnalizadorApplication {

    public static void main(String[] args) {
        SpringApplication.run(AnalizadorApplication.class, args);
    }

    // Modelo de entrada para el código fuente
    public static class CodigoFuente {
        private String codigo;

        public String getCodigo() {
            return codigo;
        }

        public void setCodigo(String codigo) {
            this.codigo = codigo;
        }
    }

    // Modelo para representar un token
    public static class Token {
        private String tipo;
        private int linea;
        private int columna;

        public Token(String tipo, int linea, int columna) {
            this.tipo = tipo;
            this.linea = linea;
            this.columna = columna;
        }

        public String getTipo() {
            return tipo;
        }

        public void setTipo(String tipo) {
            this.tipo = tipo;
        }

        public int getLinea() {
            return linea;
        }

        public void setLinea(int linea) {
            this.linea = linea;
        }

        public int getColumna() {
            return columna;
        }

        public void setColumna(int columna) {
            this.columna = columna;
        }
    }

    // Lógica del analizador léxico
    private static final String[] TOKEN_PATTERNS = {
            "PALABRA_RESERVADA", "\\b(int|float|bool|char|string|if|else|for|while|print|println)\\b",
            "IDENTIFICADOR", "\\b[a-zA-Z_][a-zA-Z0-9_]*\\b",
            "NUMERO", "\\b\\d+(\\.\\d+)?\\b",
            "OPERADOR_ARITMETICO", "[+\\-*/^#]",
            "OPERADOR_RELACIONAL", "(==|!=|<=|>=|<|>)",
            "OPERADOR_LOGICO", "(\\|\\||&&|!)",
            "ASIGNACION", "=",
            "DELIMITADOR", "[;{}()]",
            "COMENTARIO", "//.*|/\\*[\\s\\S]*?\\*/",
            "CADENA", "\"([^\"]|\\\\.)*\"",
            "CARACTER", "'.{1}'",
            "ESPACIO", "\\s+"
    };

    private static final Pattern TOKEN_REGEX = Pattern.compile(String.join("|", getPatterns()));

    private static String[] getPatterns() {
        String[] patterns = new String[TOKEN_PATTERNS.length / 2];
        for (int i = 1; i < TOKEN_PATTERNS.length; i += 2) {
            patterns[i / 2] = "(?P<" + TOKEN_PATTERNS[i - 1] + ">" + TOKEN_PATTERNS[i] + ")";
        }
        return patterns;
    }

    // Endpoint para recibir el código fuente y devolver los tokens
    @PostMapping("/analizador_lexico")
    public List<Token> analizarCodigo(@RequestBody CodigoFuente codigoFuente) {
        return analizar(codigoFuente.getCodigo());
    }

    // Método para realizar el análisis léxico
    private List<Token> analizar(String codigoFuente) {
        List<Token> tokens = new ArrayList<>();
        String[] lines = codigoFuente.split("\n");
        int lineNumber = 1;

        for (String line : lines) {
            Matcher matcher = TOKEN_REGEX.matcher(line);
            int pos = 0;

            while (matcher.find(pos)) {
                String tokenName = matcher.group();
                if (!tokenName.isEmpty()) {
                    tokens.add(new Token(tokenName, lineNumber, pos));
                    pos = matcher.end();
                }
            }
            lineNumber++;
        }
        return tokens;
    }
}
