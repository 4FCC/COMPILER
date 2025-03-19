import { useState } from 'react';
import axios from 'axios';
import dragonImg from "./assets/Tohru_29.png";
import './App.css';

function App() {
  const [codigo, setCodigo] = useState("");
  const [resultado, setResultado] = useState("");

  const analizarCodigo = async () => {
    try {
      const response = await axios.post("http://localhost:8000/api/v1/analizador_lexico", { codigo });
      setResultado(JSON.stringify(response.data, null, 2));
    } catch (error) {
      setResultado("❌ Error: Problemas técnicos, revisa la consola.");
      console.error("Error al analizar el código:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white p-6 space-y-6">
      {/* Imagen del Dragón */}
      {dragonImg ? (
        <img 
        src={dragonImg} 
        alt="Dragón" 
        className="mb-4 animate-pulse"
        style={{ width: "30%", height: "auto", maxWidth: "5000px", maxHeight: "5000px" }}
      />
      ) : (
        <p className="text-red-500">⚠️ Imagen no encontrada</p>
      )}
      
      {/* Título */}
      <h1 className="text-4xl font-bold text-green-400 drop-shadow-lg">Analizador Léxico</h1>
      
      {/* Área de código */}
      <div className="w-full max-w-2xl">
        <textarea
          className="w-full h-40 p-4 border-2 border-green-500 rounded-xl bg-gray-800 text-green-300 focus:ring-2 focus:ring-green-500 shadow-lg"
          placeholder="Escribe tu código aquí..."
          value={codigo}
          onChange={(e) => setCodigo(e.target.value)}
        />
      </div>

      {/* Botón de ejecución */}
      <button
        className="px-6 py-3 bg-green-500 hover:bg-green-600 text-white font-bold rounded-xl transition duration-300 transform hover:scale-105 shadow-lg"
        onClick={analizarCodigo}
      >
        🏆 Ejecutar Código
      </button>

      {/* Resultado */}
      <div className="w-full max-w-2xl">
        <pre className="bg-black text-green-300 p-4 rounded-xl overflow-auto text-sm border border-green-500 shadow-lg h-48">
          {resultado || "Aquí verás el resultado..."}
        </pre>
      </div>
    </div>
  );
}

export default App;
