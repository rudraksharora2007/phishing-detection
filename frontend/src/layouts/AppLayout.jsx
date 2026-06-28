import { Link, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const AppLayout = () => {
  const { user, logout } = useAuth();
  return (
    <div className="min-h-screen p-4 md:p-8">
      <nav className="glass p-4 mb-6 flex flex-wrap gap-3 items-center justify-between">
        <div className="font-semibold text-cyber-neon">AI Phishing Detection</div>
        <div className="flex gap-3 text-sm">
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/history">History</Link>
          {user?.is_admin && <Link to="/admin">Admin</Link>}
          <button onClick={logout} className="text-cyber-danger">Logout</button>
        </div>
      </nav>
      <Outlet />
    </div>
  );
};

export default AppLayout;
