import { useEffect, useState } from "react";
import api from "../services/api";

const HistoryPage = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    api.get("/history").then((res) => setItems(res.data));
  }, []);

  return (
    <div className="glass p-6 overflow-auto">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold">Scan History</h2>
        <a className="text-cyber-neon" href={`${import.meta.env.VITE_API_URL || "http://localhost:5000/api"}/history/export`}>Export CSV</a>
      </div>
      <table className="w-full text-sm">
        <thead><tr className="text-left"><th>URL</th><th>Result</th><th>Confidence</th><th>Timestamp</th></tr></thead>
        <tbody>
          {items.map((row) => (
            <tr key={row.id} className="border-t border-white/10">
              <td className="py-2 pr-2">{row.url}</td><td>{row.result}</td><td>{row.confidence}%</td><td>{new Date(row.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HistoryPage;
