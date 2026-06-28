import { useState } from "react";
import { motion } from "framer-motion";
import api from "../services/api";

const Dashboard = () => {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const analyze = async () => {
    setLoading(true);
    try {
      const { data } = await api.post("/predict", { url });
      setResult(data);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="glass p-6">
        <h2 className="text-xl font-semibold mb-3">URL Scanner</h2>
        <div className="flex flex-col md:flex-row gap-3">
          <input className="flex-1 p-3 rounded bg-slate-900" placeholder="https://example.com" value={url} onChange={(e) => setUrl(e.target.value)} />
          <button onClick={analyze} disabled={loading} className="px-5 py-3 rounded bg-cyber-neon text-black font-semibold">
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </div>
      </div>
      {result && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="glass p-6 space-y-3">
          <div className="text-lg font-semibold">Risk: {result.risk_level}</div>
          <div>Confidence: {result.confidence}%</div>
          <div className="w-full bg-slate-800 rounded h-3"><div className="h-3 rounded bg-cyber-neon" style={{ width: `${result.confidence}%` }} /></div>
          <div>
            <h3 className="font-semibold mb-1">Why this result</h3>
            <ul className="list-disc list-inside text-sm text-slate-300">
              {result.explanation.map((x) => <li key={x}>{x}</li>)}
            </ul>
          </div>
        </motion.div>
      )}
    </div>
  );
};

export default Dashboard;
