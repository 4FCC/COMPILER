import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [codigo, setCodigo] = useState("");
  const [resultado, setResultado] = useState<string | object | null>(null);
  const [modo, setModo] = useState("lexico");
  const [cargando, setCargando] = useState(false);

  const analizarCodigo = async () => {
    setCargando(true);
    try {
      const endpoint = modo === "lexico"
        ? "http://localhost:8000/api/v1/analizador_lexico"
        : "http://localhost:8000/api/v1/analizador_sintactico";
      const response = await axios.post(endpoint, { codigo });
      setResultado(response.data);
    } catch (error) {
      setResultado("ERROR : Problemas técnicos con el backend");
      console.error("ERROR al analizar el código:", error);
    }
    setCargando(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white p-6 space-y-6">

      <h1 className="text-4xl font-bold text-green-400 drop-shadow-lg">Analizador de Código `(-_o)´</h1>

      <div className="flex gap-4">
        <button onClick={() => setModo("lexico")} className={`px-4 py-2 rounded-xl font-bold transition ${modo === "lexico" ? "bg-green-500" : "bg-gray-700 hover:bg-gray-600"}`}>Léxico</button>
        <button onClick={() => setModo("sintactico")} className={`px-4 py-2 rounded-xl font-bold transition ${modo === "sintactico" ? "bg-blue-500" : "bg-gray-700 hover:bg-gray-600"}`}>Sintáctico</button>
      </div>

      <div className="w-full max-w-2xl">
        <textarea
          className="w-full h-40 p-4 border-2 border-green-500 rounded-xl bg-gray-800 text-green-300 focus:ring-2 focus:ring-green-500 shadow-lg"
          placeholder="Escribe tu código aquí..."
          value={codigo}
          onChange={(e) => setCodigo(e.target.value)}
        />
      </div>

      <button
        className="px-6 py-3 bg-green-500 hover:bg-green-600 text-white font-bold rounded-xl transition duration-300 transform hover:scale-105 shadow-lg"
        onClick={analizarCodigo}
        disabled={cargando}
      >
        {cargando ? "Analizando..." : "Ejecutar Código"}
      </button>

      <div className="w-full max-w-4xl text-left">
        <h2 className="text-lg font-semibold text-green-300 mb-2">Resultado:</h2>
        <pre className="bg-black text-green-300 p-4 rounded-xl overflow-auto text-sm border border-green-500 shadow-lg max-h-96 whitespace-pre-wrap">
          {resultado ? JSON.stringify(resultado, null, 2) : "Aquí verás el resultado..."}
        </pre>
      </div>
    </div>
  );
}

export default App;
