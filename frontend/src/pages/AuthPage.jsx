import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const AuthPage = ({ mode = "login" }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login, register } = useAuth();
  const navigate = useNavigate();

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (mode === "login") await login(email, password);
      else await register(email, password);
      navigate("/dashboard");
    } catch (err) {
      setError(err.response?.data?.error || "Request failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <form className="glass p-8 w-full max-w-md" onSubmit={onSubmit}>
        <h2 className="text-2xl font-semibold mb-5">{mode === "login" ? "Login" : "Register"}</h2>
        <input className="w-full mb-3 p-3 rounded bg-slate-900" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" className="w-full mb-3 p-3 rounded bg-slate-900" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        {error && <div className="text-cyber-danger text-sm mb-3">{error}</div>}
        <button className="w-full py-3 rounded bg-cyber-neon text-black font-semibold">{mode === "login" ? "Login" : "Create account"}</button>
      </form>
    </div>
  );
};

export default AuthPage;
