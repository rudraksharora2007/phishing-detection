import { useEffect, useState } from "react";
import api from "../services/api";

const AdminDashboard = () => {
  const [stats, setStats] = useState(null);
  const [retrainStatus, setRetrainStatus] = useState("");

  const loadStats = () => api.get("/admin/stats").then((res) => setStats(res.data));
  useEffect(() => { loadStats(); }, []);

  const retrain = async () => {
    const { data } = await api.post("/admin/retrain");
    setRetrainStatus(data.success ? "Model retrained" : "Retrain failed");
    loadStats();
  };

  if (!stats) return <div className="glass p-6">Loading...</div>;

  return (
    <div className="space-y-6">
      <div className="glass p-6">
        <h2 className="text-xl font-semibold mb-3">System Analytics</h2>
        <div>Total users: {stats.total_users}</div>
        <div>Total scans: {stats.total_scans}</div>
        <div>Safe: {stats.risk_distribution.safe} | Suspicious: {stats.risk_distribution.suspicious} | Dangerous: {stats.risk_distribution.dangerous}</div>
      </div>
      <div className="glass p-6">
        <button onClick={retrain} className="px-4 py-2 rounded bg-cyber-neon text-black font-semibold">Retrain model</button>
        {retrainStatus && <div className="mt-2 text-sm">{retrainStatus}</div>}
      </div>
    </div>
  );
};

export default AdminDashboard;
