package com.example.analizador;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.LinkedHashMap;
import java.util.Map;

@SpringBootApplication
public class AnalizadorLexicoApp {

    public static void main(String[] args) {
        SpringApplication.run(AnalizadorLexicoApp.class, args);
    }

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/v1/**")
                        .allowedOrigins("http://localhost:5173")
                        .allowedMethods("*")
                        .allowedHeaders("*");
            }
        };
    }

    @RestController
    @RequestMapping("/api/v1")
    public static class AnalizadorLexicoController {

        private static final Map<String, String> TOKEN_PATTERNS = new LinkedHashMap<>();

        static {
            TOKEN_PATTERNS.put("PALABRA_RESERVADA", "\\b(int|float|bool|char|string|if|else|for|while|print|println)\\b");
            TOKEN_PATTERNS.put("IDENTIFICADOR", "\\b[a-zA-Z_][a-zA-Z0-9_]*\\b");
            TOKEN_PATTERNS.put("NUMERO", "\\b\\d+(\\.\\d+)?\\b");
            TOKEN_PATTERNS.put("OPERADOR_ARITMETICO", "[+\\-*/^#]");
            TOKEN_PATTERNS.put("OPERADOR_RELACIONAL", "(==|!=|<=|>=|<|>)");
            TOKEN_PATTERNS.put("OPERADOR_LOGICO", "(\\|\\||&&|!)");
            TOKEN_PATTERNS.put("ASIGNACION", "=");
            TOKEN_PATTERNS.put("DELIMITADOR", "[;{}()]");
            TOKEN_PATTERNS.put("COMENTARIO", "//.*|/\\*[\\s\\S]*?\\*/");
            TOKEN_PATTERNS.put("CADENA", "\"([^\"\\\\]|\\\\.)*\"");
            TOKEN_PATTERNS.put("CARACTER", "'.{1}'");
            TOKEN_PATTERNS.put("ESPACIO", "\\s+");
        }

        private static final Pattern TOKEN_REGEX = Pattern.compile(String.join("|", TOKEN_PATTERNS.values()), Pattern.CASE_INSENSITIVE);

        public static class CodigoFuente {
            private String codigo;

            public String getCodigo() {
                return codigo;
            }

            public void setCodigo(String codigo) {
                this.codigo = codigo;
            }
        }

        public static class Token {
            private String tipo;
            private String valor;
            private int linea;
            private int columna;

            public Token(String tipo, String valor, int linea, int columna) {
                this.tipo = tipo;
                this.valor = valor;
                this.linea = linea;
                this.columna = columna;
            }

            public String getTipo() { return tipo; }
            public void setTipo(String tipo) { this.tipo = tipo; }
            public String getValor() { return valor; }
            public void setValor(String valor) { this.valor = valor; }
            public int getLinea() { return linea; }
            public void setLinea(int linea) { this.linea = linea; }
            public int getColumna() { return columna; }
            public void setColumna(int columna) { this.columna = columna; }
        }

        @PostMapping("/analizador_lexico")
        public List<Token> analizarCodigo(@RequestBody CodigoFuente codigoFuente) {
            String codigo = codigoFuente.getCodigo();
            List<Token> tokens = new ArrayList<>();
            String[] lineas = codigo.split("\\n");

            for (int numLinea = 0; numLinea < lineas.length; numLinea++) {
                String linea = lineas[numLinea];
                Matcher matcher = TOKEN_REGEX.matcher(linea);
                int pos = 0;

                while (matcher.find(pos)) {
                    for (Map.Entry<String, String> entry : TOKEN_PATTERNS.entrySet()) {
                        if (matcher.group().matches(entry.getValue())) {
                            if (!entry.getKey().equals("COMENTARIO") && !entry.getKey().equals("ESPACIO")) {
                                tokens.add(new Token(
                                    entry.getKey(),
                                    matcher.group(),
                                    numLinea + 1,
                                    matcher.start() + 1
                                ));
                            }
                            break;
                        }
                    }
                    pos = matcher.end();
                }
            }
            return tokens;
        }
    }
}
